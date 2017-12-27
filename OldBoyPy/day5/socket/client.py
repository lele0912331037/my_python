#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import socket
import sys

client = socket.socket()
client.connect(('127.0.0.1', 8080))

num = 0
while True:
    num += 1
    #data = client.recv(1024)
    #data = data.decode()
    #print(data)
    inp = input('请输入：')
    #inp = str(num)
    client.send(inp.encode())
    send_data = "hello server, this is  %s time " % num
    client.send(send_data.encode())
    data = client.recv(1024)
    ata = data.decode()
    print(data)

