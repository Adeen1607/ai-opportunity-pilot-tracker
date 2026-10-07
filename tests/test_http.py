import json
import tempfile
import threading
import unittest
import urllib.request
import urllib.error
from http.server import HTTPServer
from app import make_handler
from core import connect

class HttpTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(); path=self.temp.name+'/api.db'
        db=connect(path)
        from core import seed
        seed(db)
        db.close()
        self.server=HTTPServer(('127.0.0.1',0),make_handler(path)); self.thread=threading.Thread(target=self.server.serve_forever,daemon=True); self.thread.start()
        self.url='http://127.0.0.1:'+str(self.server.server_port)
    def tearDown(self):
        self.server.shutdown(); self.server.server_close(); self.thread.join(); self.temp.cleanup()
    def request(self,path,data=None):
        request=urllib.request.Request(self.url+path,data=json.dumps(data).encode() if data is not None else None,headers={'Content-Type':'application/json'})
        with urllib.request.urlopen(request,timeout=5) as response: return json.load(response)
    def test_html_served(self):
        with urllib.request.urlopen(self.url) as response:
            self.assertIn(b'<title>',response.read()); self.assertIn('text/html',response.headers['Content-Type'])
    def test_unknown_route(self):
        with self.assertRaises(urllib.error.HTTPError) as context: self.request('/unknown')
        self.assertEqual(context.exception.code,404)
    def test_api_pilot_flow_and_rejection(self):
        self.assertEqual(len(self.request('/api/portfolio')),6)
        self.request('/api/stage',{'id':'OP-01','stage':'Scoped'})
        self.request('/api/stage',{'id':'OP-01','stage':'Pilot'})
        metrics=self.request('/api/pilot',dict(id='OP-01',baseline_minutes=10,assisted_minutes=7,eligible_users=40,active_users=28,satisfaction=4.2,incidents=0))
        self.assertEqual(metrics['adoption_pct'],70)
        self.request('/api/stage',{'id':'OP-01','stage':'Review'})
        self.request('/api/stage',{'id':'OP-01','stage':'Approved'})
        self.assertEqual(len(self.request('/api/events')),5)
        with self.assertRaises(urllib.error.HTTPError) as context: self.request('/api/stage',{'id':'OP-03','stage':'Approved'})
        self.assertEqual(context.exception.code,400)
