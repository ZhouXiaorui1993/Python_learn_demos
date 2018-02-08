#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 使用sorted()函数对列表按名字排序


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0]

L2 = sorted(L, key=by_name)
print("by name:",L2)

print("by score(high to low):")
print(sorted(L, key=lambda x: x[1], reverse=True))
