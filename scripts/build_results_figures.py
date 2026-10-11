from pathlib import Path
import json
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'reports/figures';OUT.mkdir(parents=True,exist_ok=True)
rows=json.loads((ROOT/'reports/portfolio-results.json').read_text())['opportunities']
fig,ax=plt.subplots(figsize=(10,5));ax.barh([r['name'] for r in rows],[r['score'] for r in rows],color='#2563eb');ax.set(title='Synthetic pilot opportunity scores',xlabel='Weighted scenario score',xlim=(0,100));fig.tight_layout();fig.savefig(OUT/'scenario-scores.png',dpi=160);plt.close(fig)
