#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 断言（assert）用法示例


def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'  # assert的意思是其后的表达式应该是True，否则根据程序运行逻辑，后面的代码肯定会出错
    return 10 / n


def main():
    foo('0')

main()