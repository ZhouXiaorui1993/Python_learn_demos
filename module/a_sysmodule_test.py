#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 以内建sys模块为例，编写一个标准的模块


'a test module-sys'  # 这是模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释

__author__ = 'Kunimi Hiro'


import sys


def test_sys():
	args = sys.argv  # sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称
	if len(args) == 1:
		print("你只输入了文件名称来运行它，没有附加额外的参数，如果想了解所有参数，请加入'--help'来获取详细信息") 
	elif args[1] == '--help':
		print('''以下是帮助信息：
选项'-n':打印作者名称；
选项'-c':打印作者在看的漫画''')
	elif args[1] == '-n':
		print('author is %s'% __author__)
	elif args[1] == '-c':
		print('cross game by atachi')
	else:
		print('too many arguments!')


if __name__ == '__main__':  # 直接运行此文件时会执行下面的语句，若是被导入的则不会执行下面的语句
	print('你直接运行了这个文件')
	test_sys()
