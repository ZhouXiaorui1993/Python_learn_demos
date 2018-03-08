#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# WSGI是一个接口，应用它，web开发者只需要实现一个函数，就可以响应HTTP请求。

# 看一个例子


def application(environ, start_response):
    """
    一个符合WSGI标准的HTTP处理函数，接收两个参数
    :param environ: 一个包含所有HTTP请求信息的dict对象
    :param start_response: 一个发送HTTP响应的函数
    :return: 作为HTTP响应的Body发送给浏览器
    """
    start_response('200 ok', [('Content-Type', 'text/html')])
    # body = '<h1>hello,%s</h1>' % (environ['PATH_INFO'][1:] or 'web')
    with open('hello2.html', 'r') as f:
        body = f.read()
    # print(environ)
    return [body.encode('utf-8')]

# 有了WSGI，我们需要关心的就是如何从environ这个对象中拿到HTTP请求信息，然后构造HTML，通过
# start_response()发送header，最后返回Body。
# 而application这个函数必须由WSGI服务器来调用。有很多符合WSGI规范的服务器，我们可以挑选一个来用。
# 现在使用Python内置的一个服务器（仅供开发测试使用）实现一下试试
# 见WSGI_server.py
