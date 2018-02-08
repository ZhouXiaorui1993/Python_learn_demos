#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 匹配Email的正则表达式，版本1


import re


def is_valid_email(test):
    if re.match(r'^[\w\.]+\w*@\w+\.(com|org)$', test):
        return True

# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
assert is_valid_email('tom@voyager.org')
print('ok')
