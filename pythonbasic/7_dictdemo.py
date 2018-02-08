#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#dict使用的小demo
#通过学号查找姓名
d = {1:'zhou', 2:'bart', 3:'gemini', 4:'minami'}
n =int(input('请输入学号：'))
if n in d:
	print('%d号对应的学生姓名为%s：'%(n,d[n]))
else:
	print('查无此号')

