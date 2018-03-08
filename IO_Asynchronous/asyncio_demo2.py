#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 我们用asynico的异步网络来连接获取sina、sohu和163的网站首页

import asyncio


@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()  # drain方法用于在数据量较大时，刷新缓存区
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()
# asyncio.get_event_loop方法可以创建一个事件循环
loop = asyncio.get_event_loop()
# 使用run_until_complete将协程注册到事件循环，并启动事件循环
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
# 可见3个连接由一个线程通过coroutine并发完成。
