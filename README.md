# Process Automation Portfolio

A portfolio focused on reliable business-process automation, process engineering, operational controls, and AI-assisted development.

The purpose of this repository is to show how I approach automation problems without publishing employer-owned code, production data, internal system details, confidential business rules, or customer information.

## What this portfolio demonstrates

- Python automation
- Browser automation with Selenium
- Excel / VBA workflow automation
- Batch processing and failure recovery
- Rule-based validation
- Reconciliation and operational controls
- Process redesign and continuous improvement
- Human-in-the-loop automation
- AI-assisted development with human review

## How the portfolio is structured

### Professional case studies

The `case-studies/` folder contains generalized descriptions of automation and process-improvement work completed in enterprise operations environments.

These case studies focus on the transferable problem-solving approach: the problem, the automation pattern, controls, reliability, and outcome. They intentionally omit employer names, internal application names, production identifiers, customer or partner information, source code, and proprietary rules.

### Synthetic technical projects

The `projects/` folder contains independently written demonstrations using fictional workflows and synthetic data.

These projects are not copies of production implementations. They exist to demonstrate technical patterns such as batch execution, retries, checkpoints, validation, logging, rule separation, and exception handling.

## Engineering approach

I generally use this sequence:

**Problem → Process → Rules → Data → Automation → Controls → Result**

A few principles guide the work:

- automate deterministic repetition before adding unnecessary complexity;
- keep business judgment with people when accountability matters;
- validate outcomes, not only successful clicks;
- design batch processes so one failed item does not destroy the full run;
- separate rules from execution when requirements change frequently;
- log failures in a way that supports investigation and recovery;
- use AI to accelerate development where useful, while keeping testing, validation, and accountability explicit.

## Case studies

- [Template & Data Preparation Automation](case-studies/template-data-preparation.md)
- [Cross-Application Communication Workflow](case-studies/cross-application-communication.md)
- [Invoice Request Artifact Workflow](case-studies/invoice-request-artifact-workflow.md)
- [High-Volume Browser Workflow Automation](case-studies/high-volume-browser-workflow.md)
- [Reference Validation Tool](case-studies/reference-validation-tool.md)
- [Approval Control Redesign](case-studies/approval-control-redesign.md)
- [Controlled Record Reassignment](case-studies/controlled-record-reassignment.md)
- [Excel / VBA Operations Suite](case-studies/excel-vba-operations-suite.md)

## Technical demos

- [Batch Workflow Automation](projects/batch-workflow-automation/README.md)
- [Process Validation Engine](projects/process-validation-engine/README.md)

## Confidentiality

Everything in this repository is intended to be safe for public review.

The repository must never contain:

- employer-owned source code;
- production screenshots;
- internal URLs, hostnames, or application identifiers;
- credentials, tokens, cookies, certificates, or connection strings;
- customer, partner, employee, account, transaction, order, invoice, claim, or case identifiers from real systems;
- confidential policy documents or proprietary business rules;
- production exports, logs, spreadsheets, emails, or financial records.

When a public example is inspired by a professional problem, the implementation is recreated independently with synthetic data and generic terminology.

## Status

This repository is intentionally curated. I prefer a smaller number of clear, defensible examples over a large collection of unfinished or overly detailed artifacts.
