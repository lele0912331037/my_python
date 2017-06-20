#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a = ['甲','乙','丙','丁','戊','己','庚','辛','壬','癸']
b = ['子','丑','寅','卯','辰','巳','午','未','申','酉','戌','亥']
print ('方法1')
c=[]
for i in range(5):
    a.append(a[0])
    a.append(a[1])
    for n in range(12):
        c.append(a[n]+b[n])
        print(a[n]+b[n],end=" ")
    a.pop(0)
    a.pop(1)
#print(c)
print ('方法2')
for i in range(60):
    print(a[i%10]+b[i%12],end=" ")
#print (a[1])
