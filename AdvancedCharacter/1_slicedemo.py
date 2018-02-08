#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 利用切片操作，实现一个trim()函数,去除字符串首尾的空格


def trim(s):
    l_index = 0
    while l_index < len(s):
        if s[l_index] == ' ':
            l_index += 1
        else:
            break
    s = s[l_index:]
    r_index = len(s)
    while r_index > 0:
        if s[r_index-1] == ' ':
            r_index -= 1
        else:
            break
    s = s[:r_index]
    return s
# print(trim(input("请输入要去除空格的字符串:")))

''''以上为我自己编的程序，方法比较笨，下面为参考答案'''
# def trim(str):
#     if str == '':
#         return str
#     while str[:1] == ' ':
#         str = str[1:]
#     while str[-1:] == ' ':
#         str = str[:-1]
#     return str
# print(trim(input("请输入要去除空格的字符串:")))

# 测试程序:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
