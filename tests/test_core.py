import json
import tempfile
import unittest
from core import ROOT, assess, connect, seed, transition, record_pilot, portfolio

class PortfolioTests(unittest.TestCase):
    def setUp(self):
        self.directory=tempfile.TemporaryDirectory(); self.db=connect(self.directory.name+'/test.db'); seed(self.db)
        self.item=json.loads((ROOT/'data/opportunities.json').read_text())[0]
    def tearDown(self): self.db.close(); self.directory.cleanup()
    def test_financial_model(self):
        a=assess(self.item)
        self.assertAlmostEqual(a['gross_annual_capacity_value'],26880)
        self.assertAlmostEqual(a['net_annual_capacity_value'],22080)
        self.assertAlmostEqual(a['first_year_net_value'],10080)
        self.assertEqual(a['payback_months'],6.5)
    def test_zero_adoption_has_no_payback(self): self.assertIsNone(assess(self.item,0)['payback_months'])
    def test_invalid_scores_and_costs_rejected(self):
        for field,value in [('risk',6),('value',float('nan')),('users',-1),('implementation_cost',float('inf'))]:
            with self.assertRaises(ValueError): assess({**self.item,field:value})
    def test_high_value_cannot_override_safety_gate(self):
        transition(self.db,'OP-03','Scoped')
        with self.assertRaises(ValueError): transition(self.db,'OP-03','Pilot')
    def test_missing_data_approval_blocks_pilot(self):
        transition(self.db,'OP-05','Scoped')
        with self.assertRaises(ValueError): transition(self.db,'OP-05','Pilot')
    def test_no_skipping_stages(self):
        with self.assertRaises(ValueError): transition(self.db,'OP-01','Approved')
    def test_requires_pilot_evidence(self):
        transition(self.db,'OP-01','Scoped'); transition(self.db,'OP-01','Pilot')
        with self.assertRaises(ValueError): transition(self.db,'OP-01','Review')
    def test_failed_pilot_cannot_be_approved(self):
        transition(self.db,'OP-01','Scoped'); transition(self.db,'OP-01','Pilot')
        record_pilot(self.db,'OP-01',dict(baseline_minutes=10,assisted_minutes=9,eligible_users=40,active_users=28,satisfaction=4.2,incidents=0))
        transition(self.db,'OP-01','Review')
        with self.assertRaises(ValueError): transition(self.db,'OP-01','Approved')
    def test_successful_pilot_and_audit(self):
        transition(self.db,'OP-01','Scoped'); transition(self.db,'OP-01','Pilot')
        result=record_pilot(self.db,'OP-01',dict(baseline_minutes=10,assisted_minutes=7,eligible_users=40,active_users=28,satisfaction=4.2,incidents=0))
        self.assertEqual(result['time_reduction_pct'],30)
        transition(self.db,'OP-01','Review'); transition(self.db,'OP-01','Approved')
        self.assertEqual(self.db.execute('SELECT COUNT(*) FROM events').fetchone()[0],5)
    def test_invalid_counts(self):
        with self.assertRaises(ValueError): record_pilot(self.db,'OP-01',dict(baseline_minutes=10,assisted_minutes=7,eligible_users=40,active_users=41,satisfaction=4.2,incidents=0))
    def test_rank_and_seed_idempotent(self):
        seed(self.db); rows=portfolio(self.db)
        self.assertEqual(len(rows),6)
        self.assertEqual(rows[0]['id'],'OP-01')

if __name__=='__main__': unittest.main()
