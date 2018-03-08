#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 对应demo2的客户端程序

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
s.connect(('127.0.0.1', 9999))  # 本机ip，端口9999
# 接收欢迎消息
print(s.recv(1024).decode('utf-8'))
for data in [b'hanyu', b'tatsuya', b'minami']:
    # 发送数据
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()
