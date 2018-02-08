#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 内建模块datetime使用示例

# datetime模块中有一个datetime类
from datetime import datetime

# 获取当前datetime,返回当前日期和时间，其类型是datetime
now_time = datetime.now()
print(now_time)
print(type(now_time))

# 获取指定某个日期和时间，可以直接用参数构造一个datetime
dt = datetime(2008, 8, 8, 12, 12, 12)
print(dt)
print(type(dt))

# datetime转换为timestamp
# 在计算机中，时间实际上是用数字表示的。我们把1970年1月1日00:00:00 UTC+00:00时区
# 的时刻称为epoch time，记为0（1970年以前的timestamp为负数），当前时间就是相对epoch time的秒数，称为timestamp
# 调用timestam()方法即可转换
now_timestamp = dt.timestamp()
print('当前时间的timestamp为：%s' % now_timestamp)

# 将timestamp转换为datetime
# 注意timestamp是一个浮点数，它没有时区的概念，而datetime是有时区的
# 下面的转化是在timestamp和本地时间（当前操作系统设定的时区）之间做转换
t = 1234567890.0
print('转换为本地时间：%s' % datetime.fromtimestamp(t))
# timestamp也可以直接被转换到UTC标准时间
print('转换为UTC标准时间：%s' % datetime.utcfromtimestamp(t))

# str转换为datetime
# 很多时候用户输入的日期和时间是字符串，要处理日期和时间，首先必须要将str转换为datetime
# 注意转换后的datetime是没有时区信息的
cday = datetime.strptime('2012-9-1 14:14:14', '%Y-%m-%d %H:%M:%S')
print(cday, '转换后类型为：', type(cday))

# datetime转换为str
# 如果已经有了datetime对象，要把它格式化为字符串显示给用户，就需要转换为str
str_now_time = now_time.strftime('%a, %b %d %H:%M')
print(str_now_time, '转换后的类型为：', type(str_now_time))

# datetime加减
# 对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime
# 加减可以直接用＋和－运算符，不过需要导入timedelta类
from datetime import timedelta
print('12 hours later:', now_time + timedelta(hours=+12))
print('3 day later:', now_time + timedelta(days=3))

# 本地时间转换为UTC时间
from datetime import timezone
# 创建时区UTC+8:00
tz_utc_8 = timezone(timedelta(hours=8))
# 强制设置为UTC+8:00
print(now_time.replace(tzinfo=tz_utc_8))

# 时区转换
# 利用带时区的datetime，通过astimezaone()方法，可以转换到任意时区
# 我们可以先通过utcnow()拿到当前的UTC时间，再转换为任意时区的时间
# 强制设置为UTC+0:00
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
# astimezone()将转换时区为东京时间
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print('tokyo_dt: %s' % tokyo_dt)

