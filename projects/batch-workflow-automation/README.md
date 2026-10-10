# Batch Workflow Automation

A fully synthetic browser-automation project that demonstrates reliable batch execution without using any production system, employer code, or real operational data.

## What it demonstrates

- spreadsheet-style batch input through CSV;
- record-level processing;
- Selenium browser automation;
- explicit UI waits;
- retry of transient failures;
- isolation of permanent failures;
- CSV execution logging;
- checkpoint-based restartability;
- continuation after an individual record fails.

## Synthetic workflow

The project opens a local HTML application and processes fictional records.

Each row contains:

- a fictional record ID;
- a fictional owner;
- a generic decision;
- a generic comment;
- a failure mode used only to demonstrate error handling.

The local application can intentionally produce a transient or permanent failure so the automation's retry and recovery behavior can be observed.

## Run

Install the dependency:

```bash
pip install -r requirements.txt
```

Run with a visible Chrome window:

```bash
python automation.py --reset
```

Or run headless:

```bash
python automation.py --reset --headless
```

## Output

Runtime files are generated locally and ignored by Git:

- `run_log.csv`
- `checkpoint.json`

The checkpoint allows a later run to skip records already completed successfully.

## Reliability choices

A batch is not treated as one giant transaction. Every record is processed independently.

A transient failure is retried within a defined limit. A permanent failure is logged and the remaining queue continues. Successful records are checkpointed immediately so a later restart does not need to repeat them.

## Confidentiality

This project is independently written for portfolio demonstration. The data, interface, selectors, workflow states, and code are fictional and are not copied from any production implementation.
