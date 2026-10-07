# HTTP API reference

[Documentation index](README.md)

Base URL: `http://127.0.0.1:8051`. Examples use a fresh `--db api-demo.db` database and run in the stated order. These are demo JSON APIs with no authentication or version prefix. Use `Content-Type: application/json` and a body from 1 to 16,384 bytes for POST requests. `curl` examples use a POSIX shell; on Windows use Git Bash/WSL or adapt JSON quoting for PowerShell.

## Routes

| Method | Path | Successful response |
|---|---|---|
| GET | `/` | HTML interface |
| GET | `/api/portfolio` | Score-sorted array of proposals with assessments and scenarios |
| GET | `/api/events` | Newest 50 event objects |
| POST | `/api/stage` | `{ "saved": true }` |
| POST | `/api/pilot` | Calculated pilot acceptance metrics |

GET routes ignore query strings through URL parsing. POST routes match the exact path; extra query strings are not supported. Unknown routes return HTTP 404. Expected body/key/type/validation failures return HTTP 400 with an `error` string. Unexpected database failures do not have a structured production error contract.

## Read the portfolio

```bash
curl http://127.0.0.1:8051/api/portfolio
```

Each response element contains the complete stored opportunity plus `stage`, `assessment` and `scenarios`. For OP-01, the base assessment reports score `80.0`, net annual capacity value `22080.0`, payback `6.5` and `pilot_eligible: true`. Financial fields are CAD assumptions. See [Data dictionary](data-dictionary.md) for all fields.

## Record stage decisions

Required fields: `id` (existing proposal ID) and `stage` (allowed next stage).

```bash
curl -X POST http://127.0.0.1:8051/api/stage -H 'Content-Type: application/json' -d '{"id":"OP-01","stage":"Scoped"}'
curl -X POST http://127.0.0.1:8051/api/stage -H 'Content-Type: application/json' -d '{"id":"OP-01","stage":"Pilot"}'
```

Each successful decision returns `{"saved": true}` and appends a stage event. Skipping directly from Discovery to Approved produces HTTP 400, typically `{"error":"Invalid stage transition"}`. Missing eligibility conditions produce the relevant blocker messages.

## Record synthetic pilot evidence

```bash
curl -X POST http://127.0.0.1:8051/api/pilot -H 'Content-Type: application/json' -d '{"id":"OP-01","baseline_minutes":10,"assisted_minutes":7,"eligible_users":40,"active_users":28,"satisfaction":4.2,"incidents":0}'
```

Expected JSON response:

```json
{
  "time_reduction_pct": 30.0,
  "adoption_pct": 70.0,
  "satisfaction": 4.2,
  "incidents": 0,
  "review_recommendation": "Ready for owner review"
}
```

This updates the latest aggregate result and appends an event. It is accepted regardless of current stage; acceptance does not itself move the proposal. The values above are synthetic demonstration inputs.

## Review and approve the demonstration

```bash
curl -X POST http://127.0.0.1:8051/api/stage -H 'Content-Type: application/json' -d '{"id":"OP-01","stage":"Review"}'
curl -X POST http://127.0.0.1:8051/api/stage -H 'Content-Type: application/json' -d '{"id":"OP-01","stage":"Approved"}'
curl http://127.0.0.1:8051/api/events
```

The fresh database now has five events: Scoped, Pilot, measurement submission, Review and Approved. The latest state remains a local demo record; no actual sponsor identity/signature exists. Resubmitting the same stage is invalid. There are no request idempotency keys, pilot-result GET route, CRUD routes for opportunities or audit pagination.
