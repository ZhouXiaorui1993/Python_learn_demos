#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 利用@property给一个screen对象加上width和height属性，以及一个只读属性resolution


class Screen(object):

    @property
    def width(self):  # getter方法
        return self.__width

    @width.setter
    def width(self, value_w):  # setter方法
        if not isinstance(value_w, (float, int)):
            raise ValueError('width must be a float or integer!')
        if value_w < 0:
            raise ValueError('width must greater than zero!')
        self.__width = value_w

    @property
    def height(self):  # getter方法
        return self.__height

    @height.setter
    def height(self, value_h):  # setter方法
        if not isinstance(value_h, (float, int)):
            raise ValueError('height must be a float or integer!')
        if value_h < 0:
            raise ValueError('height must greater than zero!')
        self.__height = value_h

    @property
    def resolution(self):
        self.__resolution = self.__width * self.__height
        return self.__resolution
# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')