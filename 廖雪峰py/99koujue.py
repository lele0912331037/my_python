#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from enum import Enum
# 使用枚举


class Num(Enum):
    """ 枚举类"""
    一 = 1
    二 = 2
    三 = 3
    四 = 4
    五 = 5
    六 = 6
    七 = 7
    八 = 8
    九 = 9
    十 = 0
    得 = 10

# 方法1
for x in range(1, 10):
    for j in range(1, x+1):
        Sum = j*x
        if Sum < 10:
            Sum = Num(10).name + Num(Sum).name
        else:
            Sum = str(Sum)
            if Sum[1] == '0':
                Sum = Num(int(Sum[0])).name + Num(int(Sum[1])).name
            else:
                Sum = Num(int(Sum[0])).name + Num(0).name + Num(int(Sum[1])).name
        print(Num(j).name + Num(x).name + Sum, end="  ")
    print(" ")

# 方法2
for x in range(1, 10):
    for j in range(1, x+1):
        Sum = '%s%s%s' % (j, x, x*j)
        if len(Sum) == 4:
            if Sum[3] == '0':
                Sum1 = Num(int(Sum[2])).name + Num(0).name
            else:
                Sum1 = Num(int(Sum[2])).name + Num(0).name + Num(int(Sum[3])).name
        else:
            Sum1 = Num(10).name + Num(int(Sum[2])).name
        Sum = Num(int(Sum[0])).name + Num(int(Sum[1])).name + Sum1
        print(Sum, end=' ')
    print(" ")


# 使用dict字典
num = {'一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9}

# 方法1


def find_num(n):
    """通过value获取key"""
    for i in num:
        if num[i] == n:
            return i

for key in num:
    for item in num:
        Sum = num[item] * num[key]
        if Sum < 10:
            Sum = '得' + find_num(Sum)
        else:
            Sum = str(Sum)
            if Sum[1] != '0':
                Sum = find_num(int(Sum[0])) + '十' + find_num(int(Sum[1]))
            else:
                Sum = find_num(int(Sum[0])) + "十 "
        print(item + key + Sum, end=" ")
        if key == item:
            num2 = num['一']
            break
    print(" ")

# 方法2
for key in num:
    for item in num:
        Sum = '%s%s%s' % (item, key, num[item] * num[key])
        #print(Sum, end=' ')
        print(Sum, end=' ')
        if key == item:
            num2 = num['一']
            break
        if len(Sum) == 4:
            if Sum[3] == '0':
                Sum1 = find_num(int(Sum[2])) + '十'
            else:
                Sum1 = find_num(int(Sum[2])) + '十' + find_num(int(Sum[3]))
        else:
            Sum1 = '得' + find_num(int(Sum[2]))
        Sum = find_num(int(Sum[0])) + find_num(int(Sum[1])) + Sum1
    print(" ")


numA = {'1': '一', '2': '二', '3': '三', '4': '四', '5': '五', '6': '六', '7': '七', '8': '八', '9': '九', '0': '十'}

# 方法2
for x in range(1, 10):
    for j in range(1, x+1):
        Sum = x * j
        if Sum >= 10:
            Sum = str(Sum)
            if Sum[1] == 0:
                Sum = numA[Sum[0]] + numA['0']
            else:
                Sum = numA[Sum[0]] + numA['0'] + numA[Sum[1]]
        else:
            Sum = '得' + numA[str(Sum)]
        print(numA['{}'.format(j)] + numA[str(x)] + Sum, end=" ")
    print(" ")

# 方法3
for x in range(1, 10):
    for j in range(1, x+1):
        Sum = '%s%s%s' % (j, x, x*j)
        if len(Sum) == 4:
            if Sum[3] != '0':
                Sum1 = numA[Sum[2]] + "十" + numA[Sum[3]]
            else:
                Sum1 = numA[Sum[2]] + "十" + " "
        else:
            Sum1 = '得' + numA[Sum[2]]
        Sum = numA[Sum[0]] + numA[Sum[1]] + Sum1
        print(Sum, end=' ')
    print(' ')
