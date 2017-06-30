#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Race_dict = {'Terran': '人族', 'Fairy': '仙族', 'Orcs': '兽族'}
# Profession_dict = {'Datang': '大唐官府', 'Huasheng': '化生寺', 'Fangcun': '方寸山', 'Nver': '女儿村'}
# virtue_dict = {'physique': '体质', 'mana': '法力', 'power': '力量', 'endurance': '耐力', 'agile': '敏捷'}
# Add_point = ['1', '2', '5', '10', '20', '50', '全部']


def print_choose(choose='', *args, **kw):
    if args:
        for i, j in enumerate(args, 1):
            if choose == '':
                print(i, j)
            else:
                if choose == str(i):
                    return j
    elif kw:
        for i, j in enumerate(kw, 1):
            if choose == '':
                print(i, kw[j])
            else:
                if choose == str(i):
                    return j, kw[j]

# print(print_choose('1', **Profession_dict))