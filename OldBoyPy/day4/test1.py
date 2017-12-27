#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import operator

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list1*2)

def a(num):
    return num, str(num)
print(list(map(a, list1)))

c = list(map(lambda x: (x, str(x)), list1))
print(c, type(c[1]))
new_lines = []


def convert(a, b):
    size = 0
    with open(a, 'r') as f:
        while size < 10:
            lines = f.readline()
            print(f.tell())
            print(lines)
            size += 1
        '''
        for i in lines:
            print(i)
            i = i.split('|')
            print(i)

            i[1] = i[1]+i[2]
            del i[2]
            if i[2] != 'nv':
                new_lines.append(i)
                #with open(b, 'a') as fs:
                #    fs.write(','.join(i)+"\n")
    print(new_lines)
    #J = new_lines.sort(key=operator.itemgetter(1))
    #print(J)
    '''
dd = convert('aa', 'bb')
# print(new_lines)
'''
L = [('b',6),('a',1),('c',3),('d',4)]
L = [['10', 'zhangsan', 'nan', '20', '82'], ['3', 'hasi', 'nan', '20', '44']]
#L.sort(lambda x,y:cmp(x[1],y[1]))
L.sort(key=operator.itemgetter(1))
print(L)
print(type(int('123555')))
'''

import os

print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:
pid = os.fork()
print(pid)
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))