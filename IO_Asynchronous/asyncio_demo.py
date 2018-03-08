#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# asyncio是Python3.4版本引入的标准库，直接内置了对异步IO的支持
# asynico的编程模型就是一个消息循环，我们从asynico模块中直接取出一个EventLoop的引用，
# 然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO

# 用asynico实现hello,world代码如下
import threading
import asyncio


@asyncio.coroutine  # 把一个generator标记成coroutine类型
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    # 异步调用asyncio.sleep(1)
    # yield from语法可以让我们方便地调用另一个generator，这里的r其实是生成器asyncio.sleep()发生StopIteration时的返回值
    # 把asyncio.sleep(1)看成是一个耗时1秒的IO操作，在此期间，主线程并未等待，而是去执行EventLoop中其他可以执行的coroutine了，因此可以实现并发执行。
    r = yield from asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())

# 获取EventLoop
loop = asyncio.get_event_loop()
# 用task封装两个coroutine
tasks = [hello(), hello()]
# 执行coroutine
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

# 由打印的当前线程名称可以看出，两个coroutine是由同一个线程并发执行的。

# 如果把asyncio.sleep()换成真正的IO操作，则多个coroutine就可以由一个线程并发执行。
