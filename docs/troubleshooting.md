# Troubleshooting

[Documentation index](README.md)

| Symptom | Likely explanation | Resolution |
|---|---|---|
| `python` is not found | Python command differs by platform | Use `python3` or Windows `py -3`; verify Python 3.10+ |
| `ModuleNotFoundError: core` during tests | Tests launched from outside the repository | Change to the directory containing `core.py` and run unittest there |
| Address already in use | Port 8051 is occupied | Start with `--port 8061`, then open that port |
| Unable to open database file | Parent path missing or not writable | Use an existing writable directory or `--db walkthrough.db` |
| Fixture edits do not appear in the UI | Existing IDs were seeded earlier | Stop the app and select a new `--db` filename |
| Stage change is refused | Invalid next stage or unmet gate | Inspect the transition table, blockers and pilot evidence |
| Review allowed but approval refused | A stored pilot exists but acceptance fails | Inspect time, usage, satisfaction and incident measures |
| Scores and eligibility disagree | They answer different questions | Priority score never overrides a gate |
| Payback is `null` | Net annual capacity value is not positive | Review costs/adoption; do not display this as zero-month payback |
| Old results remain after pause/restart | Workflow restart retains evidence | Use a new database for a completely fresh demo |
| Approved stage remains after worse metrics | No automatic approval invalidation exists | Pause manually for the demonstration; implement versioned evidence before real use |

For a clean reproduction, start the app with a unique database and rerun the documented API sequence. Capture the synthetic inputs, stage before/after and error message. Never include a real company database in an issue.

A portfolio evaluator report can differ from the running UI after fixture edits: evaluation reads source JSON, whereas the UI reads the database's previously seeded payloads. Stop the app and use a fresh database to compare the same version.
