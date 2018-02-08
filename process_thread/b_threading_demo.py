#!/usr/bin/env python34
# -*- coding: utf-8 -*-
# 使用threading模块实现多线程


import time, threading
import os


# 新线程要执行的代码
def loop():
    # current_thread()函数，永远返回当前线程的实例，主线程实例的name属性为MainThread，子线程的名字在创建时指定
    print('thread %s (id = %s) is running...' % (threading.current_thread().name, os.getpid()))
    n = 0
    while n < 5:
        n += 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

# 主线程要执行的代码
print('tread %s is running...' % threading.current_thread().name)
# 启动一个线程就是把一个函数传入，并创建Thread实例
t = threading.Thread(target=loop, name='LoopThread')  # 将子线程的名字指定为LoopThread
# 调用start()开始执行
t.start()
# 等待执行结束
t.join()
print('thread %s ended.' % threading.current_thread().name)