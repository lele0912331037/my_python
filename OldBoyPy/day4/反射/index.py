#!/usr/bin/env python3
# -*- coding: utf-8 -*-

data = input('请输入地址：')
array = data.split('/')

user_import = __import__('backend.'+array[0])
model = getattr(user_import, array[0])
func = getattr(model, array[1])
func()

# from backend import account
# account.login()
