#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# class中的某些属性定义为私有变量，防止外部更改


class Student():
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def print_info(self):
        print('%s: %s' % (self.name, self.__gender))

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        # if gender == 'male' or gender == 'female':  # 改为下面的语句更好
        if gender in ('male', 'female'):
            self.__gender = gender
        else:
            raise ValueError("性别为'male' 或 'female', 请检查后再输入！")
# 测试代码
bart = Student('Bart', 'male')
bart.set_gender('emale')
print(bart.get_gender())
