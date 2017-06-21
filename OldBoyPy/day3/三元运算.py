#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 三元运算
def yunsuan(a, b):
    if a > b:
        print(a)
    else:
        print(b)
yunsuan(1, 2)

# 三元运算简化代码
def yunsuan1(a, b):
    print(a if a > b else b)
    print( s='1' if a>b else s='2')
yunsuan1(1, 2)
