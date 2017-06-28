#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class MyException(Exception):

    def __init__(self, msg):
        self.error = msg

    # 类默认返回的数据
    def __str__(self, *args, **kwargs):
        return self.error
    __repr__ = __str__

a = MyException('123')
print(a)