#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 用asyncio提供的@asyncio.coroutine可以把一个generator标记为coroutine类型，然后在它
# 内部用yield from调用另一个coroutine实现异步操作

# 为了简化并更好地标识异步IO，从Python3.5引入了新的语法async和await，可以让coroutine代码更简洁易读

# 要使用新语法，只需要做两部简单的替换(必须对两者都进行替换)：
# 1. 把@asyncio.coroutine 替换为async
# 2. 把yield from替换为await

import threading
import asyncio


# 把一个generator标记成coroutine类型
async def hello():
    print('Hello world! (%s)' % threading.currentThread())
    # 异步调用asyncio.sleep(1)
    # yield from语法可以让我们方便地调用另一个generator，这里的r其实是生成器asyncio.sleep()发生StopIteration时的返回值
    # 把asyncio.sleep(1)看成是一个耗时1秒的IO操作，在此期间，主线程并未等待，而是去执行EventLoop中其他可以执行的coroutine了，因此可以实现并发执行。
    r = await asyncio.sleep(1)
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
