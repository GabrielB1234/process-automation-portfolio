# Publication Safety Checklist

This repository is designed to be reviewed before any change in visibility or before sharing a link externally.

## Content checks

Before publication, verify that no tracked file contains:

- employer names when they are not necessary to explain the work;
- internal application names, URLs, hostnames, queue names, project codenames, or environment names;
- customer, partner, employee, vendor, account, order, invoice, claim, opportunity, case, or transaction identifiers;
- real production data, screenshots, logs, spreadsheets, email exports, or documents;
- credentials, tokens, passwords, cookies, certificates, API keys, connection strings, or private keys;
- proprietary selectors copied from production browser automation;
- internal policy text or proprietary decision rules;
- exact operational volumes, internal staffing data, or precise productivity baselines unless explicitly cleared for external use;
- source code copied from an employer-owned implementation.

## Metric checks

Professional impact should be described conservatively.

Prefer:

- qualitative impact;
- rounded ranges or broad scale descriptions where a metric materially improves the case study;
- explicit labels such as `estimated` when the value is not directly measured.

Avoid publishing:

- exact internal baselines;
- exact monthly production volumes;
- calculations that reveal staffing or internal capacity assumptions;
- combinations of numbers that allow an internal process to be reconstructed.

## Code checks

Public technical demos should use:

- independently written code;
- fictional names and identifiers;
- synthetic datasets;
- local mock applications or public demo endpoints;
- generic workflow states;
- explicit error handling and safe defaults.

Never copy production code and attempt to make it safe only by changing names or URLs.

## Git-history checks

Review the full repository history, not only the latest files.

Before changing visibility to public:

1. enumerate all branches;
2. inspect the commit list;
3. confirm there are no old commits containing sensitive material;
4. check pull requests and issue content;
5. inspect tracked file names and the complete tree;
6. search for known internal terms, domains, identifiers, email addresses, and secret patterns;
7. confirm the repository is still private until the review is complete.

If sensitive material has ever been committed, prefer rebuilding a clean repository rather than relying only on a later deletion.
