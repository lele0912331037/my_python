#!/usr/bin/env python3
# -*- coding: utf-8 -*-

for i in range(1, 10):
    for k in range(1, 10 - i):
        print(end="       ")
    for j in range(1, i + 1):
        print('%d*%d=%2d' % (j, i, j * i), end=" ")
    print(" ")


