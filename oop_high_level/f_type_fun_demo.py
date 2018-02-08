#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 使用type函数创建一个class

"""
要创建一个class对象，type()函数依次传入3个参数：

    class的名称；
    继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
    class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
"""


def init_fun(self, name):
    self.name = name


def hello_name(self):
    print('hello, %s' % self.name)

Student = type('Student', (object,), dict(__init__=init_fun, hello=hello_name ))
hiro = Student('Kunimi Hiro')
hiro.hello()
