#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pymysql
conn_dict = dict(
            host='10.10.9.240',
            user='root',
            password='123456',
            database='08day5',
            cursorclass=pymysql.cursors.DictCursor)
conn_dict2 = {
            'host': '10.10.9.240',
            'user': 'root',
            'password': '123456',
            'database': '08day5',
            'cursorclass': pymysql.cursors.DictCursor, }
