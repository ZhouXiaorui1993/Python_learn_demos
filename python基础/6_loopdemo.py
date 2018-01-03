#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#循环的一个demo
L = ['bart', 'lisa', 'adam']
print('下面是用for循环打印的')
for name in L:
	print(name)
print('下面是用while循环打印的')
i = 0
while i<len(L):
	print(L[i])
	i+=1
