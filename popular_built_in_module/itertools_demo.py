#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数

import itertools

# 首先，我们看看itertools提供的几个无限迭代器
# count()会创建一个无限迭代器
natuals = itertools.count(1)
# 打印出自然数序列，只能强制停止运行
# for n in natuals:
#     print(n)

# cycle()会把传入的一个序列无限重复下去
cs = itertools.cycle('ABCD') # 字符串也是序列的一种
# 无限重复打印ABCD
# for c in cs:
#     print(c)

# repeat()可以将一个元素无限重复下去，但如果提供了第二个参数就可以限定重复次数
ns = itertools.repeat('abc', 4)
for n in ns:
    print(n)

# 无限序列虽然可以无限迭代下去，但通常我们会通过takewhile()等函数根据条件来截取出一个有限的序列
ns2 = itertools.takewhile(lambda x: x < 10, natuals)
print(list(ns2))

# chain()函数可以把一组迭代对象串联起来，形成一个更大的迭代器
for c in itertools.chain('ABC', ['x', 'y', 'z']):
    print(c)

# groupby()把迭代器中相邻的重复元素挑出来放在一起：
for key, group in itertools.groupby('AAAABBBBCCCDDDDDD'):
    print(key, list(group))

