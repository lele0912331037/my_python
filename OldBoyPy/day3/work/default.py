#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from function import my_function

my_function.file_type('db.txt', 3, 'aa', my_function.get_md5('aa', '123'))


def register(username, password):
    # 注册函数
    status = 0
    #for j in my_function.file_type('db.txt', 1):
    #    j = j.split()
    #    if username == j[0]:
    #        status = 1
    if status == 1:
        print('账户已存在，请重新输入')
    else:
        my_function.file_type('db.txt', 3, username, my_function.get_md5(username, password))
        print('注册成功，', username, '你好')
        my_function.shop(username)


def login(username, password):
    # 登陆函数
    pwd = my_function.get_md5(username, password)
    status = 0
    for j in my_function.opendb():
        j = j.split()
        if username == j[0] and pwd == j[1]:
            status = 1
    if status == 1:
        print('登陆成功 hello', username)
    else:
        print('用户名/密码错误')


def showlist(user):
    change = []
    for l in my_function.openshop():
        l = l.split()
        u = l[0]
        if user == u:
            u, old_free = l[0], int(l[1])
            break
    print(u, '你好，你的余额为', old_free, '\n序号 商品名称 价格')
    for j in my_function.openfile():
        print(j)
    while True:
        num = int(input('请选择要购买的商品:'))
        for x in my_function.openfile():
            x = x.split()
            if str(num) == x[0]:
                new_free = old_free - int(x[2])
                old_free = new_free
                change.append(x[1]+' '+x[2]+' 1')
        if new_free < 0:
            print('可用余额不足,退出到主界面')
            break
        print(u, '你好，你的余额为', new_free, '购买的商品如下:\n商品名称 价格 数量')
        print('\n'.join(change))
        my_function.write_change(*change)
        my_function.write_shop(user, old_free, new_free)

while True:
    choose = input('请选择操作:\n1 注册\n2 登陆\n3 退出\n')
    if choose == '1':
        register(input('请输入用户名：'), input('请输入密码：'))
    elif choose == '2':
        login(input('请输入用户名：'), input('请输入密码：'))
        choose_ch = input('1 购物\n2 取现\n3 查看余额\n4 查看账单\n5 退出 ')
        if choose_ch == '1':
            showlist('yinxl')
        if choose_ch == '2':
            pass
        if choose_ch == '3':
            pass
        if choose_ch == '4':
            pass
        if choose_ch == '5':
            break
    elif choose == '3':
        sys.exit()

#                with open('change.txt', 'a+') as f:
#                    f.write('%s\n' % (' '.join(x)))