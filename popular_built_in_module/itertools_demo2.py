#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 利用itertools模块，计算圆周率（通过计算序列的前n项和）


import itertools


def cal_pi(N):
    """
    step1: 创建一个奇数序列：1， 3， 5， 7， 9...
    step2： 取该序列的前n项： 1, 3, 5,..., 2*N-1
    step3: 添加正负号并用4除： 4/1, -4/3, 4/5, -4/7, ...
    step4: 求和
    """
    # 创建一个奇数序列
    odd = itertools.count(1, 2)
    pos_neg = itertools.cycle([4, -4])
    return sum(next(pos_neg)/next(odd) for i in range(N)) # sum可以直接作用于一个生成器

print(cal_pi(10000000))

