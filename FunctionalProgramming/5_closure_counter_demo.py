#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 利用闭包返回一个计时器函数，每次调用它返回递增整数


# def create_counter():
#     """方法1:使用nonlocal关键字"""
#     n = 0
#
#     def counter():
#         nonlocal n
#         n = n+1
#         return n
#     return counter


# def create_counter():
#     """方法2：使用生成器"""
#     def f():
#         """先创建一个生成器"""
#         n = 0
#         while True:
#             n = n+1
#             yield n
#     g = f() # 生成器
#
#     def counter():
#         return next(g)
#     return counter

def create_counter():
    """使用列表，列表是全局变量"""
    fn = [0]

    def counter():
        fn[0] = fn[0]+1
        return fn[0]
    return counter

# 测试代码
counterA = create_counter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = create_counter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')