#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 使用枚举类，以减少使用变量

from enum import Enum, unique


# 用下面的语句，会自动进行赋值，默认从1开始计数
# Gender = Enum('Gender', ('Male', 'Female'))

# 用下面的语句可以精确控制赋值（value）内容
@unique  # @unique装饰器可帮助我们检查是否有重复值
class Gender(Enum):  # Enum可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较
    Male = 0  # Male的value被设置为0
    Female = 1


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

# 测试
bart = Student('Bart Simpson', Gender.Male)
print(bart.gender)
print(Gender(1))  # 根据value来引用枚举变量
print(Gender.Female)  # 用成员名称引用枚举变量
for name, member in Gender.__members__.items():
    print('%s' % name + '=>' + '%s' % member + ':' + '%s' % member.value)
