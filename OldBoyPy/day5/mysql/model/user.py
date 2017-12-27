#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from utility.sql_helper import MySqlHelper


class User(object):

    def __init__(self):
        self.__helper = MySqlHelper()

    def get_id(self, ids):
        sql = "select * from user where id = %s"
        params = (ids,)
        return self.__helper.get_one(sql, params)

    def check_validate(self, user, pwd=None):
        if not pwd:
            sql = "select name from user WHERE name = %s "
            params = (user,)
        else:
            sql = "select * from user WHERE name = %s AND password = %s"
            params = (user, pwd,)
        return self.__helper.get_one(sql, params)

    def insert_one(self, user, pwd):
        sql = "insert into user(name,password) values(%s,%s)"
        params = (user, pwd)
        return self.__helper.insert_one(sql, params)
