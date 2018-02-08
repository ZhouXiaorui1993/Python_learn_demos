#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
from functools import reduce


def str2float(s):
    point_index = s.find('.')
    p1 = reduce(fn, map(chr2num, s[:point_index]))
    # 可以用lambda函数简化为： p1 = reduce(lambda x,y: x*10+y, map(chr2num, s[:point_index])
    p2 = 10**(-point_index)*reduce(fn, map(chr2num, s[point_index+1:]))
    return p1+p2


def chr2num(c):
    d = {'0': 0, '1': 1, '2': 2, '3':3, '4': 4, '5': 5,
         '6': 6, '7': 7, '8': 8, '9': 9}
    return d[c]


def fn(x, y):
    return x*10+y

# 测试代码
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')