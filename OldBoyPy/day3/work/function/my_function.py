#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import hashlib


def get_md5(user, pwd):
    # md5加密
    md5 = hashlib.md5()
    md5.update((pwd+user+'@123').encode('utf-8'))
    return md5.hexdigest()


def shop(user, my=15000):
    # 注册用户默认有15000元
    with open('./database/shop.txt', 'a+') as f:
        str1 = '%s %s\n' % (user, my)
        f.write(str1)


def write_change(*kw):
    # 购物列表
    with open('./database/change.txt', 'w') as f:
        f.write('\n'.join(kw))


def file_type(file, wr=1, *args, **kwargs):
    print(args, wr, file)
    if wr == 1:
        with open('./database/{0}'.format(file), 'r') as f_read:
            for item in f_read.readlines():
                yield item
    elif wr == 2:
        with open('./database/{0}'.format(file), 'w+') as f_write:
            f_write.write('\n'.join(args))
    elif wr == 3:
        print(args, wr, file)
        with open('./database/{0}'.format(file), 'a+') as f_a:
            f_a.write('\n{0}'.format(' '.join(args)))




def write_shop(user, old_free, new_free):
    with open('./database/shop.txt', 'r') as f:
        lines = f.readlines()
    with open('./database/shop.txt', 'w+') as f_w:
        for line in lines:
            if user in line:
                line = line.replace(str(old_free), str(new_free))
                f_w.write(line)
                continue
            f_w.write(line)

