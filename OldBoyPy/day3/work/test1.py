#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from function import my_function
import os
for x in my_function.file_type('db.txt'):
    print(x)
    x = x.split()
    print(x[0])

path = '/data/scripts/restart/auto_deploy/'

print(path+'old_system_market3.sh')
print('%sold_system_market3.sh' % path)
os.system('ls {0}sold_system_market3'.format(path))

li = (True, ['yinxl', 'eaf771f7c5217e240774f9c0ca5fa306'])
print(li[1][1])