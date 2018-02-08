#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 一些特殊变量和函数的用法


# __str__
class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):  # __str__()返回的是用户看到的字符串
        return 'Student object (name: %s)' % self.name
    __repr__ = __str__  # __repr__()返回的是程序开发者看到的字符串，如果在交互式环境中直接运行变量，就会看到它的返回值

    def __getattr__(self, attr):  # 在寻找某不存在的属性时，Python会自动调用__getattr__()方法。
        if attr == 'score':
            return 99
        raise AttributeError('Student object不存在属性%s' % attr)

    def __call__(self, *args, **kwargs):  # 任何类,只需要定义一个__call__()方法,就可以直接对实例进行调用
        print('你直接调用了name属性为%s的实例哦！' % self.name)
print('__str__的测试结果：')
print(Student('Hiro'))

print('__call__的测试结果：')
s = Student('Hikari')
s()

print('__getattr__的测试结果：')
print(s.score)
# print(s.age)


# __iter__
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a, b

    def __iter__(self):  # 若一个类想被用于for循环，必须有一个__iter__()方法，返回一个迭代对象
        return self

    def __next__(self):  # Python的for循会不断调用该迭代对象的__next__()方法拿到循环的下一个值
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100:
            raise StopIteration()
        return self.a

    # 虽然利用__iter__可使Fib实例作用于for循环，但不能像list一样按照下标取元素
    # 要实现这一功能，需要实现__getitem__()方法
    def __getitem__(self, n):
        a, b = 1, 1
        if isinstance(n, int):
            for x in range(n):
                a, b = b, a+b
            return a
        if isinstance(n, slice):  # 实现简单的切片功能
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            l = []
            for x in range(stop):
                if x >= start:
                    l.append(a)
                a, b = b, a+b
            return l
print('以下是__iter__的用法示例(打印斐波那契数列)：')
for n in Fib():
    print(n)

print('以下为__getitem__的用法示例：')
f = Fib()
print('f[3] = %s' % f[3])
print('f[:3] = ',f[:3], sep='')
print('f[3:10] = ',f[3:10], sep='')
