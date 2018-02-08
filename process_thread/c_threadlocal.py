#!/usr/bin/env python34
# -*- coding: utf-8 -*-
# 在多线程环境中，由于使用全局变量必须加锁，而使用局部变量在函数调用时，传递起来非常麻烦
# 所以ThreadLocal应运而生，来解决这一问题


import threading


# 创建全局ThreadLocal对象
local_school = threading.local()


def process_student():
    # 获取当前线程关联的student
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))


def process_thread(name):
    print('%s is running...' % threading.current_thread().name)
    # 绑定ThreadLocal的student
    local_school.student = name
    process_student()
    print('%s ended.' % threading.current_thread().name)

print('%s is running...' % threading.current_thread().name)
# 创建线程
t1 = threading.Thread(target=process_thread, args=('Hiro',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Hideo', ), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
print('%s ended.' % threading.current_thread().name)

# 注：ThreadLocal最常用的地方就是为每个线程绑定一个数据库链接，HTTP请求，用户身份信息等
# 这样一个线程的所有调用到的处理函数都可以非常方便的访问这些资源
