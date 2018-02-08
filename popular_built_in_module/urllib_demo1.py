#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# urllib提供了一系列用于操作URL的功能

# urllib的request模块可以非常方便的抓取URL内容，也就是发送一个get请求到指定页面，然后返回HTTP的响应
# 例如，对豆瓣的一个url进行抓取，并返回响应
from urllib import request


with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()
    # status属性表示HTTP状态响应码，返回200表示请求被正常处理；reason是HTTP响应短语，如果没有指定，则使用默认响应短语
    print('Status:', f.status, f.reason)
    # 打印get后的headers（响应报头）
    for k,v in f.getheaders():
        print('%s: %s' % (k,v))
    # 打印url内容
    print('Data:', data.decode('utf-8'))

# 如果我们要模拟浏览器发送get请求，就需要使用Request对象，通过它添加HTTP请求头，我们就可以把请求伪装成浏览器。
# 例如，模拟iPhone6去请求豆瓣首页，
req = request.Request('http://www.douban.com/')
# user-agent中文名为用户代理，它是一个特殊的字符串头，向访问网站提供你所使用的浏览器类型及版本、操作系统及版本、
# 浏览器内核等信息的标识，通过这个标识，所访问的网站可以根据不同的浏览器显示不同的排版，以提供更好的用户体验。
# UA可以进行伪装
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f2:
    print('Status:', f2.status, f2.reason)
    for k, v in f2.getheaders():
        print('%s: %s' % (k, v))
    # 这样豆瓣会返回适合iPhone的移动版网页
    print('Data of douban:', f2.read().decode('utf-8'))

# 如果要以Post发送一个请求，只需要把data参数以bytes形式传入
# 我们模拟一个微博登录，先读取登录的邮箱和口令，然后按照weibo.cn的登录页的格式，以username=xxx&password=xxx的编码传入
from urllib import parse

print('Login to weibo.cn...')
email = input('Email: ')
passwd = input('Password: ')
login_data = parse.urlencode([
    ('username', email),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req2 = request.Request('https://passport.weibo.cn/sso/login')
req2.add_header('Origin', 'https://passport.weibo.cn')
req2.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req2.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req2, data=login_data.encode('utf-8')) as f3:
    print('Status:', f3.status, f3.reason)
    for k, v in f3.getheaders():
        print('%s: %s' % (k, v))
    print('Data of weibo:', f3.read().decode('utf-8'))



