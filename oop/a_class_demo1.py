#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 定义一个class对象


class Student(object):

    # 可以在创建实例时，把一些我们认为必须绑定的属性强制填写进去
    def __init__(self, name, score):  # __init__方法的第一个参数永远是self，表示创建的实例本身，
        # 因此，在__init__方法内部，就可以将各种属性绑定到self，因为self就指向创建的实例本身
        self.name = name
        self.score = score

    def print_info(self):  # 定义一个类的方法，除了其第一个参数是self之外，其他和普通函数一样。
        # 要调用一个方法，只需要在实例变量上直接调用，除了self不用传递，其他参数正常传入。
        print(self.name, ':', self.score)

bart = Student('Bart Simpson', 29)
hiro = Student('Kunimi Hiro', 80)
hiro.print_info()
print(bart.name)