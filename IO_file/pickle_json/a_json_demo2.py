#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 将Python对象（class实例）序列化为json对象，以便在不同的编程语言之间传递


import json


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Hiro', 17, 88)


# 为将class实例对象序列化为JSON文件，需要先定义一个转换函数，将实例转换为一个dict
def student2dict(std):
    return {
        'name':std.name,
        'age':std.age,
        'score':std.score
    }

print("转换后的json内容为：")
print(json.dumps(s, default=student2dict))

# 但这样一来，如果下次遇到其他class的实例对象便需要重新写转换函数，下面有一个偷懒的方法
print("\n第二种转换方法得到的结果：")
s_json = json.dumps(s, default=lambda obj: obj.__dict__)
print(s_json)
# 因为通常的class实例都会有一个__dict__属性，他就是一个dict，用来存储实例变量。
# 但也有少数例外，比如定义了__slots__的class。注：变量__slots__是用来限制给实例添加的属性的


# 同理，反序列化也需要先定义一个函数
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
print("\n反序列化为：")
print(json.loads(s_json, object_hook=dict2student))


# 对中文的序列化
print("\n对中文序列化示例：")
print('case 1: ensure_ascii=True')
obj = dict(name='小明', age=23)
s = json.dumps(obj, ensure_ascii=True)
print(s)
print('case 2: ensure_ascii=False')
s2 = json.dumps(obj, ensure_ascii=False)
print(s2)