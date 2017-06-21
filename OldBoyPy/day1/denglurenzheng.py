#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

users = {'root':'123','guest': '123','ftp': '123456'}
#locks = []
i = 1
status = 0
while i <= 3:
    user = str(input('请输入用户名:'))
    #locks.append(user)
    lock = open('lock_file','r')
    for line in lock.readlines():
        if user == line:
            print('该账户已锁定！')
            sys.exit()
    pwd = str(input('请输入密码:'))
    for x in users:
        if user == x and pwd == users[x]:
            status = 1
            break
    if status ==1:
        print('登陆成功！欢迎用户%s' % user)
        break
    else:
        i += 1
        print('用户名或密码错误')
else:
    print('输入错误达3次，账户%s已锁定' % user) 
    f = open('lock_file','a')
    f.write(user)
    f.close()      
#BUG: 三次每次输入的用户非同一个用户，则锁定的为第三次输入的用户。