#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 数据库表是一个二维表，包含多行多列。把一个表的内容用Python的数据结构表示出来的话，
# 可以用一个list表示多行，list的每一个元素是tuple，表示一行记录
# Python的DB-API返回的数据结构就是这样表示的
# 但是用tuple表示一行很难看出表的结构，如果把一个tuple用class实例来表示，就更容易看出表的结构来。

"""
class User(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name

user_list = [
    User('1', 'Michael'),
    User('2', 'Bob'),
    User('3', 'Adam')
]
"""

# 这就是传说中的ORM技术：Object-Relational Mapping，把关系数据库的表结构映射到对象上。
# ORM框架就是来做这种转换的，在Python中，最有名的ORM框架是SQLAlchemy
# 首先需要通过pip安装SQLAlchemy：$ pip install sqlalchemy
# 然后利用上次在test数据库中创建的student表，用SQLAlchemy试试

# 第一步：导入SQLAlchemy，并初始化DBSession
from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类
Base = declarative_base()


# 定义Student对象
class Student(Base):
    # 表的名字
    __tablename__ = 'student'

    # 表的结构
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    score = Column(Integer)

# 初始化数据库连接
# SQLAlchemy用一个字符串表示连接信息
# '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine('mysql+mysqlconnector://root:116764@localhost:3306/test')
# 创建DBSession类型
DBSession = sessionmaker(bind=engine)

# 由于有了ORM，我们想数据库表中添加一行记录，可以视为添加一个Student对象

# 创建session对象,DBSession对象可视为当前数据库连接。
session = DBSession()
# 创建新的student对象
new_student = Student(id='5', name='Tina', score=100)
# 添加到session
session.add(new_student)
# 提交即保存到数据库
session.commit()
# 关闭session
session.close()


# 查询数据，有了ORM，查询出来的可以不再是tuple，而是Student对象
# 创建Session
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，若调用all()则返回所有行
student = session.query(Student).filter(Student.id=='5').one()
# 打印类型和对象的name属性:
print('type:', type(student))
print('name:', student.name)
# 关闭Session:
session.close()