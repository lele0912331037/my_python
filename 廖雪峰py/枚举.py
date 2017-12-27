#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 枚举
from enum import Enum


class Num(Enum):
    一 = 1
    二 = 2
    三 = 3
    四 = 4
    五 = 5
    六 = 6
    七 = 7
    八 = 8
    九 = 9
    十 = 0
    得 = 10

for x in range(1, 10):
    for j in range(1, x+1):
        Sum = j*x
        if Sum < 10:
            Sum = Num(10).name + Num(Sum).name
        else:
            Sum = str(Sum)
            if Sum[1] == '0':
                Sum = Num(int(Sum[0])).name + Num(int(Sum[1])).name
            else:
                Sum = Num(int(Sum[0])).name + Num(0).name + Num(int(Sum[1])).name
        print(Num(j).name + Num(x).name + Sum, end="  ")
    print(" ")

for x in range(1, 10):
    for j in range(1, x+1):
        Sum = '%s%s%s' % (j, x, x*j)
        if len(Sum) == 4:
            if Sum[3] == '0':
                Sum1 = Num(int(Sum[2])).name + Num(0).name
            else:
                Sum1 = Num(int(Sum[2])).name + Num(0).name + Num(int(Sum[3])).name
        else:
            Sum1 = Num(10).name + Num(int(Sum[2])).name
        Sum = Num(int(Sum[0])).name + Num(int(Sum[1])).name + Sum1
        print(Sum, end=' ')
    print(" ")