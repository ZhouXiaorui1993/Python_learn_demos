#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# multiprocessing 模块中的Pool类，进程池可用来启动大量的子进程


from multiprocessing import Pool

import os
import time
import random


def long_time_task(name):
    print('Run task %s (id=%s) ...' % (name, os.getpid()))
    start = time.time()  # 启动时间
    time.sleep(random.random()*3)
    end = time.time()  # 结束时间
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    # Pool(n)表示最多同时执行几个进程，如果缺省，则他的默认值和电脑核数一致（我的电脑是4）
    p = Pool(5)
    # 利用进程池的方式创建4个子进程
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    # 调用join()方法之前必须要先调用close()方法，调用close之后就不能再继续添加新的Process了
    p.close()
    # 对Pool对象调用join()方法会等待所有子进程执行完毕
    p.join()
    print('All subprocesses done.')


