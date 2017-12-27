#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import socketserver
import os


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        base_path = '/tmp'
        conn = self.request
        print('connnected...')
        while True:
            pre_data = conn.recv(1024).decode()
            cmd, file_name, file_size = pre_data.split('|')
            recv_size = 0
            file_dir = os.path.join(base_path, file_name)
            f = open(file_dir, 'wb')
            print(file_size, type(file_size), type(recv_size))
            Flag = True
            while Flag:
                if int(file_size) > recv_size:
                    data = conn.recv(1024)
                    recv_size += len(data)
                    f.write(data)
                else:
                    recv_size = 0
                    Flag = False
                    continue
            print('upload successed.')
            f.close()
isinstan = socketserver.ThreadingTCPServer(('127.0.0.1', 10086), MyServer)
isinstan.serve_forever()