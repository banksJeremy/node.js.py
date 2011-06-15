#!/usr/bin/env python2.6
import random

try:
    from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
except ImportError:    
    from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    pass

class Server(HTTPServer):
    def __init__(self, address=None, handler=None):
        self.address = address or ("localhost", random.randint(49152, 65535))
        self.host, self.port = self.address
        
        HTTPServer.__init__(self, self.address, handler or Handler)

server = Server()
print server.port
server.serve_forever()
