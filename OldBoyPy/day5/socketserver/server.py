#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import socketserver


class MyServer(socketserver.BaseRequestHandler):
    def setup(self):
        print('1111')

    def handle(self):
        pass

    def finish(self):
        pass

if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 10008), MyServer)
    server.serve_forever()
