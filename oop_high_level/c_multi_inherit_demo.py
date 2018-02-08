#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 多重继承的例子


class Animal(object):
    pass

# 能飞和能跑
class Runnable(object):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying...')

# 大类：哺乳类和鸟类
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

# 各种动物
class Dog(Mammal, Runnable):  # Dog既是哺乳动物，又可以跑
    pass

class Parrot(Bird, Flyable):
    pass

class Ostrich(Bird, Runnable):
    pass

class bat(Mammal, Flyable):
    pass
