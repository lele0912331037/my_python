#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from functools import reduce

# help() 帮助
a = []
# help(a)

# dir() 获取方法
print(dir(a))
# www.cnblogs.com/wupeiqi/articles/4276448.html

# pow() 求次方
print(pow(2, 5))

# len() 字符串的长度
print(len('123sd'))

# all() 参数都为真，返回True
print(all([1, 2, 3, 4, 5]))
print(all([1, 2, 3, 0, 3]))

# any() 参数有真时，返回True
print(any([0, 0, 0, 4, 0]))
print(any([0, 0, 0, 0, 0]))

# chr() ord() 编码转换
print(chr(65), chr(66), chr(67), chr(68), chr(69))
print(ord('A'), ord('B'), ord('C'), ord('D'), ord('E'))

# hex() oct() bin() 进制转换
print(hex(2), oct(2), bin(2))

# range() 生成列表
print(range(0, 10))
for i in range(10):
    print(i)

# enumerate() 获取/添加索引
for k, v in enumerate([1, 2, 3, 4]):
    print(k, v)

# 格式化字符串
print('i am {0} {1}'.format('yin', 'xiaole'))
print('i am %s %s' % ('yin', 'xiaole'))

# map 返回迭代器，需要list
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5])))

# filter，返回迭代器，需要list
tmp = filter(lambda x: x % 2 == 1, range(10))
print(list(tmp))

# reduce，返回非迭代器，不需要使用list
print(reduce(lambda x, y: x + y, range(10)))

#
x = [1, 2, 3]
y = [4, 5, 6]
z = [4, 5, 6]
print(list(zip(x, y, z)))

# eval
com = compile('1+1', '', 'eval')
print(eval(com))

# 字符串的形式导入模块
# __import__() 动态导入模块
# hasattr() 判断模块是否有此函数
# delattr() 删除模块某个函数
# getattr() 获取模块某个函数
temp = 'sys'
module = __import__(temp)
print(dir(module))

# 字符串的形式执行函数
val = hasattr(module, 'version')
print(val)

# join()：    连接字符串数组。将字符串、元组、列表中的元素以指定的字符(分隔符)连接生成一个新的字符串
# os.path.join()：  将多个路径组合后返回
### 链接： http://www.cnblogs.com/jsplyy/p/5634640.html
