#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 正则表达式


import re

"""
test = '用户输入的字符串'
if re.match(r'正则表达式', test):
    print('ok')
else:
    print('failed')
"""

# 切分字符串
s = re.split(r'[\s,;]+', 'A,, B;;  C   D')
print(s)

# 分组(group)
# 除了简单地判断是否匹配之外，正则表达式还有提取子串的功能
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
# group(0)永远是原始字符串
print(m.group(0))
# group(1)、group(2)……表示第1、2、……个子串。
print(m.group(1))
print(m.group(2))
# groups()返回一个包含所有子串的tuple
print(m.groups())

# 贪婪匹配(默认状态下，匹配尽可能多的字符)
print(re.match(r'^(\d+)(0*)$', '123000').groups())
# 非贪婪匹配（尽可能少的匹配）
print(re.match(r'^(\d+?)(0*)$', '123000').groups())

# 当我们在Python中使用正则表达式时，re模块内部会干两件事
# 1.编译正则表达式，如果表达式的字符串本身不合法，会报错
# 2.用编译后的正则表达式去匹配字符串，
# 如果一个正则表达式要重复使用上千次，出于效率的考虑，我们可以预编译该正则表达式，接下来重复使用时就不需要编译这个步骤了，直接进行匹配
# 预编译
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# 使用
print(re_telephone.match('010-12345').groups())
