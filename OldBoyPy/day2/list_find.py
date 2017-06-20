#!/usr/bin/env python3 
# -*- cnding:utf-8 -*-

name = ['2','2','3','4','5','6','7','8','9','2','3','44','66','2','3','2','5','7','9','2','8',]

next_num = 0
find_num = '2'
for x in range(name.count(find_num)):
    if x == 0:
        next_num = name.index(find_num)
    else:
        next_num = name.index(find_num,next_num+1)
    print (next_num)

next_num = 0
find_num = '2'
for x in range(name.count(find_num)):
    first_list = name[next_num:]
    first_num = first_list.index(find_num)
    print ('Find：第%s个%s的位置是%s' % ((x+1),find_num,(next_num+first_num)) )
    next_num=next_num+first_num+1