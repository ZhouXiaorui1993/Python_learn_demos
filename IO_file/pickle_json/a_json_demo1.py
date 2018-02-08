#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 将Python对象序列化为json对象，以便在不同的编程语言之间传递


import json


d = dict(name='Bob', age=30, marry_state=True)
with open('bob.json', 'w') as f:
    json.dump(d, f)  # 序列化为json对象并写入文件

print("将Python对象序列化为json文件：")
with open('./bob.json', 'r') as f:
    print(f.read())

print("将json文件反序列化为Python对象：")
with open('./bob.json', 'r') as f:
    d = json.load(f)
    print(d)

