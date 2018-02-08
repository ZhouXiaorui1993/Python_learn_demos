#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 教程中的一个例子：利用内置高阶函数filter()来求素数，方法是艾氏筛法。


def _int_iter():
    """先定义一个generator function，生成自然数序列（无穷序列）"""
    n = 1
    while True:
        n += 1
        yield n


def _not_divisible(n):
    """定义一个筛选函数，使用闭包可保证每次传入的n在单次循环中是固定的"""
    return lambda x: x % n > 0


def primes():
    """定义一个生成器，不断返回下一个素数"""
    it = _int_iter()
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        # it = filter(_not_divisible(n), it)  # 用闭包的方法，将n绑定到筛选函数
        it = filter(lambda x,n=n: x % n > 0, it)  # 用默认参数的方法定义时先绑定n，也可以得到正确的结果

count = 0
for i in primes():
    print(i)
    count += 1
    if count == 25:
        break
