# AI Opportunity & Pilot Tracker

**A reviewable path from manufacturing AI proposal to pilot decision.**

[![Verify prototype](https://github.com/Adeen1607/ai-opportunity-pilot-tracker/actions/workflows/checks.yml/badge.svg)](https://github.com/Adeen1607/ai-opportunity-pilot-tracker/actions/workflows/checks.yml)

This Python/SQLite prototype brings opportunity assessment, benefit assumptions, eligibility gates and pilot evidence into one local interface. Six fictional manufacturing proposals show how an analyst can recommend a scoped pilot while keeping ownership and risk visible.

## Quick start

Requires Python 3.10+. No packages or API key are needed.

```bash
git clone https://github.com/Adeen1607/ai-opportunity-pilot-tracker.git
cd ai-opportunity-pilot-tracker
python app.py
```

Open http://127.0.0.1:8051. See [Getting started](docs/getting-started.md) for Windows/macOS/Linux invocation options and isolated databases.

## What the application does

| Capability | Evidence in the prototype |
|---|---|
| Opportunity assessment | Weighted value, feasibility, readiness and inverse-risk score |
| Business case | Low/base/high adoption scenarios; cost and payback assumptions |
| Pilot eligibility | Independent risk, readiness and simulated approval gates |
| Pilot acceptance | Time reduction, active/eligible usage, satisfaction and incidents |
| Decision tracking | Stage transition validation and recorded measurement/decision events |

This application uses deterministic rules; it does not ask a model to approve proposals. Opportunity records are seeded from JSON. The UI records pilot measurements and stage changes; it does not edit proposal definitions or approvals.

## Baseline evidence

Four of the six synthetic proposals are eligible for pilot review. The document assistant scores 80/100. Under its base assumptions, the model estimates CAD 22,080 annual net capacity value and 6.5-month payback. These figures value released staff time; they are not measured cash savings.

**14 automated tests pass**, covering decision rules and real localhost HTTP workflows. [Portfolio results](reports/portfolio-results.json) are reproducible:

```bash
python -m unittest discover -s tests -v
python evaluate.py
```

## Documentation

Start with the [Documentation index](docs/README.md), or choose a route:

- **Run and demonstrate:** [Setup](docs/getting-started.md), [User guide](docs/user-guide.md), [Troubleshooting](docs/troubleshooting.md).
- **Understand the implementation:** [Architecture](docs/architecture.md), [Data dictionary](docs/data-dictionary.md), [API reference](docs/api-reference.md), [Decision rules](docs/decision-model.md).
- **Review the analyst work:** [Requirements](docs/requirements.md), [Business case](docs/business-case.md), [Pilot/UAT](docs/pilot-and-uat.md), [Governance and rollout](docs/governance-and-rollout.md).
- **Assess evidence:** [Testing and evaluation](docs/testing-and-evaluation.md), [Build validation](reports/validation.md), [Research and role fit](docs/research-and-role-fit.md).

## Scope and next steps

Independent portfolio work by Mohammed Adeen Shaik, using synthetic data and simulated stakeholders. There is no Linamar affiliation, real sponsor approval or production deployment. Local approval flags and stage labels are demonstration records. SQLite audit events are not tamper-proof, and changing pilot measurements does not automatically invalidate an already-approved stage.

Before enterprise adoption, validate task volumes and assumptions, add authenticated approvals and evidence freshness, and compare AI use cases against simpler alternatives. See [Security](SECURITY.md), [Contributing](CONTRIBUTING.md) and the [MIT license](LICENSE).
