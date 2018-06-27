import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler

webdir = '.'
port = 88

os.chdir(webdir)
srvaddr = ("", port)
srvobj = HTTPServer(srvaddr, CGIHTTPRequestHandler)
srvobj.serve_forever()