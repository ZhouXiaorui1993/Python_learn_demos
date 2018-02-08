#!/usr/bin/env python3
# -*- coding: utf-8
# 利用os模块编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件

import os


# 较为繁琐的程序
# def search_special_file(s):
#     """
#     此函数可以在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件
#     并打印出其绝对路径
#     """
#     now_path = os.path.abspath('.')  # 获得当前目录的绝对路径
#     l = [t for t in os.walk(now_path)]  # l的每一项都是一个包含三个元素（dirpath，dirname，filename）的tuple
#     for i in range(len(l)):
#         if l[i][2]:
#             for n in range(len(l[i][2])):
#                 filename = os.path.splitext(l[i][2][n])[0]
#                 if s in filename:
#                     print(l[i][2][n])
#                     print(r"it's absolute path is %s" % l[i][0])


# 改进后的程序
def search_file(s):
    for dirpath, dirnames, filenames in os.walk('.'):
        for file in filenames:
            no_extension_name = os.path.splitext(file)[0]
            if s in no_extension_name:
                print(file)
                print(r"it's absolute path is: '%s'" % os.path.abspath(os.path.join(dirpath, file)))


def main():
    s = input('请输入指定字符串：')
    print('\n',r"包含字符串'%s'的文件有：" % s, sep='')
    search_file(s)

main()
