#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 递归函数实现汉诺塔的移动demo


def move(n, a, b, c):
    global COUNT
    if n == 1:
        COUNT += 1
        print(a, '-->', c,COUNT)
    else:
        move(n-1, a, c, b)  # 先借助c将n-1个盘子移动到b
        COUNT += 1
        print(a, '-->', c, COUNT)  # 再将最大的盘子从a移动到c
        move(n-1, b, a, c)  # 再将b上的n-1个盘子借助a移动到c
COUNT = 0  # 初始移动次数为0
move(3, 'A', 'B', 'C')




