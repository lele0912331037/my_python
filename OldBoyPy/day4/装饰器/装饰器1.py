#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#def outer(fun):
#    def wrapper():
#        print('装饰器')
#        return fun()
#    return wrapper()
#
#
#@outer
#def fun1():
#    print('fun1')
#
#
#@outer
#def fun2():
#    print('fun2')
#
#
#@outer
#def fun3():
#    print('fun3')
#
#
#def fun4():
#    print('fun4')


def Filter(before_func, after_func):
    def outer(main_func):
        def wrapper(request, kargs):
            before_result = before_func(request, kargs)
            if before_result != None:
                return before_func

            main_result = main_func(request, kargs)
            if main_result != None:
                return main_result
            after_result = after_func(request, kargs)
            if after_result != None:
                return after_func
        return wrapper
    return outer


@Filter()
def list(request, kargs):
    print(request, kargs)
list('ww', 'cc')