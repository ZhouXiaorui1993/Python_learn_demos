#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 利用map()函数，将用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。


def normalize(name):  # 第一种没有用到字符串内建方法`title()`
    l_name = list(name)
    if ord(l_name[0]) >= 97:
        l_name[0] = chr(ord(name[0])-32)
    for i in range(1, len(l_name)):
        if ord(l_name[i]) <= 90:
            l_name[i] = chr(ord(l_name[i])+32)
    normal_name = "".join(l_name)
    return normal_name


def normalize2(name):  # 第二种用到字符串内建方法`title()`
    return name.title()

s = input('请输入姓名以空格隔开：')
l = s.split()
#L1 = ['adam', 'LISA', 'barT']
print(list(map(normalize, l)))
print(list(map(normalize2, l)))
