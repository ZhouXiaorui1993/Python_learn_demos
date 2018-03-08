#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 了解了WSGI接口以后，我们发现，其实一个web app，就是写一个WSGI的处理函数，针对每个HTTP请求进行响应
# 而web框架是在WSGI的基础上进一步抽象化，让我们专注于用一个函数处理一个URL，至于URL到函数的映射，可以交给web框架来做
# 下面选择使用flask
# 处理3个URL，分别是：
# GET /:首页，返回home
# GET /signin:登录页，显示登录表单
# POST /signin:处理登录表单，显示登录结果
# flask可以通过Python的装饰器在内部自动地把URL和函数关联起来，如下：

from flask import Flask
from flask import request
from flask import render_template
import hashlib
import mysql.connector


# 如果import该模块，__name__的值为模块文件名；如果直接运行，则__name__的值为__main__
app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET'])
def login_form():
    return render_template('login_form.html')


@app.route('/register', methods=['GET'])
def register_form():
    return render_template('register.html')


@app.route('/login', methods=['POST'])
def login():
    # 需要从request对象读取表单内容,flask通过requst.form['name']来获取表单的内容
    username = request.form['username']
    password = request.form['password']
    md5_password = hashlib.md5()
    md5_password.update(password.encode('utf-8'))
    # 连接数据库
    conn = mysql.connector.connect(user='root', password='116764', database='dtt_web')
    # 打开游标
    cursor = conn.cursor()
    # 查找数据
    cursor.execute(r"select * from user where name = '%s'" % username)
    res = cursor.fetchall()
    # 关闭
    cursor.close()
    conn.close()
    if not res[0][0]:
        return render_template('login_form.html', message='用户不存在，请检查后再输入！', username=username)
    elif md5_password.hexdigest() != res[0][1]:
        return render_template('login_form.html', message='密码错误，请检查后再输入！', username=username)
    return render_template('login_ok.html', username=username)


@app.route('/register', methods=['POST'])
def register(name=None):
    username = request.form['username']
    password = request.form['password']
    re_password = request.form['re_password']
    md5_password = hashlib.md5()
    md5_password.update(password.encode('utf-8'))
    # 建立连接，数据库dtt_web
    conn = mysql.connector.connect(user='root', password='116764', database='dtt_web')
    # 打开游标
    cursor = conn.cursor()
    # 查找数据
    cursor.execute(r"select * from user where name = '%s'" % username)
    res = cursor.fetchall()
    if res:
        return render_template('register.html', message='用户名已存在，请直接登录！', username=username)
    elif password != re_password:
        return render_template('register.html', message='两次输入的密码不一致，请检查后重新输入！', username=username)
    elif not username or not password:
        return render_template('register.html', message='用户名和密码不能为空，请检查后重新输入！', username=username)
    # 数据没问题，则存储到数据库dtt_web
    # 插入数据
    cursor.execute('insert into user (name, password) values (%s, %s)', [username, md5_password.hexdigest()])
    # 提交事务
    conn.commit()
    # 关闭游标和连接
    cursor.close()
    conn.close()
    return render_template('register_ok.html')

if __name__=='__main__':
    # 若不配置host和port，则默认是localhost，端口为5000
    # 若配置，如写作app.run("",8000)，就是localhost，端口8000
    app.run("",8080)
