#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from backend import CustomException
data = input('请输入地址：')
array = data.split('/')

# 异常处理
try:
    user_import = __import__('backend.'+array[0])
    model = getattr(user_import, array[0])
    func = getattr(model, array[1])
    func()
    # 调用自定义类
    raise CustomException.MyException('自定义错误')
except ImportError as e:
    print('ImportError 错误异常处理：\n', e)
except AttributeError as e:
    print('AttributeError 错误异常处理：\n', e)
except Exception as e:
    print('Exception 错误异常处理：\n', e)
#else:
#    print('没有异常，执行')
finally:
    print('无论错误与否，都执行')
# from backend import account
# account.login()


