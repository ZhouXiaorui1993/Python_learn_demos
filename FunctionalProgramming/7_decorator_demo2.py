#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间
import time
import functools


def metric(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        begin = time.time()
        f = func(*args, **kw)  # 要计算执行时间，所以需要先执行函数
        end = time.time()
        print('%s executed in %s ms' % (func.__name__, 1000*(end - begin)))
        return f  # 最后返回执行结果
    return wrapper


@metric
def fast(x, y):
    time.sleep(0.0012)  # 推迟调用线程的运行，单位为s
    return x+y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
