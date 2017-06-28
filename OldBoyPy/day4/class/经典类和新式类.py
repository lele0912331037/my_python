#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 调用父类的init方法

# 新式类 object ,，2.2版本开始有新式类 3以上默认使用新式类
# 经典类

class A:
    def __init__(self):
        print('This is A')

    def save(self):
        print('save method from A')


class B(A):
    def __init__(self):
        print('This is B')


class C(A):
    def __init__(self):
        print('this is C')

    def save(self):
        print('save methed  from C')


class D(B, C):
    def __init__(self):
        print('this is D')
c = D()
print(c.save())

# 解决多重继承的执行顺序，深度优先和广度优先
