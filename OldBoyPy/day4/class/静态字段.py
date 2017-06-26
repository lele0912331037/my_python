#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Province:

    # 静态字段，属于类
    memo = '中国的省份'

    def __init__(self, name, capital, leader):
        # 动态字段,属性
        self.Name = name
        self.Capital = capital
        self.Leader = leader

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

# 定义对象实例
HB = Province('河北', '石家庄', '李XX')
HN = Province('河南', '郑州', '王XX')

# 调用动态字段
print(HB.Leader)

# 调用静态字段
print(Province.memo)

# 类不能访问动态字段
# print(Province.Leader)

# 对象(实例)可以访问静态字段，不建议使用
print(HB.memo)

# 对象(实例)调用动态方法
HB.sports_meet()
HN.sports_meet()

# 调用静态方法
Province.Foo()

# 调用特性
HB.Bar
