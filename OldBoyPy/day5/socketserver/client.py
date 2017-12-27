#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import socket

ip_port = ('127.0.0.1', 10008)
while True:
    sk = socket.socket()
    sk.connect(ip_port)
    inp = input('Data:')
    sk.sendall(inp.encode())
    sk.close()
