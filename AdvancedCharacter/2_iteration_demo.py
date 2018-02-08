#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 使用迭代查找一个list中最小和最大值，并返回一个tuple


def find_min_and_max(l):
    if len(l) == 0:
        return None, None
    min_num = l[0]
    max_num = l[0]
    for num in l:
        if num<min_num:
            min_num = num
        if num>max_num:
            max_num = num
    return min_num, max_num
# 测试
if find_min_and_max([]) != (None, None):
    print('测试失败!')
elif find_min_and_max([7]) != (7, 7):
    print('测试失败!')
elif find_min_and_max([7, 1]) != (1, 7):
    print('测试失败!')
elif find_min_and_max([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')