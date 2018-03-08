#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# WSGI_hello.py实现了web应用程序的处理函数
# 本程序负责启动WSGI服务器

# 从wsgiref模块导入
from wsgiref.simple_server import make_server
# 导入我们自己编写的处理函数
from WSGI_hello import application

# 创建一个服务器，IP地址为空，端口为8000，处理函数为application
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求
httpd.serve_forever()
