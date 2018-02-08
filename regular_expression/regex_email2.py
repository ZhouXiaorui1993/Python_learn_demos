#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 匹配Email的正则表达式，版本2：可以提取带名字的Email地址


import re


def name_of_email(addr):
    re_email = re.compile(r'(<?)([\w\s]*?)(>?)(\s?)([\w]+)@([\w]+)\.(com|org)$')
    re_match = re_email.match(addr)
    if not re_match:
        return '非合法Email地址'
    if re_match.group(2):
        return re_match.group(2)
    return re_match.group(5)
    # print(re_match.groups())

print(name_of_email('voyager.org'))
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')
