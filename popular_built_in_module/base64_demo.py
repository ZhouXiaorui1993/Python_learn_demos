#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# base64模块使用示例

import base64

# 用记事本打开exe、jpg、pdf等文件时，经常会看到一堆乱码。这时因为二进制文件包含很多无法显示和打印的字符
# 所以，如果要让记事本这样的文本处理软件能处理二进制数据源，就需要一个二进制到字符串的转换方法
# Base64是一种最常见的二进制编码方法
# Base64会把3字节的二进制数据编码为4字节的文本数据，长度增加33%，好处是编码后的文本数据可以在邮件正文、网页等直接显示
# 如果要编码的二进制数据不是3的倍数，Base64会用\x00字节在末尾补足后，再在编码的末尾加上1个或2个=号，表示补了多少字节，解码时会自动去掉
import base64
be = base64.b64encode(b'binary\x00string')
print(be)
print(len(be))
bd = base64.b64decode(be)
print(bd)

# 由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_
be2 = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(be2)
bue2 = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(bue2)
bud2 = base64.urlsafe_b64decode(bue2)
print(bud2)

# 总结：Base64是一种任意二进制到文本字符串的编码方法，常用于在URL、Cookie、网页中传输少量二进制数据
