import argparse
import csv
import json
import time
from pathlib import Path
from urllib.parse import urlencode

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "sample_input.csv"
MOCK_APP = BASE_DIR / "mock_app.html"
LOG_FILE = BASE_DIR / "run_log.csv"
CHECKPOINT_FILE = BASE_DIR / "checkpoint.json"
WAIT_SECONDS = 5
MAX_ATTEMPTS = 2


def load_records():
    required_columns = {"record_id", "owner", "decision", "comment", "failure_mode"}

    with INPUT_FILE.open("r", newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        columns = set(reader.fieldnames or [])
        missing = required_columns - columns
        if missing:
            raise ValueError(f"Missing required columns: {sorted(missing)}")

        records = []
        seen_ids = set()

        for row in reader:
            record_id = row["record_id"].strip()
            if not record_id or record_id in seen_ids:
                continue
            seen_ids.add(record_id)
            records.append({key: value.strip() for key, value in row.items()})

    return records


def load_checkpoint():
    if not CHECKPOINT_FILE.exists():
        return set()

    try:
        payload = json.loads(CHECKPOINT_FILE.read_text(encoding="utf-8"))
        return set(payload.get("completed", []))
    except (OSError, json.JSONDecodeError, TypeError):
        return set()


def save_checkpoint(completed):
    CHECKPOINT_FILE.write_text(
        json.dumps({"completed": sorted(completed)}, indent=2),
        encoding="utf-8",
    )


def append_log(record_id, status, attempt, duration_seconds, error=""):
    first_write = not LOG_FILE.exists()

    with LOG_FILE.open("a", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        if first_write:
            writer.writerow(
                ["timestamp", "record_id", "status", "attempt", "duration_seconds", "error"]
            )

        writer.writerow(
            [
                time.strftime("%Y-%m-%d %H:%M:%S"),
                record_id,
                status,
                attempt,
                f"{duration_seconds:.3f}",
                error,
            ]
        )


def build_url(record, attempt):
    query = urlencode(
        {
            "record": record["record_id"],
            "failure_mode": record["failure_mode"],
            "attempt": attempt,
        }
    )
    return f"{MOCK_APP.as_uri()}?{query}"


def process_record(driver, record, attempt):
    driver.get(build_url(record, attempt))
    wait = WebDriverWait(driver, WAIT_SECONDS)

    wait.until(
        EC.text_to_be_present_in_element((By.ID, "record-id"), record["record_id"])
    )

    owner = wait.until(EC.element_to_be_clickable((By.ID, "owner")))
    owner.clear()
    owner.send_keys(record["owner"])

    decision = driver.find_element(By.ID, "decision")
    decision.send_keys(record["decision"])

    comment = driver.find_element(By.ID, "comment")
    comment.clear()
    comment.send_keys(record["comment"])

    driver.find_element(By.ID, "submit-action").click()

    try:
        wait.until(EC.text_to_be_present_in_element((By.ID, "result"), "SUCCESS"))
    except TimeoutException as exc:
        result = driver.find_element(By.ID, "result").text.strip()
        raise RuntimeError(result or "No success confirmation returned") from exc


def run(reset=False, headless=False):
    if reset:
        for path in (LOG_FILE, CHECKPOINT_FILE):
            if path.exists():
                path.unlink()

    records = load_records()
    completed = load_checkpoint()

    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=options)

    counts = {"success": 0, "skipped": 0, "failed": 0}

    try:
        for index, record in enumerate(records, start=1):
            record_id = record["record_id"]

            if record_id in completed:
                counts["skipped"] += 1
                print(f"[{index}/{len(records)}] {record_id}: skipped from checkpoint")
                continue

            final_error = ""
            print(f"[{index}/{len(records)}] {record_id}")

            for attempt in range(1, MAX_ATTEMPTS + 1):
                started = time.perf_counter()

                try:
                    process_record(driver, record, attempt)
                    duration = time.perf_counter() - started
                    append_log(record_id, "SUCCESS", attempt, duration)
                    completed.add(record_id)
                    save_checkpoint(completed)
                    counts["success"] += 1
                    print(f"  success on attempt {attempt}")
                    break
                except Exception as exc:
                    duration = time.perf_counter() - started
                    final_error = str(exc)
                    append_log(record_id, "ERROR", attempt, duration, final_error)
                    print(f"  attempt {attempt} failed: {final_error}")
            else:
                counts["failed"] += 1
                print(f"  final failure: {final_error}")

    finally:
        driver.quit()

    print("\nRun summary")
    print(f"Successful: {counts['success']}")
    print(f"Skipped:    {counts['skipped']}")
    print(f"Failed:     {counts['failed']}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Synthetic batch workflow automation demo")
    parser.add_argument("--reset", action="store_true", help="Clear runtime files before execution")
    parser.add_argument("--headless", action="store_true", help="Run Chrome without a visible window")
    arguments = parser.parse_args()

    run(reset=arguments.reset, headless=arguments.headless)
