#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from model.user import User
import sys
# import model.user


def login(username, password):
    user = User()
    result = user.check_validate(username, password)
    if not result:
        print("用户名密码错误")
        return False
    else:
        print("成功")
        return True


def register(username, password):
    user = User()
    user_register = user.check_validate(username)
    if user_register:
        print('用户【%s】存在，重新输入' % username)
        return False
    else:
        user.insert_one(username, password)
        print("用户【%s】注册成功" % username)
        return True


def login_input():
    user = input("username:")
    pwd = input("password:")
    return user, pwd

if __name__ == "__main__":
    while True:
        choose = input('请选择操作:\n1 注册\n2 登陆\n3 退出\n')
        if choose == '1':
            while True:
                user, pwd = login_input()
                if register(user, pwd):
                    break
        if choose == '2':
            while True:
                user, pwd = login_input()
                if login(user, pwd):
                    break
        if choose == '3':
            sys.exit()
