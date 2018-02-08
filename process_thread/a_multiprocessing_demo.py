#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 由于Windows上没有fork调用，在windows上编写多进程程序需要用到Python提供的multiprocessing模块
# 下面是该模块的应用示例


from multiprocessing import Process
import os


# 子进程要执行的代码
def run_proc(name):
    print('Child process %s (%s) is running...' % (name, os.getpid()))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    # 创建子进程时，只需要传入一个执行函数和函数的参数
    # 首先创建一个Process实例
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    # 用start()方法启动子进程
    p.start()
    # join方法可以等待子进程运行结束后再继续往下执行，通常用于进程间的同步
    p.join()
    print('Child process end.')
