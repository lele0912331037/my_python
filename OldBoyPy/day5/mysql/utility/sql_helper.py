#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pymysql
import conf

class MySqlHelper(object):
    def __init__(self):
        self.__conn_dict = conf.conn_dict
        self.__conn_dict2 = conf.conn_dict2

    def get_dict(self, sql, params):
        """ 创建数据库连接"""
        conn = pymysql.connect(**self.__conn_dict)
        # 打开数据库
        cursor = conn.cursor()
        cursor.execute(sql, params)
        data = cursor.fetchall()
        conn.close()
        return data

    def get_one(self, sql, params):
        """ 创建数据库连接"""
        conn = pymysql.connect(**self.__conn_dict)
        # 打开数据库
        cursor = conn.cursor()
        cursor.execute(sql, params)
        data = cursor.fetchone()
        conn.close()
        return data

    def insert_one(self, sql, params):
        conn = pymysql.connect(**self.__conn_dict2)
        # 打开数据库
        cursor = conn.cursor()
        str = cursor.execute(sql, params)
        conn.commit()
        conn.close()
        return str

