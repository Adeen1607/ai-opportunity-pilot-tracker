"""Reproduce portfolio decisions without altering the application database."""
import json
from core import ROOT, assess
items=json.loads((ROOT/'data/opportunities.json').read_text())
report={'dataset':'6 synthetic opportunities; no observed savings','formula':'48 working weeks; released capacity valued at assumed hourly cost','opportunities':[{'id':i['id'],'name':i['name'],**assess(i)} for i in items]}
(ROOT/'reports').mkdir(exist_ok=True)
(ROOT/'reports/portfolio-results.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
