#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 格式化输出demo
name = input("please enter your name:")
print("please enter your score of last year:")
s1 = int(input())
print("please enter your score of this year:")
s2 = int(input())
if s2>=s1:
	print('score of %s have been raised by %.2f%%'%(name,100*(s2-s1)/s1))#%.2f表示浮点数类型保留两位小数输出
else:
	print('score of %s have been dropped by %.2f%%'%(name,100*(s1-s2)/s1))
