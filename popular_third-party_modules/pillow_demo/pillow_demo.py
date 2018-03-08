#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Pillow的前身是PIL（Python Image Library），由于它仅支持到Python2.7，所以一群志愿者在其基础上创建了兼容的版本，即为Pillow
# 安装时需要使用 $ pip install pillow
# 但导入该库实际上是导入PIL

from PIL import Image

# 最常见的图像缩放操作
# 打开一个png文件
im = Image.open('test.png')
# 获得图像尺寸
w, h = im.size
print('Original image size: %s×%s' % (w, h))
# 缩放到%50
im.thumbnail((w//3, h//3))
print('Resize image to: %sx%s' % (w//3, h//3))
# 将RGBA转换为RGB
rgb_im = im.convert('RGB')
# 把缩放后的图像用jpeg格式保存
rgb_im.save('thumbnail.jpg', 'jpeg')

# 其他功能如切片、旋转、滤镜、输出文字、调色板等一应俱全
# 比如，模糊效果也只需要几行代码
from PIL import ImageFilter

# 打开之前缩放后的图像
im2 = Image.open('thumbnail.jpg')
# 应用模糊滤镜
im3 = im2.filter(ImageFilter.BLUR)
im3.save('blur.jpg', 'jpeg')
# im3.show()

# PIL的ImageDraw提供了一系列绘图方法，让我们可以直接绘图。
# 比如要生成字母验证码的图片

from PIL import ImageDraw, ImageFont
import random


# 随机字母
def rnd_chr():
    return chr(random.randint(65, 90))


# 随机颜色1
def rnd_color():
    return random.randint(64, 255), random.randint(64, 255), random.randint(64, 255)


# 随机颜色2
def rnd_color2():
    return random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)

# 新建一个图像
width = 100 * 4
height = 130
image = Image.new('RGB', (width, height), (255, 220, 255))
# print(image)
# image.show()
# 创建Font对象
font = ImageFont.truetype('/usr/share/fonts/truetype/Ubuntu-LI.ttf', 45)
# 创建Draw对象
draw = ImageDraw.Draw(image)
# 填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rnd_color())
# 输出文字
for t in range(4):
    draw.text((100 * t + 35, 40), rnd_chr(), font=font, fill=rnd_color())
# 模糊
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')
image.show()


