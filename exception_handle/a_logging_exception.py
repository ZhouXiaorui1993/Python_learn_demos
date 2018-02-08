#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 使用logging模块记录错误信息

import logging


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s)/2


def main():
    try:
        bar('0')
    except Exception as e:  # Exception类中包含了大多数错误类型
        logging.exception("发生了异常!")

main()
print('执行完毕')  # 如果“END”打印了，则表面记录了错误，并继续执行了程序
