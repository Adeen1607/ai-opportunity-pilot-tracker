"""Transparent portfolio decisions. All sample costs and benefits are assumptions."""
import json
import math
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent
STAGES = ('Discovery', 'Scoped', 'Pilot', 'Review', 'Approved', 'Paused')
WEIGHTS = {'value': .35, 'feasibility': .25, 'readiness': .20, 'risk': .20}

def validate(item):
    for field in WEIGHTS:
        value = item[field]
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or not 1 <= value <= 5:
            raise ValueError(f'{field} must be a finite number from 1 to 5')
    for field in ('users', 'minutes_saved', 'uses_per_week', 'hourly_cost', 'implementation_cost', 'annual_running_cost'):
        value = item[field]
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value < 0:
            raise ValueError(f'{field} must be finite and non-negative')
    if not 0 <= item['adoption'] <= 1 or not math.isfinite(item['adoption']):
        raise ValueError('adoption must be between 0 and 1')
    if not item.get('owner'):
        raise ValueError('Accountable owner required')

def assess(item, adoption=None):
    validate(item)
    adoption = item['adoption'] if adoption is None else adoption
    if not isinstance(adoption, (int, float)) or not math.isfinite(adoption) or not 0 <= adoption <= 1:
        raise ValueError('adoption must be between 0 and 1')
    components = {k: round((6-item[k] if k == 'risk' else item[k])*w*20, 2) for k, w in WEIGHTS.items()}
    gross = item['users']*item['uses_per_week']*item['minutes_saved']/60*item['hourly_cost']*48*adoption
    net = gross-item['annual_running_cost']
    blockers = []
    if item['risk'] >= 4: blockers.append('Risk review required')
    if not item.get('data_approved'): blockers.append('Data owner approval missing')
    if not item.get('sponsor_approved'): blockers.append('Sponsor approval missing')
    if item['readiness'] < 3: blockers.append('Implementation readiness below threshold')
    return {'score': round(sum(components.values()), 2), 'components': components,
            'gross_annual_capacity_value': round(gross, 2), 'net_annual_capacity_value': round(net, 2),
            'first_year_net_value': round(net-item['implementation_cost'], 2),
            'payback_months': round(item['implementation_cost']/net*12, 1) if net > 0 else None,
            'pilot_eligible': not blockers, 'blockers': blockers,
            'adoption_assumption': adoption}

def connect(path):
    db = sqlite3.connect(path)
    db.row_factory = sqlite3.Row
    db.executescript('''CREATE TABLE IF NOT EXISTS opportunities(id TEXT PRIMARY KEY, payload TEXT NOT NULL, stage TEXT NOT NULL);
    CREATE TABLE IF NOT EXISTS events(id INTEGER PRIMARY KEY, opportunity_id TEXT, kind TEXT, detail TEXT, created_at TEXT DEFAULT CURRENT_TIMESTAMP);
    CREATE TABLE IF NOT EXISTS pilot_results(opportunity_id TEXT PRIMARY KEY, baseline_minutes REAL, assisted_minutes REAL, eligible_users INTEGER, active_users INTEGER, satisfaction REAL, incidents INTEGER);''')
    return db

def seed(db):
    for item in json.loads((ROOT/'data/opportunities.json').read_text()):
        validate(item)
        db.execute('INSERT OR IGNORE INTO opportunities VALUES(?,?,?)', (item['id'], json.dumps(item), 'Discovery'))
    db.commit()

def portfolio(db):
    rows = []
    for row in db.execute('SELECT * FROM opportunities'):
        item = json.loads(row['payload'])
        rows.append({**item, 'stage': row['stage'], 'assessment': assess(item),
                     'scenarios': {name: assess(item, rate) for name, rate in [('low', .3), ('base', item['adoption']), ('high', .85)]}})
    return sorted(rows, key=lambda i: i['assessment']['score'], reverse=True)

def pilot_metrics(row):
    baseline, assisted = row['baseline_minutes'], row['assisted_minutes']
    return {'time_reduction_pct': round((baseline-assisted)/baseline*100, 1),
            'adoption_pct': round(row['active_users']/row['eligible_users']*100, 1),
            'satisfaction': row['satisfaction'], 'incidents': row['incidents'],
            'review_recommendation': 'Ready for owner review' if assisted <= .8*baseline and row['active_users']/row['eligible_users'] >= .6 and row['satisfaction'] >= 4 and row['incidents'] == 0 else 'Improve pilot before rollout'}

def record_pilot(db, identifier, values):
    if not db.execute('SELECT 1 FROM opportunities WHERE id=?', (identifier,)).fetchone(): raise ValueError('Unknown opportunity')
    fields = ['baseline_minutes','assisted_minutes','eligible_users','active_users','satisfaction','incidents']
    if any(isinstance(values[k], bool) or not isinstance(values[k], (int,float)) or not math.isfinite(values[k]) for k in fields): raise ValueError('Finite numeric metrics required')
    if values['baseline_minutes'] <= 0 or values['assisted_minutes'] < 0 or values['eligible_users'] <= 0 or not 0 <= values['active_users'] <= values['eligible_users'] or not 1 <= values['satisfaction'] <= 5 or values['incidents'] < 0: raise ValueError('Invalid pilot metrics')
    if any(int(values[k]) != values[k] for k in ['eligible_users','active_users','incidents']): raise ValueError('Counts must be integers')
    with db:
        db.execute('INSERT OR REPLACE INTO pilot_results VALUES(?,?,?,?,?,?,?)', (identifier, *(values[k] for k in fields)))
        db.execute('INSERT INTO events(opportunity_id,kind,detail) VALUES(?,?,?)', (identifier,'pilot_metrics',json.dumps(values)))
    return pilot_metrics(values)

def transition(db, identifier, target):
    row = db.execute('SELECT * FROM opportunities WHERE id=?', (identifier,)).fetchone()
    if not row: raise ValueError('Unknown opportunity')
    allowed = {'Discovery':['Scoped','Paused'], 'Scoped':['Pilot','Paused'], 'Pilot':['Review','Paused'], 'Review':['Approved','Pilot','Paused'], 'Paused':['Discovery'], 'Approved':['Paused']}
    if target not in allowed[row['stage']]: raise ValueError('Invalid stage transition')
    if target in ['Pilot','Approved']:
        assessment = assess(json.loads(row['payload']))
        if not assessment['pilot_eligible']: raise ValueError('; '.join(assessment['blockers']))
    if target == 'Review' and not db.execute('SELECT 1 FROM pilot_results WHERE opportunity_id=?',(identifier,)).fetchone(): raise ValueError('Pilot evidence required')
    if target == 'Approved':
        pilot = db.execute('SELECT * FROM pilot_results WHERE opportunity_id=?',(identifier,)).fetchone()
        if not pilot or pilot_metrics(pilot)['review_recommendation'] != 'Ready for owner review': raise ValueError('Pilot acceptance criteria not met')
    with db:
        db.execute('UPDATE opportunities SET stage=? WHERE id=?', (target,identifier))
        db.execute('INSERT INTO events(opportunity_id,kind,detail) VALUES(?,?,?)',(identifier,'stage',f"{row['stage']} -> {target}"))
