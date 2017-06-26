#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import hashlib


def get_md5(user, pwd):
    # md5加密
    md5 = hashlib.md5()
    md5.update((pwd+user+'@123').encode('utf-8'))
    return md5.hexdigest()


def user_judge(username, table_list):
    # 判断输入和文件内字符是否相等
    for item in file_type(table_list):
        item = item.split()
        if username == item[0]:
            return True, item
    else:
        return False


def file_type(file, wr=1, *args, **kwargs):
    # 对文件的操作,读取,追加,覆盖和替换
    # 读取
    if wr == 1 or wr == 4:
        with open('./database/{0}'.format(file), 'r') as f_read:
            lines = f_read.readlines()
        # 替换单个字符串
        if wr == 4:
            with open('./database/{0}'.format(file), 'w+') as f_w:
                for line in lines:
                    if kwargs['user'] in line:
                        line = line.replace(str(kwargs['old']), str(kwargs['new']))
                        f_w.write(line)
                        continue
                    f_w.write(line)
        return lines
    # 覆盖(2),追加(3)
    else:
        if wr == 2:
            wr_str = 'w+'
        elif wr == 3:
            wr_str = 'a+'
        with open('./database/{0}'.format(file), wr_str) as f_a:
            f_a.write('{0}\n'.format(' '.join(args)))


def tack_function(user, tack_money):
    tack_user = user_judge(user, 'shop.txt')
    if tack_user:
        old_money = int(tack_user[1][1])
        if old_money < 0:
            print('账户余额错误')
        elif tack_money > old_money:
            print('余额不足')
        else:
            new_money = old_money - tack_money
            file_type('shop.txt', 4, user=str(user), old=str(old_money), new=str(new_money))
            return True
