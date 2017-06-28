#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def count(n):
    return lambda x, y: x-y
print(count(1)(1, 2))

a = [(lambda x, i=i:i**i) for i in range(10)]
b = (lambda x, i=i: i**i for i in range(10))
print('111', next(b)(2))
for i in b:
    print(i(2))
for c in a:
    print(c(2))

print(list(x**x for x in range(10)))
