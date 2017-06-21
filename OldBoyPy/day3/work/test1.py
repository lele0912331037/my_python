#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def test(a, b, c=1, *args, **kwargs):
    bb = ['1500']
    print(a, b, c, args, kwargs)


test('aa', 'bb', user='yinxl', old='1500', new='200')
aa = {'user': 'yinxl', 'old': '1500', 'new': '200'}
print(aa['user'])