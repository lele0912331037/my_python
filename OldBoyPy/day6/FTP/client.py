#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import socket
import sys
import os

ip_port = ('127.0.0.1', 10086)
sk = socket.socket()
sk.connect(ip_port)

container = {'key': '', 'data': ''}
while True:
    inputs = input('path:')
    cmd, path = inputs.split('|')
    file_name = os.path.basename(path)
    file_size = os.stat(path).st_size
    sk.send(bytes(cmd + "|" + file_name + '|' + str(file_size), encoding='utf8'))
    send_size = 0
    with open(path, 'rb') as f:
        Flag = True
        while Flag:
            if send_size + 1024 > file_size:
                data = f.read(file_size - send_size)
                Flag = False
                print('1已上传{0}%'.format(round((send_size+len(data)) / file_size * 100)))
            else:
                data = f.read(1024)
                send_size += 1024
                print('已上传{0}%'.format(round(send_size / file_size * 100)))
            sk.send(data)

sk.close()