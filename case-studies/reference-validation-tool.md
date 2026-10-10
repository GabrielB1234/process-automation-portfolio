# Reference Validation Tool

## Problem

A recurring validation task required users to check reference values against historical source files and determine which source version was relevant for a given date.

The first working approach still depended too much on repeatedly opening and scanning files, which became the main performance bottleneck.

## What I built

I helped turn the repeated lookup process into a reusable Python tool and iterated on the data-access design as the use case matured.

The solution included patterns such as:

- reference normalization;
- duplicate removal;
- date parsing and validation;
- version- and date-aware source selection;
- consolidated indexing for repeated lookup;
- caching to avoid reloading unchanged source data;
- structured result output;
- export to Excel;
- a lightweight interface for non-developer users.

## Stack

- Python
- pandas
- Streamlit
- Excel processing
- indexing / caching

## Controls

The tool supported validation and evidence gathering. It did not replace analyst judgment when source information was incomplete or ambiguous.

## Outcome

The redesign reduced repeated file handling and made high-volume reference checks materially faster and more consistent.

## What this demonstrates

The strongest improvement was architectural rather than cosmetic: instead of trying to make repeated file scans slightly faster, the source data was prepared once and queried repeatedly.

The employer reference tables, production data, and company-specific validation rules are not included. A synthetic implementation is represented by the [`process-validation-engine`](../projects/process-validation-engine/README.md) project.
