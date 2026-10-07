# AI Opportunity & Pilot Tracker: documentation

[Project overview](../README.md)

This index separates running the prototype, understanding its contracts, and assessing the analyst evidence. All business scenarios and stakeholder personas are synthetic. Proposed deployment capabilities are explicitly identified; a written plan is not a completed rollout.

## Guides

| Document | Purpose |
|---|---|
| [Getting started](getting-started.md) | Clone, run and select an isolated database |
| [User guide](user-guide.md) | Demonstrate the UI and explain decisions |
| [Architecture](architecture.md) | Components, transactions and runtime boundaries |
| [Data dictionary](data-dictionary.md) | Fixtures, SQLite schema and retention |
| [API reference](api-reference.md) | Requests, responses and a complete walkthrough |
| [Decision model](decision-model.md) | Weights, benefit formulas, gates and transitions |
| [Requirements](requirements.md) | Business scope and requirement traceability |
| [Business case](business-case.md) | Baseline process, alternatives and assumed benefits |
| [Pilot and UAT](pilot-and-uat.md) | Proposed coordination and acceptance workflow |
| [Governance and rollout](governance-and-rollout.md) | Owners, risk controls and staged adoption |
| [Testing and evaluation](testing-and-evaluation.md) | Verified evidence and what it cannot establish |
| [Troubleshooting](troubleshooting.md) | Expected refusals and operational problems |
| [Research and role fit](research-and-role-fit.md) | Role coverage and design references |

## Suggested reading paths

**First-time user:** getting started → user guide → troubleshooting.

**Technical reviewer:** architecture → data dictionary → API reference → algorithm/decision guide → testing.

**Systems-analysis reviewer:** requirements → business case or evaluation decision → governance → pilot/adoption plan.

## Project maintenance

- [Contributing](../CONTRIBUTING.md): local workflow and relevant verification.
- [Security](../SECURITY.md): local-use boundaries and safe issue reporting.
- [Changelog](../CHANGELOG.md): initial prototype and documentation update.
- [License](../LICENSE): MIT terms.
- [Build validation](../reports/validation.md): original verification scope and unverified paths.

Documentation describes the current implementation. Read baseline reports alongside CI results; an automated run does not establish real user adoption, operational safety or financial benefit.
