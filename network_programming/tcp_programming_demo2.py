#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 和客户端编程相比，服务器编程要复杂一些
# 服务器进程首先要绑定一个端口并监听来自其他客户端的连接。如果某个客户端连接过来了，服务器就与该客户端建立socket连接，随后的通信就靠这个连接了

# 所以服务器会打开固定端口（比如80）来监听，每来一个客户端连接，就创建该Socket连接。由于服务器会有大量来自客户端的连接，
# 所以，服务器要能够区分一个Socket连接是和哪个客户端绑定的。一个Socket依赖4项：服务器地址、服务器端口、客户端地址、客户端端口来唯一确定一个Scoket。

# 但是服务器还需要同时响应多个客户端的请求，所以每个连接都需要一个新的线程或新的进程来处理，否则，服务器一次就只能服务一个客户端了。

# 下面编写一个简单的服务器程序，它接收客户端连接，把客户端发过来的字符加上Hello再发回去。
import socket
import threading
import time

# 首先，创建一个基于IPv4和TCP的Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 然后，我们要绑定监听的地址和端口。服务器可能有多块网卡，可以绑定到某一块网卡的IP地址上，也可以用0.0.0.0绑定到所有的网络地址，
# 还可以用127.0.0.1（特殊的IP地址，表示本机地址，如果绑定到这个地址，客户端必须同时在本机运行才能连接，即外部的计算机无法连接进来）绑定到本机地址。
# 端口号需要预先指定。因为我们写的不是标准服务，所以选则了9999这个端口号。
# 监听端口
s.bind(('127.0.0.1', 9999))

# 紧接着，调用listen()方法开始监听端口，传入的参数指定等待连接的最大数量：
s.listen(5)
print('Waiting for connection...')


# 每个连接必须创建新线程（或进程）来处理，否则，单线程在处理连接的过程中无法接受其他客户端的连接
def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    # 连接建立后，服务器首先发一条欢迎消息
    sock.send(b'Welcome')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        # 如果接收完毕或客户端发送了exit字符串，就关闭连接
        if not data or data.decode('utf-8') == 'exit':
            break
        # 然后等待客户端数据，并加上Hello再发送给客户端。
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

# 接下来，服务器程序通过一个永久循环来接受来自客户端的连接，accept()会等待并返回一个客户端的连接
while True:
    # 接受一个新连接
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()

# 要测试该服务器程序，就需要再编写一个客户端程序，见tcp_programming_demo3.py





