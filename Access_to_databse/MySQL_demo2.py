#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 导入MySQL数据库
import mysql.connector
conn = mysql.connector.connect(user='root', password='116764', database='test')
# 查询数据
cursor = conn.cursor()
cursor.execute('select * from student where id = %s or id = %s', ('1', '2'))
values = cursor.fetchall()
print(values)

# 关闭游标和连接
cursor.close()
conn.close()