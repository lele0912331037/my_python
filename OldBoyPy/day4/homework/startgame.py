#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# from game_function import init_profession
# from game_class import profession
lists = ['逍遥生', '剑侠客', '飞燕女', '英女侠']


def choose_ps(types=1, *args, **kwargs):
    ps_list = args
    print(ps_list)
    if types == 1:
        return ps_list
    elif types == 2:
        for num, item in enumerate(choose_ps(), 1):
            if choose == str(num):
                return item
a = choose_ps(*lists)
print(a)
#for num, item in enumerate(choose_ps(*lists), 1):
#    print(num, item)
#choose = input('请选择你的角色:')