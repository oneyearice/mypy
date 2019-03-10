#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
from http.server import HTTPServer, CGIHTTPRequestHandler
port = 80
httpd = HTTPServer(('',port), CGIHTTPRequestHandler)
print('Starting simple httpd on port: ' + str(httpd.server_port))
httpd.serve_forever()
