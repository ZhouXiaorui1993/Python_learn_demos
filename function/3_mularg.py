#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 利用可变参数计算一个或多个数的乘积


def product(*num):
    if len(num) == 0:
        raise TypeError('最少需要输入一个数')
    else:
        result = 1
        for n in num:
            result = result*n
        return result
line = input('please input numbers:')
n_str = line.split()  # 字符串的split()方法是通过指定分隔符对字符串进行切片。返回值为分割后的字符串列表
i = 0
n_int = []
for n in n_str:
    n_int.append(int(n))

print(product(*n_int))
