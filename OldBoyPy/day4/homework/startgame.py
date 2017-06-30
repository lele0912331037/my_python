#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from game_class import profession
from game_function import functions
Race_dict = {'Terran': '人族', 'Fairy': '仙族', 'Orcs': '兽族'}
Profession_dict = {'Datang': '大唐官府', 'Huasheng': '化生寺', 'Fangcun': '方寸山', 'Nver': '女儿村'}
virtue_dict = {'physique': '体质', 'mana': '法力', 'power': '力量', 'endurance': '耐力', 'agile': '敏捷'}
Add_point = ['1', '2', '5', '10', '20', '50', '全部']




# 打印种族列表
functions.print_choose('', **Race_dict)
# 获取种族类
ps = functions.print_choose(input('请选择你的种族:'), **Race_dict)
# 打印职业列表
functions.print_choose(**Profession_dict)
# 获取职业选择
ps_choose = functions.print_choose(input('请选择职业：'), **Profession_dict)
print(ps_choose)
# 初始化实例
user_import = __import__('game_class.profession', fromlist=True)
func = getattr(user_import, ps_choose[0])
user1 = func(ps_choose[1], ps[1])
# 打印实例的种族和职业
print(user1.get_race())
user1.grade = 120
print(user1.get_ab())
# 打印初始化属性
functions.print_choose(**virtue_dict)
while True:
    if user1.point > 0:
        add_virtue = functions.print_choose(input('请选择要增加的属性，突出输入0，'), **virtue_dict)
        while True:
            if user1.point > 0:
                add_point = functions.print_choose(input('请选择要增加的点数,退出输入0，'), *Add_point)
                if add_point == '0':
                    break
                user1.add_point(add_virtue, add_point)
            else:
                print('剩余属性点不足！')
                break
    else:
        print('没有多余属性点可加！')
        break

print(user1.__dict__)

