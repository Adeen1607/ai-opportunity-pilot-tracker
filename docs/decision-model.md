# Decision and financial model

[Documentation index](README.md)

## Priority score

Each dimension accepts a finite numeric score from 1 to 5. The model treats higher value, feasibility and readiness as better; higher risk is worse.

| Dimension | Weight | Contribution |
|---|---|---|
| Business value | 35% | `value × 0.35 × 20` |
| Feasibility | 25% | `feasibility × 0.25 × 20` |
| Implementation readiness | 20% | `readiness × 0.20 × 20` |
| Inverse risk | 20% | `(6 − risk) × 0.20 × 20` |

Contributions are rounded to two decimal places before summation. The resulting score ranges from 20 to 100, not 0 to 100. Scoring is an assumed prioritization rubric, not an ML prediction or calibrated business valuation. `portfolio` sorts descending by score; no additional strategic tie-breaker is implemented.

## Eligibility gates

A proposal is eligible only when all these conditions hold: risk below 4, readiness at least 3, truthy data-owner approval and truthy sponsor approval. Missing conditions are returned in `blockers`. Approval values are fixture metadata, not signed decisions. A higher priority score cannot remove a blocker.

## Capacity-value model

```text
gross annual capacity value = users × uses/week × minutes saved/60
                              × hourly cost × 48 weeks × adoption
net annual capacity value = gross annual capacity value − annual running cost
first-year net value = net annual capacity value − implementation cost
payback months = implementation cost / net annual capacity value × 12
```

Payback is `null` when net annual capacity value is zero or negative. Adoption must lie between 0 and 1. Financial/volume inputs must be finite and non-negative. The scenario cards use 30% adoption, the proposal's configured adoption, and 85% adoption. Those are assumptions, not statistical intervals; a configured base adoption outside 30–85% can make the scenario names misleading.

For OP-01, 40 users × 8 uses/week × 5/60 hours × CAD 35/hour × 48 weeks × 0.60 = CAD 26,880 gross value. Subtract CAD 4,800 running cost for CAD 22,080 net annual capacity value. First-year net value is CAD 10,080 after CAD 12,000 implementation cost. Simple payback is 6.5 months. See [Business case](business-case.md) for interpretation and alternatives.

## Pilot acceptance

Time reduction is `(baseline − assisted)/baseline × 100`. Adoption is `active/eligible × 100`. Acceptance requires assisted time no more than 80% of baseline, active/eligible at least 60%, satisfaction at least 4/5 and zero critical incidents. Counts must be integers, baseline and eligible users must be positive, assisted time cannot be negative, and active users cannot exceed eligible users.

Calculations use unrounded values for acceptance; display values are rounded to one decimal place. Passing these aggregate conditions returns `Ready for owner review`, not an independent rollout authorization.

## State transitions

| Current stage | Allowed next stages | Additional check |
|---|---|---|
| Discovery | Scoped, Paused | No additional evidence gate |
| Scoped | Pilot, Paused | Pilot requires eligibility |
| Pilot | Review, Paused | Review requires a stored pilot result |
| Review | Approved, Pilot, Paused | Approved requires eligibility and passing acceptance; Pilot rechecks eligibility |
| Approved | Paused | No automatic revalidation on later metric edits |
| Paused | Discovery | Stored measurements remain; this is not a data reset |

A failed pilot can enter Review because that stage examines outcomes. It cannot enter Approved. Pause/restart retains prior evidence; a real workflow must associate measurements with a defined pilot iteration and approval version.
