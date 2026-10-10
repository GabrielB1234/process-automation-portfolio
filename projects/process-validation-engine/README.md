# Process Validation Engine

A synthetic rule-driven validation project that separates business rules from execution logic.

The project is intentionally generic. All field names, thresholds, categories, rule versions, and sample records are fictional.

## What it demonstrates

- configuration-driven rules;
- rule-version selection by effective date;
- data normalization;
- explainable decisions;
- explicit `VALID`, `INVALID`, and `REVIEW_REQUIRED` outcomes;
- reason codes and human-readable explanations;
- separation of business logic from input/output handling;
- audit-friendly CSV output.

## Why this design

Operational automation becomes fragile when business rules are buried directly inside browser or spreadsheet code.

This demo keeps the rule configuration separate from the validation engine so changes can be reviewed independently from execution logic.

## Synthetic architecture

```text
sample_input.csv
      ↓
Normalization
      ↓
Rule-set selection by effective date
      ↓
Validation checks
      ↓
Decision + reason codes
      ↓
validation_results.csv
```

## Run

No third-party package is required.

```bash
python validation_engine.py
```

The script reads `sample_input.csv` and `rules.json`, then writes `validation_results.csv` locally. The generated result file is ignored by Git.

## Decision model

`VALID`
: The record has enough information and meets the fictional rule set.

`INVALID`
: The record clearly violates at least one deterministic rule.

`REVIEW_REQUIRED`
: Required information is missing or the engine cannot safely make a deterministic decision.

The last state matters. Missing evidence should not automatically be converted into a negative decision.

## Confidentiality

This is an independent portfolio project. It does not reproduce an employer rule set, internal field names, proprietary thresholds, production data, or source code.
