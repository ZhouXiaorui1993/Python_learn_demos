#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 利用列表生成式，将既包含字符串又包含整数的list中所有字符串变为小写


def ls_to_low(l):
    return [s.lower() for s in l if isinstance(s, str)]

L = ['Tatsuya', 'HIro', '16', 'HideO']
print(ls_to_low(L))