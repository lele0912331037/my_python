#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
# mysql 数据库操作
# 登陆
mysql -uroot -p'123456' --host=ip
# 显示数据库
show databases;
# 创建数据库
create database 08day5;
# 使用数据库
use 08day5;
# 显示表
show tables;
# 创建表
create table UserInfo(id int,name varchar(10));
# 插入数据
insert into UserInfo(id,name) values(1,'alex');
# 查询所有
select * from userinfo;
# 更行
update userinfo set name='sb';
update userinfo set name :'alex' where id:1;
# 删除
delete from userinfo;
'''
# 安装 pymysql
# pip3 install PyMySQL
import pymysql


def my_sql(sql, params=None, types=1, mode='relative', values=0):
    """ 创建数据库连接"""
    conn = pymysql.connect(host='10.10.9.240',
                           user='root',
                           password='123456',
                           database='08day5',
                           cursorclass=pymysql.cursors.DictCursor)
    # 打开数据库
    cursor = conn.cursor()

    # 1为查询所有
    if types == 1:
        cursor.execute(sql, params)
        data = cursor.fetchall()
        return data
    # 4为查询一条
    elif types == 4:
        cursor.execute(sql, params)
        # scroll 指针 mode：absolute relative
        cursor.scroll(values, mode)
        data = cursor.fetchone()
        return data
    # 3为批量操作，2为单一执行
    else:
        if types == 3:
            recount = cursor.executemany(sql, params)
        elif types == 2:
            recount = cursor.execute(sql, params)
        conn.commit()
        # 获取id 返回执行结果和获取的id
        new_id = cursor.lastrowid
        return recount, new_id

# 查询
sqlcomm = 'select * from user'
print(my_sql(sqlcomm))

sql_select = "select * from user where id = %s"
params = (2,)
print(my_sql(sql_select, params))

# 插入
sql_insert = "insert into user(name,password) values(%s,%s)"
params = ('sb', '123456')
print(my_sql(sql_insert, params, 2))

# 更新
sql_update = "update user set name = %s WHERE id = 1"
params = ('sb', )
print(my_sql(sql_update, params, 2))

# 删除
sql_delete = "delete from user where name = %s "
li = [('sb',)]
params = (li)
print(my_sql(sql_delete, params, 3))

# 批量插入
'''
li = [('yxl', '123123'), ('xly', '321321')]
sql_updates = "insert into user(name, password) values(%s,%s)"
params = (li)
print(my_sql(sql_updates, params, 3))
'''
# 查询一条
sql_select_one = "select * from user"
print(my_sql(sql_select_one, None, 4))

# scroll 指针 absolute relative
sql_select_one = "select * from user"
print(my_sql(sql_select_one, None, 4, 'relative', 1))
