#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# hashilib模块使用示例

# Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等。
# 所谓摘要算法，又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个固定长度的数据串（通常用16进制的字符串表示）
# 摘要算法就是通过摘要函数f()对任意长度的数据data计算出固定长度的摘要digest，目的是为了发现原始数据是否被人篡改过。


import hashlib


# 我们以常见的摘要算法MD5为例，计算出一个字符串的MD5值
md5 = hashlib.md5()
md5.update('How to use md5 in python hashlib?'.encode('utf-8'))
# MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示。
print(md5.hexdigest())
# 如果数据量很大，可以分块调用update()，最后计算出的结果是一样的
md5_test2 = hashlib.md5()
md5_test2.update('How to use md5 '.encode('utf-8'))
md5_test2.update('in python hashlib?'.encode('utf-8'))
print(md5_test2.hexdigest())
# 如果改动了一个字母，则计算出的结果会完全不同
md5_test2.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5_test2.hexdigest())

# 另一种常见的摘要算法是SHA1，调用SHA1和调用MD5完全类似
sha1_test = hashlib.sha1()
sha1_test.update('how to use sha1 in python hashlib?'.encode('utf-8'))
# SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示
print(sha1_test.hexdigest())
# 比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法不仅越慢，而且摘要长度更长。
