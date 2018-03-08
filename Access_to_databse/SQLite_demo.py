#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# SQLite是一种嵌入式数据库，它的数据库就是一个文件。由于SOLite本身是C写的，体积很小，
# 所以经常被集成到各种应用程序中，甚至在iOS和Android的APP中都可以集成。
# Python就内置了SQLite3，所以在Python中可以直接使用SQLite。
# 在使用前，需要搞清楚几个概念：

# 表是数据库中存放关系数据的集合，一个数据库里面通常包含多个表，例如学生的表，班级的表，
# 学校的表等等。表与表之间通过外键关联。

# 要操作关系数据库，首先要连接到数据库，一个数据库连接称为Connection；

# 连接到数据库后，需要打开游标，称之为Cursor，通过它来执行SQL语句，然后获得执行结果。

# Python定义了一套操作数据库的API接口，任何数据库要连接到Python，只需要提供符合Python
# 标准的数据库驱动即可。

# 由于SQLite的驱动内置在Python标准库中，所以我们可以直接操作SQLite数据库。

# 练习：请编写函数，在sqlite中根据分数段查找指定的名字

import os
import sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'test.db') # 在当前运行脚本的绝对路径下，创建一个test.db路径
if os.path.isfile(db_file):  # 如果该路径中存在test.db，则删除此文件，在后面新建
    os.remove(db_file)

# 初始数据
conn = sqlite3.connect(db_file)  # 在当前路径下新建test.db文件并建立连接
cursor = conn.cursor()  # 打开游标
try:
    # 执行SQL语句
    cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
    cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
    cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
    cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
finally:
    # 关闭游标
    cursor.close()
    # 提交事务
    conn.commit()
    # 关闭连接
    conn.close()


def get_score_in(low, high):
    """返回指定的分数区间的名字，按分数从低到高排序"""
    con = sqlite3.connect(db_file)
    curs = con.cursor()
    try:
        # 执行查询语句
        curs.execute(r"select * from user where score between ? and ? order by score", (low, high))
        # 获得查询结果集
        values = curs.fetchall()
    finally:
        curs.close()
        con.close()
    return [std[1] for std in values]

print(get_score_in(60, 90))


