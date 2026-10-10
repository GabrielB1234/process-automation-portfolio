import csv
import json
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "sample_input.csv"
RULES_FILE = BASE_DIR / "rules.json"
OUTPUT_FILE = BASE_DIR / "validation_results.csv"


@dataclass(frozen=True)
class RuleSet:
    version: str
    effective_from: date
    eligible_categories: set[str]
    maximum_amount: float
    required_document: bool


def parse_date(value: str) -> date:
    return datetime.strptime(value.strip(), "%Y-%m-%d").date()


def parse_optional_bool(value: str):
    normalized = value.strip().lower()
    if normalized == "":
        return None
    if normalized in {"true", "yes", "1"}:
        return True
    if normalized in {"false", "no", "0"}:
        return False
    return None


def load_rule_sets() -> list[RuleSet]:
    payload = json.loads(RULES_FILE.read_text(encoding="utf-8"))
    rule_sets = []

    for item in payload["rule_sets"]:
        rule_sets.append(
            RuleSet(
                version=item["version"],
                effective_from=parse_date(item["effective_from"]),
                eligible_categories={value.upper() for value in item["eligible_categories"]},
                maximum_amount=float(item["maximum_amount"]),
                required_document=bool(item["required_document"]),
            )
        )

    return sorted(rule_sets, key=lambda rule: rule.effective_from)


def select_rule_set(rule_sets: list[RuleSet], event_date: date):
    applicable = [rule for rule in rule_sets if rule.effective_from <= event_date]
    return applicable[-1] if applicable else None


def load_records():
    required_columns = {
        "record_id",
        "category",
        "amount",
        "event_date",
        "has_required_document",
    }

    with INPUT_FILE.open("r", newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        columns = set(reader.fieldnames or [])
        missing = required_columns - columns
        if missing:
            raise ValueError(f"Missing required columns: {sorted(missing)}")

        return [row for row in reader]


def validate_record(record, rule_sets):
    reasons = []

    record_id = record["record_id"].strip()
    category = record["category"].strip().upper()

    try:
        amount = float(record["amount"].strip())
    except ValueError:
        return {
            "record_id": record_id,
            "decision": "REVIEW_REQUIRED",
            "rule_version": "",
            "reason_codes": "INVALID_AMOUNT_FORMAT",
            "explanation": "Amount could not be parsed safely.",
        }

    try:
        event_date = parse_date(record["event_date"])
    except ValueError:
        return {
            "record_id": record_id,
            "decision": "REVIEW_REQUIRED",
            "rule_version": "",
            "reason_codes": "INVALID_DATE_FORMAT",
            "explanation": "Event date could not be parsed safely.",
        }

    rule = select_rule_set(rule_sets, event_date)
    if rule is None:
        return {
            "record_id": record_id,
            "decision": "REVIEW_REQUIRED",
            "rule_version": "",
            "reason_codes": "NO_APPLICABLE_RULE_SET",
            "explanation": "No fictional rule set applies to the supplied date.",
        }

    document_flag = parse_optional_bool(record["has_required_document"])

    if category not in rule.eligible_categories:
        reasons.append(("CATEGORY_NOT_ELIGIBLE", "Category is not eligible under the selected rule set."))

    if amount > rule.maximum_amount:
        reasons.append(("AMOUNT_ABOVE_LIMIT", "Amount exceeds the fictional maximum allowed by the selected rule set."))

    if rule.required_document and document_flag is None:
        return {
            "record_id": record_id,
            "decision": "REVIEW_REQUIRED",
            "rule_version": rule.version,
            "reason_codes": "DOCUMENT_STATUS_MISSING",
            "explanation": "Document status is missing, so the engine will not force a yes/no result.",
        }

    if rule.required_document and document_flag is False:
        reasons.append(("REQUIRED_DOCUMENT_MISSING", "A required fictional document is not present."))

    if reasons:
        return {
            "record_id": record_id,
            "decision": "INVALID",
            "rule_version": rule.version,
            "reason_codes": ";".join(code for code, _ in reasons),
            "explanation": " ".join(message for _, message in reasons),
        }

    return {
        "record_id": record_id,
        "decision": "VALID",
        "rule_version": rule.version,
        "reason_codes": "PASSED_ALL_RULES",
        "explanation": "Record passed all fictional deterministic checks.",
    }


def write_results(results):
    fieldnames = [
        "record_id",
        "decision",
        "rule_version",
        "reason_codes",
        "explanation",
    ]

    with OUTPUT_FILE.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)


def main():
    rule_sets = load_rule_sets()
    records = load_records()
    results = [validate_record(record, rule_sets) for record in records]
    write_results(results)

    for result in results:
        print(
            f"{result['record_id']}: {result['decision']} "
            f"({result['rule_version'] or 'no rule'}) - {result['reason_codes']}"
        )

    print(f"\nResults written to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
