#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import functools


def log(name):
    def decorator(func):
        def wrapper(*args, **kw):
            if hasattr(name, '__name__'):
                print('begin call %s() with no logname' % func.__name__)
                result = func(*args, **kw)
                print('end call %s() with no logname' % func.__name__)
            else:
                print('begin call %s() with logname %s' % (func.__name__, name))
                result = func(*args, **kw)
                print('end call %s() with logname %s' % (func.__name__, name))
            return result
        return wrapper

    return decorator(name) if hasattr(name, '__name__') else decorator

@log('log.txt')
def f(str):
    print('function f %s' % str)
    return 1

@log
def g(str):
    print('function g %s' % str)
    return 2

f('f')
g('g')
