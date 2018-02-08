#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 使用匿名函数改造下面的代码


def is_odd(n):
    return n%2 == 1

L = list(filter(is_odd, range(1, 20)))
print("原函数输出：", L)

print("匿名函数输出", list(filter(lambda x: x%2 == 1, range(1, 20))))
