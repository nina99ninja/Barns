#!/usr/bin/env python3
import http.server
import socketserver
import os

PORT = 3000
PUBLIC = os.path.join(os.path.dirname(__file__), 'public')

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=PUBLIC, **kwargs)

    def log_message(self, format, *args):
        pass  # quiet

print(f"BARNS menu running at http://localhost:{PORT}")
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
