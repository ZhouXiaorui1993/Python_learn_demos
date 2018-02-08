#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 写一个死循环，观察CPU的占用率


import threading, multiprocessing


def loop():
    x = 0
    while True:
        x = x*1


# 启动与CPU核心数量相同的N个线程
for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()

# 用top命令查看当前的cpu使用情况，可以看出四核cpu占用率仅101%，也就是仅使用了一核
# 但是用c或JAVA来改写相同的死循环，直接可以把全部核心跑满，到400%.
# 这是由于Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global Interpreter Lock
# 任何Python线程执行前，必须先获得GIL锁，然后每执行100条代码，解释器就自动释放GIL锁，让别的线程有机会执行。
# 这个GIL实际上把所有的线程执行代码都给上了锁，所以多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。
# 所以，在Python中，可以使用多线程，但不要指望能有效利用多核。
