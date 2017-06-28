#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 函数调用


def login(username):
    if username == 'yinxl':
        return '1'
    else:
        return '2'


def detail(user):
    print('%s 你好 ' % user)
if __name__ == "__main__":
    user = input('请输入用户名：')
    res = login(user)
    if res == '1':
        detail(user)
    else:
        print('无此用户')
