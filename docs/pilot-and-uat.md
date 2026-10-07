# Pilot coordination and UAT

[Documentation index](README.md)

## Pilot charter

Four-week proposed pilot in one fictional facility, focused on finding approved documents. Analyst coordinates scope and actions; operations owns acceptance; IT owns access and deployment; quality owns source accuracy; engineering confirms excluded machine-control scope. No participant has actually been recruited.

Week 1: validate baseline, sources, permissions and scenario weights. Week 2: run paired-task tests and resolve defects. Week 3: onboard two representative shifts and collect feedback. Week 4: compare outcomes and prepare sponsor recommendation. Go/no-go requires a named human owner; the prototype's Approved state is only a demonstration.

Targets: at least 20% lookup-time reduction, 60% active/eligible usage, satisfaction at least 4/5 and zero critical incidents. For the app, active users and eligibility refer to one chosen measurement period, specified by the analyst outside the aggregate entry form. Source accuracy and cohort coverage require the companion assistant evaluation and user study; they are not inferred from aggregate tracker values.

| UAT | Action | Expected outcome |
|---|---|---|
| UAT-01 | Inspect all six opportunities | Owner, problem, score and gate visible |
| UAT-02 | Inspect high/low adoption assumptions | Financial changes are transparent |
| UAT-03 | Start high-risk robot pilot | Gate refuses transition |
| UAT-04 | Request review without measurements | Evidence requirement refuses transition |
| UAT-05 | Record assisted time of 9 vs 10 minutes | 10% reduction; rollout acceptance fails |
| UAT-06 | Record 7 vs 10 minutes, 28/40 users, 4.2 satisfaction, zero incidents | Ready for owner review |
| UAT-07 | Inspect event history | Measurements and stages recorded |

## Action and defect tracking (example, not completed stakeholder work)

- A-01 / operations: substantiate lookup volumes and baseline; blocks business-case approval.
- A-02 / quality: approve source list and identify obsolete documents; blocks POC launch.
- A-03 / IT: validate delegated identity/access; blocks enterprise rollout.
- A-04 / analyst: resolve assistant paraphrase failures and rerun evaluation; blocks wider adoption.

## Exit and rollback

Pause on incorrect source release, access leakage or unsafe operational advice. Return to approved manual document search, preserve permitted incident metadata and notify the accountable owner. Resume only after documented root cause, fix verification and sponsor decision.
