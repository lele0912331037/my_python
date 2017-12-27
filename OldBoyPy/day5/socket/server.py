#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import socket
'''
sk = socket.socket()
ip_port = ('127.0.0.1', 10086)
sk.bind(('127.0.0.1', 10086))
sk.listen(5)

num = 0
while True:
    conn, address = sk.accept()
    str1 = "hello,%s, this is %s time" % (address[0], num)
    conn.send(str1.encode())
    while True:
            num += 1
            data = conn.recv(1024)
            print(data)
            str1 = "hello,%s, this is %s time" % (address[0], num)
            conn.send(str1.encode())
    conn.close()
    '''

# 开启ip和端口
ip_port = ('127.0.0.1', 8080)
# 生成句柄
web = socket.socket()
# 绑定端口
web.bind(ip_port)
# 最多连接数
web.listen(5)
# 等待信息
print('nginx waiting...')
# 开启死循环
while True:
    # 阻塞
    conn, address = web.accept()
    # 获取客户端请求数据
    data = conn.recv(1024)
    # 打印接受数据 注：当浏览器访问的时候，接受的数据的浏览器的信息等。
    print(data.decode())
    # 向对方发送数据
    conn.send(bytes("HTTP/1.1 200 OK\r\n\r\n", encoding="utf8"))
    conn.send(bytes('<h1>welcome nginx</h1>', encoding='utf8'))
    # 关闭链接
    conn.close()


'''
def handle_request(client):
    buf = client.recv(1024)
    client.send(bytes("HTTP/1.1 200 OK\r\n\r\n", encoding="utf8"))
    client.send(bytes("Hello, World", encoding='utf8'))


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 8080))
    sock.listen(5)

    while True:
        connection, address = sock.accept()
        handle_request(connection)
        connection.close()


if __name__ == '__main__':
    main()
'''