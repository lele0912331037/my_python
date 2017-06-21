#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from function import my_function


def register(username, password):
    # 注册函数
    status = 0
    for j in my_function.file_type('db.txt'):
        j = j.split()
        if username == j[0]:
            status = 1
    if status == 1:
        print('账户已存在，请重新输入')
    else:
        my_function.file_type('db.txt', 3, username, my_function.get_md5(username, password))
        print('注册成功，', username, '你好')
        my_function.file_type('shop.txt', 3, username, '15000')


def login():
    # 登陆函数
    status, num = 0, 1
    while num <= 3:
        username, password = input('请输入用户名：'), input('请输入密码：')
        for line in my_function.file_type('lock_file.txt'):
            if username == line:
                print('该账户已锁定！')
                sys.exit()
        pwd = my_function.get_md5(username, password)
        for x in my_function.file_type('db.txt'):
            x = x.split()
            if username == x[0] and pwd == x[1]:
                status = 1
                break
        if status == 1:
            print('登陆成功 hello', username)
            return True, username
        else:
            num += 1
            print('用户名或密码错误,请重新输入')
    else:
        print('输入错误达3次，账户%s已锁定' % username)
        my_function.file_type('lock_file.txt', 3, username)


def showlist(user):
    for l in my_function.file_type('shop.txt'):
        l = l.split()
        u = l[0]
        if user == u:
            u, old_free = l[0], int(l[1])
            break
    while True:
        print(u, '你好，你的余额为', old_free, '\n序号 商品名称 价格')
        for j in my_function.file_type('showlist.txt'):
            print(j.strip())
        num = int(input('请选择要购买的商品,退出输入0:'))
        if num == 0:
            break
        for x in my_function.file_type('showlist.txt'):
            x = x.split()
            if str(num) == x[0]:
                new_free = old_free - int(x[2])
                my_function.file_type('change.txt', 3, x[1]+' '+x[2]+' 1')
        if new_free < 0:
            print('可用余额不足,退出到主界面')
            break
        print('购买的商品如下:\n商品名称 价格 数量')
        for change_item in my_function.file_type('change.txt'):
            print(change_item)
            my_function.file_type('{0}_change.txt'.format(user), 3, change_item)
        my_function.file_type('shop.txt', 4, user=str(user), old=str(old_free), new=str(new_free))
        old_free = new_free
session_user = None
while True:
    choose = input('请选择操作:\n1 注册\n2 登陆\n3 退出\n')
    if choose == '1':
            register(input('请输入用户名：'), input('请输入密码：'))
    elif choose == '2':
        if session_user == None:
            loging = login()
            if loging:
                session_user = loging[1]
        print('请选择操作')
        choose_ch = input('1 购物\n2 取现\n3 查看余额\n4 查看账单\n5 退出 ')
        if choose_ch == '1':
            showlist(session_user)
    elif choose == '3':
        sys.exit()