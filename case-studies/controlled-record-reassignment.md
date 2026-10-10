# Controlled Record Reassignment

## Problem

A recurring workflow required many records to be reassigned according to a distribution plan prepared by the team.

The repetitive browser execution was a good automation candidate, but the assignment decision itself needed to remain with the operator.

## What I built

I translated the manual sequence into a controlled browser automation that executed a user-defined plan and verified the resulting state.

The workflow included:

- structured input of record references;
- configurable source-column selection;
- cleaning of blank or invalid input;
- user-defined distribution across assignees;
- sequential browser execution;
- validation that the intended assignee was selected before submission;
- post-action confirmation that ownership actually changed;
- audit logging for successful, failed, and skipped items;
- safe-stop and manual-investigation options for validation failures.

## Stack

- Python
- Selenium
- Excel / structured input
- CSV audit logging

## Governance design

The automation deliberately did not decide who should receive a record.

The operator remained responsible for the assignment plan. The tool executed and validated that plan.

## Outcome

The solution reduced repetitive navigation while preserving business ownership of the decision and improving post-action verification.

## What this demonstrates

A successful click is not the same as a successful outcome. The automation validates the expected state after execution instead of assuming that submission equals success.

No real user identities, record IDs, internal URLs, production selectors, or employer code are included here.
