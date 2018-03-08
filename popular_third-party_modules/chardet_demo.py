#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 字符串编码一直是令人非常头疼的问题，尤其是我们在处理一些不规范的第三方网页的时候。
# 虽然Python提供了Unicode表示的str和bytes两种数据类型，并且可以通过encode()和decode()方法转换，
#　但是，在不知道编码的情况下，对ｂｙｔｅｓ和ｄｅｃｏｄｅ()不好做

# 对于未知的bytes，要把它转换成str，需要先“猜测”编码。猜测的方式是先收集各种编码的特征字符，根据特征字符判断，就有很大概率猜对
# 而chardet库就是用来检测编码的，简单易用

import chardet

# 当我们拿到一个bytes时，就可以对其检测编码。
# confidence字段表示的是检测概率
print(chardet.detect(b'Hello world!'))
# gbk编码
data = "四月一个晴朗的早晨，遇到一个百分百女孩".encode('gbk')
print(chardet.detect(data))

# 可见，用chardet检测编码，使用简单（支持中文、日文、韩文等多种语言）。获取到编码后，再转换为str，就可以方便后续处理。


