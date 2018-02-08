#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# try..except..finally应用示例


try:  # 先尝试执行try语句块，如有错误，则跳转至except语句块
    print('try...')
    a = float(input('输入被除数：'))
    r = 10/a
    print('result of 10/%s:' % a, r)
except ValueError as e:
    print('发生ValueError:', e)
except ZeroDivisionError as e:  # 错误处理语句
    print('发生ZeroDivisionError:', e)
else:  # except语句后可跟一个else语句（也可没有），当没有错误发生时，其缩进块中的语句会被自动执行
    print('没有错误发生！')
finally:  # 无论是否有错误发生，都会执行的语句
    print('finally...')
print('End')