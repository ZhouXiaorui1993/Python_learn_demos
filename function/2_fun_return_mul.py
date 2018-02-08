#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 计算一个二元一次方程的解，函数返回两个值的demo

import math  # 为计算平方根调用math.sqrt()函数


def quadratic(a, b, c):

    d = b**2 - 4*a*c
    if d <= 0:
        return "方程无实数解"
    elif a == 0:
        return "二次项系数不为0，请检查后再输入！"
    else:
        x1 = (-b+math.sqrt(d))/(2*a)
        x2 = (-b-math.sqrt(d))/(2*a)
        return x1, x2


def main():
    print("二元一次方程为ax^2+bx+c=0，请输入对应的系数")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    x = quadratic(a, b, c)
    if not isinstance(x, tuple):
        print(x)
    else:
        print("方程的解为：\nx1 = %.2f\nx2 = %.2f" % x)

main()