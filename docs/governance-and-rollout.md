# Governance, rollout and ownership

Borrowed NIST functions guide this small prototype; no compliance claim is made.

| Function | Decision evidence | Accountable persona |
|---|---|---|
| Govern | Scope, stage approvals, incident ownership | Operations sponsor |
| Map | Process, baseline, intended users, alternatives | Analyst with operations |
| Measure | Tests, pilot time, adoption and satisfaction | Analyst and quality |
| Manage | Pause gates, remediation and rollback | Sponsor and IT |

| Risk | Impact | Current prototype control | Residual gap |
|---|---|---|---|
| Overstated savings | Poor investment decision | Explicit capacity assumptions and scenarios | No validated actual volumes |
| High-risk use case approved by score | Unsafe pilot | Separate eligibility gates | Approval flags are fixtures |
| Weak adoption masks technical success | Failed rollout | Active/eligible users and satisfaction | No shift-level cohort capture |
| Incorrect pilot entries | Misleading acceptance | Range and integer-count checks | No source-observation audit |
| Unauthorized stage change | False approval | Localhost binding only | No authentication/authorization |
| Altered audit records | Lost accountability | App inserts decision events | SQLite can be edited outside app |

Rollout sequence: source/identity review → task evaluation → small representative pilot → sponsor review → staged facility expansion. Do not interpret the UI's approval as business sign-off. Train users to inspect assumptions, record the measurement period and report failures. Owners review benefits monthly, source accuracy weekly during pilot and critical incidents immediately. In an enterprise version, use authenticated approval roles, protected audit retention and controlled release management.
