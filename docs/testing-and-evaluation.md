# Testing and evaluation

[Documentation index](README.md)

## Verification layers

| Layer | Coverage | What it does not prove |
|---|---|---|
| 11 core tests | Financial examples, invalid scores/counts, eligibility, stage order, evidence and audit behavior | Real benefits or approval authority |
| 3 HTTP tests | HTML response, full pilot workflow, rejected decision and unknown route | Browser layout or multi-user performance |
| Portfolio evaluation | Recalculates six fixture assessments into JSON | Empirical business outcomes |
| Manual UAT plan | Proposed reviewer steps and expected results | Completed independent user acceptance |

Run both commands from the repository root:

```bash
python -m unittest discover -s tests -v
python evaluate.py
```

The baseline contains 14 passing automated tests. Core and HTTP tests use temporary databases. The HTTP suite binds an ephemeral localhost port; it does not require the normal app server to run. `evaluate.py` reads source JSON and writes `reports/portfolio-results.json` without changing application data.

## Expected evaluation interpretation

The report retains the six fixture opportunities, scores, capacity assumptions, payback and gate blockers. Four proposals are pilot-eligible, but eligibility is not a funding recommendation. The document assistant's modeled net annual capacity value is CAD 22,080; no released time or cash benefit was observed in a facility.

CI runs unittest and the evaluator, then uploads JSON reports. A successful workflow confirms those commands completed. The evaluator is a reporting script, not a statistical validation study.

## Documentation verification

API examples should be exercised in order against a new database. Validate that all relative Markdown links resolve, code fences are paired and response fields match the implementation. The baseline checked embedded JavaScript syntax; browser visual interaction was not verified because a browser binary was unavailable. A real browser walkthrough remains necessary for full interface QA.

## Regression expectations

If changing weights or financial assumptions, independently calculate at least one reference business case and inspect zero/negative net value. If changing gates, test a high-priority blocked proposal. If changing stages, test rejected skipping, failed acceptance and event persistence. Avoid changing fixtures merely to make the score appear favorable.

Refer to [Pilot/UAT](pilot-and-uat.md) for proposed participant measurement and acceptance decisions.
