#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 位置参数，默认参数，可变参数，关键字参数，命名关键字参数
# 形参和实参：形参为函数定义的参数名，实参为函数调用时传入的参数

# 默认参数
print('默认参数:')


def default(username, where='北京', action='巡山'):
    print(username, '去', where, action)
default('yinxiaole')
default('haha', action='睡觉')
default('heihei', action='吃饭', where='上海')

# 可变参数
print('可变参数:')


def show(*arg):
    print(arg)
show('zhangsan', 'lisi', 'wangwu', 'maliu')
list1 = ['zhangsan', 'lisi', 'wangwu', 'maliu']
show(*list1)
show()

# 关键字参数
print('关键字参数:')


def show1(**kwargs):
    # for item in kwargs:
    print(kwargs)
show_dict = {'name': 'yinxl', 'age': 24, 'city': '北京', 'job': '科学家'}
show1(name='yinxl', age=24, city='北京', job='科学家')
show1(**show_dict)
show1()
# 命名关键字参数
print('命名关键字参数:')


def show2(name, age, *, city, job):
    print('name:', name, 'age:', age, 'city:', city, 'job:', job)
show2('yinxl', 24, city='beijing', job='科学家')
# show2('yinxl',24,'bejing','科学家') 会报错

# 参数排序组合
print('参数排序组合:')


def set1(name, age, city='北京', *args, **kwargs):
    print('set1:', 'name:', name, 'age:', age, 'city:', city, 'args:', args, 'kwargs:', kwargs)


def set2(name, age, city='北京', *, job, **kwargs):
    print('set2:', 'name:', name, 'age:', age, 'city:', city, 'job:', job, 'kwargs:', kwargs)
# 只给前两个必选参数
set1('yinxl', 24)
# set2('yinxl',24)  需要job参数
# 带上job参数
set1('yinxl', 24, job='科学家')
set2('yinxl', 24, job='科学家')
# 带上默认参数
set1('yinxl', 24, '上海', job='科学家')
set2('aaayinxl', 24, city='上海', job='科学家')
# 带入多个可变参数
set1('yinxl', 24, '上海', 'a', 'b')
# set2('yinxl',24,'上海','a','b') 报错，set2没有可变参数
# 带入关键字参数
set1('yinxl', 24, '上海', 'a', 'b', c='123', d='456')
set2('yinxl', 24, '上海', job='科学家', c='123', d='456')

