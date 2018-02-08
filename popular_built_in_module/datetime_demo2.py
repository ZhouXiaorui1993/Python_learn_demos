#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 假设你获取了用户输入的日期和时间，以及一个时区信息如UTC+5:00，均是str，
# 请编写一个函数将其转换为timestamp


import re
from datetime import datetime, timezone, timedelta


def get_tz_info(tz_str):
    tz_info = re.match(r'UTC(\+|\-)(0?[0-9]|1[0-1]):00', tz_str)
    if not tz_info:
        raise TypeError('时区格式错误!')
    else:
        return int(tz_info.group(1)+tz_info.group(2))


def to_timestamp(dt_str, tz_str):
    tz_hour = get_tz_info(tz_str)
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    # 创建一个时区
    tz_utc = timezone(timedelta(hours=tz_hour))
    tz_dt = dt.replace(tzinfo=tz_utc)
    tz_stamp = tz_dt.timestamp()
    return tz_stamp


# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

# t3 = to_timestamp('2014-5-31 16:10:20', 'UTC-09:00')
# assert t3 == 1433121030.0, t2

print('ok')

