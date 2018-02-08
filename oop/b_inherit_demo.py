#!usr/bin/env python3
# -*- coding: utf-8 -*-
# 继承和多态


class Plant(object):  # 父类
    def __init__(self, color):
        self.color = color

    def print_info(self):
        print("This is a %s plant" % self.color)


class Tree(Plant):  # Plant的子类
    def __init__(self, height, age, color='green'):
        # Plant.__init__(self, color)  # 在子类中调用父类的属性--方法一
        super().__init__(color)  # 在子类中调用父类属性--方法二
        self.height = height
        self.age = age

    def print_info(self):
        print('This is a %s tree, age %s, height %s' % (self.color, self.age, self.height))


def farm(plant):  # 函数接收一个Plant类型的参数，或者说接收一个拥有print_info()方法的参数
    return plant.print_info()

farm(Plant('yellow'))
farm(Tree('30m', 100))
