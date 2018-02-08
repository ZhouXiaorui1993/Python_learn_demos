#!/usr/bin/rnv python3
# -*- coding: utf-8 -*-
# 使用@property装饰器将一个方法变为属性来调用


class Student(object):

    @property  # 把一个getter方法变成属性，只需要加上@property即可
    def score(self):
        return self.__score

    @score.setter  # @score.setter装饰器是由@property创建的，负责把一个setter方法变为属性
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self.__score = value
    # 还可以只利用@property定义getter方法，不定义setter方法，得到一个只读属性

    @property
    def mark(self):
        if 0 < self.__score < 60:
            self.__mark = 'C'
        elif self.score < 80:
            self.__mark = 'B'
        else:
            self.__mark = 'A'
        return self.__mark

s = Student()
s.score = 60
print(s.score)
print(s.mark)