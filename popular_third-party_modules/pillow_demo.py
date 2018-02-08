#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Pillow的前身是PIL（Python Image Library），由于它仅支持到Python2.7，所以一群志愿者在其基础上创建了兼容的版本，即为Pillow
# 安装时需要使用 $ pip install pillow
# 但导入该库实际上是导入PIL

from PIL import Image

# 最常见的图像缩放操作
# 打开一个jpg文件
im = Image.open('test.jpg')
# 获得图像尺寸
w, h = im.size
print('Original image size: #s×%s' % (w, h))
