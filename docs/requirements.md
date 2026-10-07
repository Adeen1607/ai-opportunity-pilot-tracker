# Business requirements and traceability

[Documentation index](README.md)

## Scenario and scope

A fictional manufacturer receives AI proposals through scattered emails. The analyst needs a consistent assessment and a defensible pilot recommendation. The prototype covers assessment and pilot evidence. It excludes autonomous equipment control, employee assessment, real procurement and production releases.

Simulated stakeholders: operations sponsor (value), engineering (feasibility), IT/data owner (access), quality (risk), supervisor (adoption), analyst (requirements and coordination). These are design personas, not interviewed people.

| ID | Requirement and acceptance criterion | Implemented evidence | Verification |
|---|---|---|---|
| BR-01 | Every proposal shows problem, owner, department, baseline and success measure | Seed records; portfolio detail | Seed validation and manual review |
| FR-01 | Rank on four dimensions, each scored 1–5, with visible weights | `assess`, dashboard | Rank and invalid-score tests |
| FR-02 | Separate pilot eligibility from priority score | Independent blockers | High-risk and approval tests |
| FR-03 | Show annual net capacity, implementation cost, first-year value and payback | `assess`, scenario cards | Financial and zero-adoption tests |
| FR-04 | Require stage order and pilot evidence before review | `transition` | No-skipping and evidence tests |
| FR-05 | Refuse approval when pilot acceptance fails | `pilot_metrics`, `transition` | Failed and successful pilot tests |
| FR-06 | Record stage changes and pilot measurements | SQLite events | Audit test |
| NFR-01 | Work without cloud credentials | Standard library local runtime | Fresh local launch |
| NFR-02 | Reject invalid/nonfinite inputs | Numeric validation | Negative, NaN and infinite tests |
| NFR-03 | Clearly label synthetic evidence and assumptions | UI and documentation | Manual review |

## Open discovery questions

What task volume and lookup baseline can users substantiate? Who owns each source? Can released time be redeployed to measurable work? What data contains personal or supplier-confidential information? Which shifts face adoption barriers? What is the simplest non-AI alternative? Which risk severity prevents a pilot regardless of financial upside?

## Deliberate gaps

No actual facilitation session, signed business case, independent UAT, identity-based approvals or production outcomes exist. The prototype makes these requirements reviewable; a real analyst must validate them with stakeholders.
