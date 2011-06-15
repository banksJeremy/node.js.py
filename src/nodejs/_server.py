#!/usr/bin/env python2.6
import random
import json

try:
    from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
except ImportError:    
    from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            data = json.load(rfile)
            
            result = {
                "result": data
            }
        except Exception as e:
            result = {
                "error": type(e).__name__,
                "message": str(e)
            }
        
        self.send_response(200)
        self.end_headers()
        json.dump(result, wfile)

class Server(HTTPServer):
    def __init__(self, address=None, handler=None):
        self.address = address or ("localhost", random.randint(49152, 65535))
        self.host, self.port = self.address
        
        HTTPServer.__init__(self, self.address, handler or Handler)

