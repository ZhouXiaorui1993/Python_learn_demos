#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志
import functools
from inspect import isfunction

# def log(func):
#
#     def wrapper(*args, **kw):
#         print("begin call: %s" % func.__name__)
#         f = func(*args, **kw)
#         print("end call: %s" % func.__name__)
#         return f
#     return wrapper
#
#
# @log
# def h2():
#     print("Kunimi Hiro & Amamiya Hikari")


def log(text):  # 写一个@log的decorator，使它既支持有参数，又支持无参数

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args2, **kw):
            print("begin call: %s" % func.__name__)
            f = func(*args2, **kw)
            print("end call: %s" % func.__name__)
            return f
        return wrapper
    if isinstance(text, str):
        print(text)
        return decorator
    else:
        f = text
        return decorator(f)


@log("execute touch")
def touch():
    print("Tatsuya and minami")


@log
def h2():
    print("Kunimi Hiro & Amamiya Hikari")


touch()
h2()