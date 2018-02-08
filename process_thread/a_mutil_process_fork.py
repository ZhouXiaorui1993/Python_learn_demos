#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# fork()的应用示例，注意Windows上没有fork()调用
# fork()调用一次，返回两次，操作系统自动把当前进程


import os


print('Process (%s) is start...' % os.getpid())  # 原进程
pid = os.fork()  # fork出两个进程
if pid == 0:  # 返回0的是子进程
    print('i am child process (%s) and my parent is %s' %(os.getpid(), os.getppid()))  # 子进程调用getppid()拿到父进程的id
else:
    print('I am (%s) and I just created a child process (%s).' % (os.getpid(), pid))  # 父进程返回子进程的ID

