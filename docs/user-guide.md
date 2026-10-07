# User guide and interview walkthrough

Run `python app.py`; select a proposal and inspect all scenario cards. Value is estimated released capacity, not booked savings. Record measurements only after defining a common pilot period and participant eligibility. Move stages in order; failures explain the missing evidence or gate. A fresh `--db` path resets the scenario without deleting other data.

### Interview narrative

“I treated AI opportunity assessment as a systems-analysis problem. I defined six manufacturing proposals, made financial assumptions visible, separated priority from risk eligibility, and built pilot evidence and stage controls. I would next validate the baseline with operators and compare the assistant against improved document search before asking for rollout.”

Show a blocked robot pilot, then a failed document lookup pilot, then an accepted synthetic pilot. Explain why a technically feasible option with negative first-year value may need a different scope. Do not say stakeholder alignment, production savings or enterprise rollout occurred.

Troubleshooting: choose another `--port` if occupied; use a fresh `--db` after fixture changes; run tests from the repository directory. Stop with Ctrl+C. Never expose this unauthenticated server beyond localhost.
