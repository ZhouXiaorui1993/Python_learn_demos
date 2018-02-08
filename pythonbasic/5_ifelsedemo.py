#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 用if语句做条件判断的demo
#根据BIM指数判断其身体状况
name = input('请输入你的姓名：')
height = float(input('请输入你的身高（单位m）：'))
weight = float(input('请输入你的体重（单位kg）：'))
BIM = weight/(height**2)
print("%s的BIM值为：%.2f\n"%(name,BIM))
if 0<BIM<=18.5:
	print("体重过轻")
elif 18.5<BIM<=25:
	print("体重正常")
elif 25<BIM<=28:
	print("体重过重")
elif 28<BIM<=32:
	print("身体肥胖")
elif BIM>32:
	print("严重肥胖")
else:
	print("输入有误，请检查后重新输入！")
