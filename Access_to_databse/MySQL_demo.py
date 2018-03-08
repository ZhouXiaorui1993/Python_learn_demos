#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# MySQL是世界上使用最广泛的数据库服务器。SQLite的特点是轻量级、可嵌入，
# 但不能承受高并发访问，适合桌面和移动应用。而MySQL是为服务器端设计的数据库，
# 能承受高并发访问，同时占用的内存也远远大于SQLite

# 此外，MySQL内部有多种数据库引擎，最常用的引擎是支持数据库事务的InnoDB

# 安装MySQL:可下载安装，也可以在命令行通过命令安装

# 安装时，MySQL会提示输入root用户的口令，本机设置的是116764
# 安装完成后，需要通过修改配置文件设置编码为utf8

# 安装MySQL驱动：
# sudo pip3 install mysql-connector-python --allow-external mysql-connector-python

# 首先启动MySQL服务器：
# $ mysql -u root -p
# 输入口令后，进入MySQL语句输入界面
# $ mysql> create database test； # 创建一个名为test的数据库，注意MySQL语句以;结尾

# 创建好以后，输入exit，退出MySQL
# 下面演示如何连接到MySQL服务器的test数据库

# 导入MySQL数据库
import mysql.connector
conn = mysql.connector.connect(user='root', password='116764', database='test')
# 打开游标
cursor = conn.cursor()
# 检查表是否存在，若存在则删除
cursor.execute('drop table if exists student')
# 创建一个table，名为student
# primary key 是主关键字，等价于唯一（UNIQUE）且非空（NOT NULL），一个表不能有多个主键，并且主键值不能为空值
# varchar()表示数据类型为字符型，20表示最大的字符长度
cursor.execute('create table student (id varchar(20) primary key, name varchar(20), score int)')
# 插入数据
# 方式一
cursor.execute('insert into student (id, name, score) values (%s, %s, %s)', ['1', 'Michael', 88])
# 方式二
cursor.execute(r"insert into student values ('2', 'Bart', 55 )")
cursor.execute(r"insert into student values ('3', 'Lisa', 90 )")
cursor.execute(r"insert into student values ('4', 'Adam', 70 )")
# 提交事务
conn.commit()
# 关闭游标
cursor.close()
# 关闭连接
conn.close()








