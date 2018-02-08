#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# decorator可以在代码运行期间动态添加功能
import functools


def log(s):
    """带参数的装饰器"""
    print(s)

    def decorator(func):
        @functools.wraps(func)  # 将装饰后的函数名称属性复原
        def wrapper(*args, **kw):
            print('call %s():' % func.__name__)  # 打印调用函数名
            return func(*args, **kw)
        return wrapper
    return decorator


@log('this is parameter of log')
def now():
    print('2015-3-25')
now()
print(now.__name__)
