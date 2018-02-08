#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 为Student类增加一个类属性，每创建一个类，该属性自动增加


class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1  # 通过 Student.count来设置类属性的值

# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')