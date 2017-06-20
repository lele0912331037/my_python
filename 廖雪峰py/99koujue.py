#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import Enum,unique

@unique
class numbuers(Enum):
    pass
num={'一':1,'二':2,'三':3,'四':4,'五':5,'六':6,'七':7,'八':8,'九':9,'十':10,'得':11}
for x in num:
    for j in num:
        print('%s%s得%s' % (j,x,int(num[j])*int(num[x])))
for x in range(1,10):
    for j in range(1,x+1):
        print ('%s+%s=%s' % (j,x,j*x),end=" ")
    print(" ")
