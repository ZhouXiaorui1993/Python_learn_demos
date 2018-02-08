#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 利用Queue实现进程间通信


from multiprocessing import Process, Queue
import os
import time
import random


# 写数据的进程
def write_data(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())


# 读数据
def read_data(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)


if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程
    q = Queue()
    pw = Process(target=write_data, args=(q,))
    pr = Process(target=read_data, args=(q,))
    # 启动子进程pw，写入数据
    pw.start()
    # 启动子进程pr，读取数据
    pr.start()
    # 等待pw结束
    pw.join()
    # pr里面是死循环，无法等待其结束，只能强行终止
    pr.terminate()
