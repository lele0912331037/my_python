#!/usr/bin.env python3
# -*- cnding:utf-8 -*-

#文件处理
f = open('/etc/passwd','r')
for i in f.readlines():
    i = i.strip('\n').split(':')
    print (i)