#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys,time
from function import my_function


def register(username, password, my='15000'):
    # 注册函数
    user_judges = my_function.user_judge(username, 'db.txt')
    if user_judges:
        print('账户已存在，请重新输入')
    else:
        my_function.file_type('db.txt', 3, username, my_function.get_md5(username, password))
        print('注册成功，', username, '你好')
        my_function.file_type('shop.txt', 3, username, my)


def login():
    # 登陆函数
    status, num = 0, 1
    while num <= 3:
        username, password = input('请输入用户名：'), input('请输入密码：')
        user_locked = my_function.user_judge(username, 'lock_file.txt')
        if user_locked:
            print('该账户已锁定！')
            sys.exit()
        user_pwd = my_function.get_md5(username, password)
        user_login = my_function.user_judge(username, 'db.txt')
        if user_login and user_pwd == user_login[1][1]:
            print('登陆成功 hello', username)
            return True, username
        else:
            num += 1
            print('用户名或密码错误')
    else:
        print('输入错误达3次，账户%s已锁定' % username)
        my_function.file_type('lock_file.txt', 3, username)


def showlist(user):
    # 购物函数，当前购买list，历史账单list，
    changes = []
    user_show_list = my_function.user_judge(user, 'shop.txt')
    if user_show_list:
        old_money = int(user_show_list[1][1])
    while True:
        print(user, '你好，你的余额为', old_money, '\n序号 商品名称 价格')
        for j in my_function.file_type('showlist.txt'):
            print(j.strip())
        num = int(input('请选择要购买的商品,退出输入0:'))
        if num == 0:
            break
        list_num = my_function.user_judge(str(num), 'showlist.txt')
        new_money = old_money - int(list_num[1][2])
        changes.append(list_num[1][1]+' '+list_num[1][2]+' 1')
        if new_money < 0:
            print('可用余额不足,退出到主界面')
            break
        print('购买的商品如下:\n商品名称 价格 数量')
        for change_item in changes:
            print(change_item)
            my_function.file_type('bill/{0}_change.txt'.format(user), 3, time.strftime('%Y-%m-%d %H:%M:%S'), 'pos刷卡', change_item)
        my_function.file_type('shop.txt', 4, user=str(user), old=str(old_money), new=str(new_money))
        old_money = new_money


session_user = None
while True:
    choose = input('请选择操作:\n1 注册\n2 登陆\n3 退出\n')
    if choose == '1':
            register(input('请输入用户名：'), input('请输入密码：'))
    elif choose == '2':
        loging = login()
        if loging:
            session_user = loging[1]
        else:
            continue
        while True:
            print('请选择操作')
            choose_ch = input('1 购物\n2 取现\n3 查看余额\n4 查看账单\n5 退出 ')
            if choose_ch == '1':
                showlist(session_user)
            elif choose_ch == '2':
                tack = my_function.user_judge(session_user, 'shop.txt')[1][1]
                print('{0}的账户余额为：'.format(session_user), tack)
                tack_value = int(input('请输入取款金额:'))
                if my_function.tack_function(session_user, tack_value):
                    my_function.file_type('bill/{0}_change.txt'.format(session_user), 3, time.strftime('%Y-%m-%d %H:%M:%S'), 'pos取款',
                                          str(tack_value))
                    print('取款成功，余额为：', tack)
            elif choose_ch == '3':
                user_money = my_function.user_judge(session_user, 'shop.txt')
                print('用户', session_user, '的余额为人民币', user_money[1][1], '元')
            elif choose_ch == '4':
                print('时间 消费类型 商品名称 商品价格 数量')
                for changelist in my_function.file_type('bill/{0}_change.txt'.format(session_user)):
                    print(changelist.strip())
            elif choose_ch == '5':
                session_user = None
                break
    elif choose == '3':
        sys.exit()
