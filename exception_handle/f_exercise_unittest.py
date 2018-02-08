#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 对下面的Student类做单元测试


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if not isinstance(self.score, (int, float)):
            raise TypeError('score must be an number!')
        elif self.score > 100 or self.score < 0:
            raise ValueError('score must in 0~100')
        elif self.score >= 80:
            return 'A'
        elif self.score >= 60:
            return 'B'
        return 'C'

s1 = Student('Bart', 'ling')
# print(s1.get_grade())