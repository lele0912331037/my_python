#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools

# 1 不带参数的装饰器
print('1 不带参数的装饰器')


def outer(func):
    def wrapper(*args, **kw):
        print('不带参数的装饰器:{0}'.format(func.__name__))
        return func(*args, **kw)
    return wrapper


@outer
def fun(*args, **kw):
    print('输入的实参是:', *args, kw)

fun('test1', test1='123')
print(fun.__name__)

# 2 带参数的装饰器
# 在函数执行前后各增加执行一个函数
print('\n\n2 带参数的装饰器')


def begin():
    # 函数一
    print('begin function')


def end():
    # 函数二
    print('end function')


def Filter(before_func, after_func):
    def outer(main_func):
        # 将原始函数(list)的__name__等属性复制到wrapper()
        @functools.wraps(main_func)
        def wrapper(*args, **kw):
            print('带参数的装饰器：{0}'.format(main_func.__name__), '传入的参数函数为：', before_func, after_func)
            before_func()
            main_result = main_func(*args, **kw)
            after_func()
            return main_result
        return wrapper
    return outer


@Filter(begin, end)
def fun(*args, **kw):
    print('输入的参数为：', args, kw)
fun('有参数装饰器', 参数='函数')
print(fun.__name__)

# 3 练习：
# #写一个@log的decorator装饰器，使它既支持
print('''3 练习
写一个@log的decorator装饰器，使它既支持
@log
def f():
    pass
又支持
@log('execute')
def f():
    pass

方法1''')


def log(text):
    # 方法1
    if isinstance(text, str) is False:
        @functools.wraps(text)
        def wrapper(*args, **kwargs):
            main_result = text(*args, **kwargs)
            return main_result
        return wrapper
    else:
        def decorator(main_func):
            @functools.wraps(main_func)
            def wrapper(*args, **kwargs):
                print('这是一个带参数的装饰器：%s' % (main_func.__name__))
                main_result = main_func(*args, **kwargs)
                return main_result
            return wrapper
        return decorator


@log
def log_func1(*args, **kwargs):
    print(*args, kwargs)


@log('execute')
def log_func2(*args, **kwargs):
    print(*args, kwargs)

log_func1('不带参数的装饰器', 函数为='func1')
log_func2('带参数的装饰器', 函数为='func2')
print('log_func1的__name__:', log_func1.__name__, 'log_func2的__name__:', log_func2.__name__)
print('\n方法2')


def log1(text):
    # 方法2，判断text参数是否有__call__方法，有表示是对象，返回decorator，没有返回decorator(text)函数
    def decorator(main_func):
        @functools.wraps(main_func)
        def wrapper(*args, **kwargs):
            x = '这是一个不带参数的装饰器：%s' % (main_func.__name__)
            y = '这是一个带参数的装饰器：%s 参数为%s' % (main_func.__name__, text)
            print(x) if hasattr(text, '__call__') else print(y)
            main_result = main_func(*args, **kwargs)
            return main_result
        return wrapper
    return decorator(text) if hasattr(text, '__call__') else decorator


@log1
def log1_func1(*args, **kwargs):
    print(*args, kwargs)


@log1('execute')
def log1_func2(*args, **kwargs):
    print(*args, kwargs)

log1_func1('不带参数的装饰器', 函数为='func1')
log1_func2('带参数的装饰器', 函数为='func2')
print('log1_func1的__name__:', log1_func1.__name__, 'log1_func2的__name__:', log1_func2.__name__)































