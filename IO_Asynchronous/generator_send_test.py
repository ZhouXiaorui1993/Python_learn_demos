#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Generator的send方法，小测试


def my_generator():
    value = yield 1
    value = yield value


gen = my_generator()
print(next(gen))
print(gen.send(2))
# 生成器的close方法会在生成器对象方法的挂起处抛出一个GeneratorExit异常
# GeneratorExit异常产生后，系统会继续把生成器对象方法后续的代码执行完毕
gen.close()
print('end.')
