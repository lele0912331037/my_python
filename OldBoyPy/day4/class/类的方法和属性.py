#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Province(object):

    # 静态字段，属于类
    memo = '中国的省份'
    # 构造函数

    def __init__(self, name, capital, leader, flag):
        # 动态字段,属性
        self.Name = name
        self.Capital = capital
        self.Leader = leader
        # 动态私有字段，属性
        self.__thailand = flag

    # 定义类的动态方法
    def sports_meet(self):
        print(self.Name, '开运动会')

    # 定义静态方法
    @staticmethod
    def Foo():
        print('每个省都在反腐')

    # 将方法转换为属性，称：特殊属性
    @property
    def Bar(self):
        print(self.Name)

    # 访问将私有字段
    def get_thailand(self):
        return self.__thailand

    # 访问将私有字段,变方法为属性
    @property
    def get_private(self):
        return self.__thailand

    # 修改私有变量的方法
    def set_thailand(self, thailand):
        self.__thailand = thailand

    # 修改私有属性，使用变方法为属性
    @get_private.setter
    def get_private(self, value):
        self.__thailand = value

    # 定义私有方法
    def __private(self):
        print('我是私有方法')

    # 析构函数，释放类时python解释器调用
    #def __del__(self):
    #    print('#')

    # __call__方法
    def __call__(self, *args, **kwargs):
        print(*args, kwargs)

# 定义对象实例
HB = Province('河北', '石家庄', '李XX', False)
HN = Province('河南', '郑州', '王XX', True)

# 调用动态字段
print(HB.Leader)

# 调用静态字段
print(Province.memo)

# 类不能访问动态字段
# print

# 对象(实例)可以访问静态字段，不建议使用
print(HB.memo)

# 对象(实例)调用动态方法
HB.sports_meet()
HN.sports_meet()

# 调用静态方法
Province.Foo()

# 调用特性
HB.Bar

# 访问私有字段
HB.get_thailand()
HN.get_thailand()

# 强制调用私有方法,不建议使用
HB._Province__private()

# 私有方法变属性的访问 和修改
print(HB.get_private)
HB.get_private = True
print(HB.get_private)

#
HB()
'''
在一个实例里，
__girl表示“我是贞女，你不能上我”
_girl表示“你虽然可以上我，但你应该把我看做贞女”
girl表示“我是荡妇，谁都可以上我”
但是python仍然可以用_实例名__girl强上贞女
……
'''

#