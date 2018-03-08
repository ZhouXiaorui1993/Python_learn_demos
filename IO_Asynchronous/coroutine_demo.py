#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 协程，又称微线程，纤程。英文名：Coroutine
# 协程看上去类似子程序，但执行过程和子程序不同。子程序调用只有一个入口，调用顺序是明确的。
# 但协程在执行过程中，在子程序内部可以中断，然后转而去执行其他的子程序，在适当的时候再返回来接着执行。

# 协程最大的优势是执行效率极高，因为子程序切换不是线程切换，而是由程序自身控制的。所以和多线程相比，线
# 程数量越多，协程的优势就越明显。
# 同时为了利用多核CPU，最简单的方法是多进程＋协程，既充分利用多核，又充分发挥协程的效率，可获得极高的性能。

# Python对协程的支持是通过Generator实现的。
# 在generator中，我们不但可以通过for循环来迭代，还可以不断调用next()函数获取由yield语句返回的下一个值。
# 但是Python中的yield不但可以返回一个值，它还可以接收调用者发出的参数。

# Python还有一个send方法
# send方法和next方法唯一的区别是在执行send方法会首先把上一次挂起的yield语句的返回值通过参数设定
# （如send(4)，即设定返回值为4，若send方法参数为None时，他与next方法完全等价）
# 从而实现与生成器方法的交互
# 但是需要注意的是，在一个生成器对象没有执行next()方法之前，由于没有yield语句被挂起，所以执行send方法会报错

# 一个例子
# 传统的生产者-消费者模型是一个线程写消息，一个线程取消息，通过锁机制控制队列和等待，但一不小心就可能死锁。
# 如果改用协程，生产者生产消息后，直接通过yield跳转到消费者开始执行，待消费者执行完毕后，切换回生产者继续生产，效率极高：


def consumer():
    r = ''
    while True:
        n = yield r  # n由send方法传递
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    c.send(None)  # c.send(None)等价于next(c),首先调用它启动生成器
    n = 0
    while n < 5:
        n = n+1
        print('[PROCEDURE] Producing %s...' % n)
        # 将参数n设定为上一次挂起的yield语句的返回值，切换到consumer执行
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    # 生成器的close方法会在生成器对象方法的挂起处抛出一个GeneratorExit异常
    # GeneratorExit异常产生后，系统会继续把生成器对象方法后续的代码执行完毕
    c.close() # produce要退出生产，通过c.close()关闭consumer，整个过程结束

c = consumer()
produce(c)

# 可以看出，整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以
# 称为“协程”，而非线程的抢占式完成任务。
