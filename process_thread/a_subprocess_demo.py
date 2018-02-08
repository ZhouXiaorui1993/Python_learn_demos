#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 有时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后还需要控制其输入和输出。
# subprocess模块可以让我们非常方便的启动一个子进程，然后控制其输入和输出
# 连接到stdin、stdout、strerr管道并获取它们的返回码


import subprocess

# call()方法用来执行一些命令行的命令，启动一个子进程去执行，等待子进程执行结束后才继续执行后续代码
# args参数由字符串形式提供，且只有一个命令参数时，无需shell=True参数
print('$ ls')
r0 = subprocess.call('ls')
print('Exit code r0:', r0)
# args参数由字符串形式提供，且有多个命令参数时，需提供shell=True参数
print('$ ls -l')
r1 = subprocess.call('ls -l', shell=True)
print('Exit code r1:', r1)

# args参数通过列表形式提供时，不需要提供shell=True参数
print('$ nsloookup www.python.org')
r2 = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code r2:', r2)

# subprocess.Popen使用：输出到管道
pipe = subprocess.Popen('ls -lh', shell=True, stdout=subprocess.PIPE)
with open('test_ls.txt', 'wb') as f:
    f.write(pipe.stdout.read())
