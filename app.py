"""Local demonstration server; not suitable for exposure to the internet."""
import argparse
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import urlsplit
from core import ROOT, connect, seed, portfolio, record_pilot, transition

def make_handler(db_path):
    class Handler(BaseHTTPRequestHandler):
        def send(self, obj, status=200):
            data = json.dumps(obj, allow_nan=False).encode()
            self.send_response(status); self.send_header('Content-Type','application/json'); self.end_headers(); self.wfile.write(data)
        def do_GET(self):
            path = urlsplit(self.path).path
            if path == '/':
                self.send_response(200); self.send_header('Content-Type','text/html; charset=utf-8'); self.end_headers(); self.wfile.write((ROOT/'index.html').read_bytes()); return
            db = connect(db_path)
            try:
                if path == '/api/portfolio': self.send(portfolio(db))
                elif path == '/api/events': self.send([dict(r) for r in db.execute('SELECT * FROM events ORDER BY id DESC LIMIT 50')])
                else: self.send({'error':'Not found'},404)
            finally: db.close()
        def do_POST(self):
            db = connect(db_path)
            try:
                length = int(self.headers.get('Content-Length',0))
                if not 0 < length <= 16384: raise ValueError('Invalid body size')
                data = json.loads(self.rfile.read(length))
                if self.path == '/api/pilot': self.send(record_pilot(db,data['id'],data))
                elif self.path == '/api/stage':
                    transition(db,data['id'],data['stage']); self.send({'saved':True})
                else: self.send({'error':'Not found'},404)
            except (ValueError, KeyError, TypeError) as e: self.send({'error':str(e)},400)
            finally: db.close()
    return Handler

if __name__ == '__main__':
    parser=argparse.ArgumentParser(); parser.add_argument('--port',type=int,default=8051); parser.add_argument('--db',default=str(ROOT/'local.db')); args=parser.parse_args()
    db=connect(args.db); seed(db); db.close()
    print(f'Open http://127.0.0.1:{args.port}',flush=True)
    HTTPServer(('127.0.0.1',args.port),make_handler(args.db)).serve_forever()
