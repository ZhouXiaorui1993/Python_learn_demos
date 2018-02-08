#!/usr/bin/env python34
# -*- coding: utf-8 -*-
# 由于线程间数据共享时，若多个线程同时改变一个变量，则可能出现数据内容被改乱的情况
# 为避免这种错误，需要使用lock来锁住变量内容


import time, threading


# 假定balance为存款
balance = 0
# 定义一个锁
lock = threading.Lock()


def change_it(n):
    # 先存后取，结果应为0
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):

    for i in range(1000000):
        # 首先获取锁
        lock.acquire()
        try:
            # 改变量
            change_it(n)
        finally:
            # 改完后要释放锁
            lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
