#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 如果在前一个demo的基础上，还需要更复杂的控制，比如使用代理服务器来访问一个网站
# 则需要利用ProxyHandler来处理，示例代码如下：

from urllib import request

proxy_handler = request.ProxyHandler({'http':'http://www.example.com:3128/'})
proxy_auth_handler = request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
opener = request.build_opener(proxy_handler, proxy_auth_handler)
with opener.open('http://www.example.com/login.html') as f:
    pass
