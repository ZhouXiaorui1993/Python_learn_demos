#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 我们已经了解了Python内置的urllib模块，用于访问网络资源。但是，它用起来比较麻烦，而且缺少很多实用的高级功能
# 更好的方案是使用requests，它是一个第三方库，处理url资源非常方便

import requests

# 通过get访问一个页面
r = requests.get('https://www.douban.com/')
# 查看响应码
print(r.status_code)
# 查看网页内容
# print(r.text)

# 对于带参数的URL，传入一个dict作为params参数
r2 = requests.get('https://www.douban.com/search', params={'q':'python','cat':'1001'})
# 实际请求的网址
print(r2.url)

# requests自动检测编码，可以使用encoding属性查看
print(r.encoding)

# 无论响应是文本还是二进制内容，我们都可以用content属性获得bytes对象
print(r.content)

# requests的方便之处还在于，对于特定类型的响应，例如JSON，可以直接获取
r3 = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20'
                  '%3D%202151330&format=json')
print(r3.json())

# 需要传入HTTPHeader时，我们传入一个dict作为headers的参数
r4 = requests.get('https://www.douban.com/', headers={'User-Agent': 'MOzilla/5.0 (iPhone; '
                                                                    'CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
# print(r4.text)

# 要发送Post请求，只需要将get()方法变为post()，然后传入data参数作为POST请求的数据
r5 = requests.post('https://accounts.douban.com/login', data={'form_email': '843786909@qq.com',
                    'form_password': '123456'})
# print(r5.text)

url = 'https://www.douban.com'
# requests默认使用application/x-www-form-urlencode对POST数据编码。如果要传递JSON数据，可以直接传入json参数
params = {'key': 'value'}
# 内部自动序列化为JSON
r6 = requests.post(url, json=params)

# 类似的，上传文件需要更复杂的编码方式，但是requests把它简化为files参数
# 在读取文件时，务必使用二进制模式读取，这样获取的bytes长度才是文件的长度
upload_files = {'file': open('report.xls', 'rb')}
r = requests.post(url, files=upload_files)

# 除了能轻松获取响应内容外，requests对获取http响应的其他信息也非常简单
# 例如获取响应头
print(r.headers)
print(r.headers['Content-Type'])

# requests对Cookies做了特殊处理，使得我们不必解析Cookie就可以轻松获取指定的Cookie
print(r.cookies['ts'])

# 要在请求中传入Cookie，只需准备一个dict传入cookies参数
cs = {'token': '12345', 'status': 'working'}
r7 = requests.get(url, cookies=cs)

# 最后，要指定超时，传入以秒为单位的timeout参数
r8 = requests.get(url, timeout=3)

