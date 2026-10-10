# Invoice Request Artifact Workflow

## Status

Historical prototype / partial implementation.

This project is included to demonstrate workflow design and cross-application automation. It is not presented as a fully deployed production solution.

## Problem

A request workflow required the same structured information to be prepared in multiple artifacts, including an email and a supporting document.

Maintaining both manually duplicated work and increased the chance of inconsistencies between the communication and the supporting record.

## What I designed

The workflow was designed around a single structured source so multiple outputs could be generated consistently.

The prototype covered:

- reading request information from Excel;
- generating the email structure automatically;
- populating subject, body, recipients, and request details from the same source;
- generating a corresponding supporting document;
- keeping both artifacts aligned by deriving them from one dataset.

## Stack

- Microsoft Excel
- VBA / Macros
- Microsoft Outlook automation
- document / PDF generation

## Controls

The intended flow kept final review with the user. The automation prepared artifacts; it did not make approval or payment decisions.

## What this demonstrates

Not every useful engineering effort reaches production. I include this project because it shows the shift from isolated spreadsheet macros toward workflow-oriented design: one source of truth, coordinated outputs, and explicit attention to consistency between artifacts.

No real request data, recipients, internal templates, production documents, employer code, or proprietary workflow rules are included here.
