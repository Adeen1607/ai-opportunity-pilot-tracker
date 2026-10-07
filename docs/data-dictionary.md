# Data dictionary and persistence

[Documentation index](README.md)

## Opportunity payload

The initial source is `data/opportunities.json`. Each object is stored as JSON in SQLite.

| Field | Meaning / intended shape |
|---|---|
| `id` | Stable proposal ID, for example `OP-01` |
| `name`, `department` | Display name and originating function |
| `owner` | Non-empty accountable-owner label; a simulated persona in fixtures |
| `problem`, `baseline`, `success` | Business problem, comparison process and acceptance description |
| `value`, `feasibility`, `readiness`, `risk` | Finite numbers from 1 to 5 |
| `data_approved`, `sponsor_approved` | Intended Boolean approval flags; current logic checks truthiness |
| `users` | Assumed users benefiting from the opportunity |
| `minutes_saved`, `uses_per_week` | Assumed time released per use and frequency |
| `hourly_cost` | Assumed CAD hourly capacity value |
| `adoption` | Fraction between 0 and 1 |
| `implementation_cost` | Assumed one-time CAD cost |
| `annual_running_cost` | Assumed annual CAD operating cost |

Numeric financial/volume values are validated as finite and non-negative; unlike pilot counts, proposal volume values do not require integers. Display fields and approval types do not have complete schema validation. Keep fixtures consistent with the intended shapes above.

## SQLite tables

| Table | Columns | Purpose |
|---|---|---|
| `opportunities` | `id TEXT PRIMARY KEY`, `payload TEXT NOT NULL`, `stage TEXT NOT NULL` | Stored proposal definition and current workflow stage |
| `pilot_results` | `opportunity_id TEXT PRIMARY KEY`, `baseline_minutes REAL`, `assisted_minutes REAL`, `eligible_users INTEGER`, `active_users INTEGER`, `satisfaction REAL`, `incidents INTEGER` | Latest aggregate pilot measurement per opportunity |
| `events` | `id INTEGER PRIMARY KEY`, `opportunity_id TEXT`, `kind TEXT`, `detail TEXT`, `created_at TEXT DEFAULT CURRENT_TIMESTAMP` | Application measurement/stage history |

These logical relationships are checked by application code where relevant; the tracker schema does not declare foreign-key constraints. Event timestamps use SQLite's default UTC timestamp format. Pilot events contain the submitted JSON payload; stage events contain a `previous -> next` string. GET events returns the most recent 50 records in descending ID order; there is no pagination or complete-history export endpoint.

## Derived portfolio fields

The API adds `stage`, `assessment` and `scenarios` to each proposal. Assessment includes `score`, weighted `components`, gross/net capacity values, first-year value, nullable payback, eligibility/blockers and adoption assumption. The three scenarios have the same assessment shape with different adoption values.

## Change and retention behavior

Startup inserts missing proposal IDs but never updates existing payloads. To demonstrate revised seed data reliably, stop the app and start with a new database. The current UI does not create/delete proposals or edit approvals. The evaluator reads JSON directly, so it reflects source edits immediately.

Pilot submissions replace the latest aggregate result but preserve prior submitted values as events. There is no retention scheduler, encryption, protected audit store or backup service. With the app stopped, copying the database file creates a simple local backup. Never commit real records or local databases.
