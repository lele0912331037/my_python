#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from model.user import User


def login():
    username = input("username:")
    password = input("password:")
    user = User()
    result = user.check_validate(username, password)
    if not result:
        print("用户名密码错误")
    else:
        print("成功")

if __name__ == "__main__":
    login()
