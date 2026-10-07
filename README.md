# AI Opportunity & Pilot Tracker

**From manufacturing business problem to a reviewable AI pilot decision.**

An independent systems-analysis portfolio prototype by Mohammed Adeen Shaik. It assesses six synthetic manufacturing AI opportunities, exposes cost and adoption assumptions, and records pilot evidence and stage decisions in SQLite.


## Why this project matters

AI opportunity selection requires more than a model demo. This project makes the business case, accountable owner, risk gate, test evidence and adoption measures visible together. The application itself is a deterministic decision-support tool; it does not use a model to invent requirements or choose approvals.

## Run locally

Requires Python 3.10+; no package installation or API key.

```bash
python app.py
```

Open http://127.0.0.1:8051. Optional isolated database: `python app.py --port 8051 --db demo.db`.

```bash
python -m unittest discover -s tests -v
python evaluate.py
```

## Demonstrate in five minutes

1. Compare the six ranked opportunities. The document assistant scores 80/100.
2. Inspect low, base and high adoption business cases. Figures are assumptions, not measured savings.
3. Try moving autonomous robot adjustment through Scoped to Pilot. Risk, readiness and missing approvals block it.
4. Move the document assistant from Discovery to Scoped to Pilot.
5. Enter a **simulated** baseline of 10 minutes, assisted time of 7 minutes, 40 eligible users, 28 active users, satisfaction 4.2 and zero critical incidents.
6. Move to Review, then Approved. The audit trail records decisions. Approval here is a demo state, not a real sponsor authorization.

## Features and evidence

- Weighted prioritization: value 35%, feasibility 25%, readiness 20%, inverse risk 20%.
- Independent gates prevent a good score overriding missing data/sponsor approval, low readiness or high risk.
- Annual capacity value, running cost, first-year net value, payback and adoption scenarios.
- Pilot time reduction, usage adoption, satisfaction and critical-incident acceptance.
- Stage validation and append-only application event records.
- 14 automated tests cover financial calculations, invalid inputs, decision gates and pilot acceptance.

The six scenarios produce four pilot-eligible candidates. The document assistant's base assumption yields CAD 22,080 annual net **capacity value**, not cash savings, and 6.5-month modeled payback. See [reproducible results](reports/portfolio-results.json).

## Analyst deliverables

- [Business requirements and traceability](docs/requirements.md)
- [Discovery, business case and process map](docs/business-case.md)
- [Pilot plan and UAT](docs/pilot-and-uat.md)
- [Governance and rollout](docs/governance-and-rollout.md)
- [User guide and interview walkthrough](docs/user-guide.md)
- [Research and role mapping](docs/research-and-role-fit.md)

## Architecture

Browser interface → localhost JSON API → decision functions → SQLite opportunity, pilot and event tables. The initial records are seeded once from `data/opportunities.json`. `evaluate.py` reads fixtures directly and does not modify the application database.

## Boundaries and next work

Local single-user demonstration; no authentication, real approvals, tamper-proof audit storage or multi-facility deployment. Owners and approvals are fictional. Opportunity authoring currently requires editing seed JSON and using a fresh database; the UI only records stage decisions and pilot evidence. Add authenticated sponsor sign-off, editable requirements records, cohort/time-period definitions and benefit validation before enterprise use. The dashboard uses aggregate pilot entries, not controlled experimental observations.

## Resume wording

“Built a Python/SQLite AI opportunity and pilot tracker for six synthetic manufacturing use cases, implementing transparent prioritization, cost-benefit scenarios, risk gates, pilot acceptance metrics and decision audit trails.”

MIT licensed. This is independent portfolio work, not employment experience.
