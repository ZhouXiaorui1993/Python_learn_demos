#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# SMTP是发送邮件的协议，Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件。
# Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件

# 首先，我们来构造一个最简单的纯文本邮件
from email.mime.text import MIMEText
# 第一个参数是邮件正文，第二个参数是MIME的subtype，传入'plain'表示纯文本，最终的MIME就是'text/plain',
# 最后一定要用utf-8编码保证多语言兼容性
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')

# 然后通过SMTP发出去
# 输入Email地址和口令
# from_addr = input('From: ')
from_addr_qq = '843786909@qq.com'
# password = input('Password: ')
password_qq = 'dhjintgjevrcbdhj'
# 输入收件人地址
# to_addr = input('To: ')
to_addr = 'zhouxiaorui1993@163.com'
# 输入SMTP服务器地址
# smtp_server = input('SMTP server: ')
smtp_server_qq = 'smtp.qq.com'

import smtplib
# server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25,qq邮箱为465(ssl端口)
server = smtplib.SMTP_SSL(smtp_server_qq, 465)
server.set_debuglevel(1) # 打印出和SMTP服务器交互的所有信息。
# server.login(from_addr, password) # 用来登录SMTP服务器,qq授权码dhjintgjevrcbdhj
server.login(from_addr_qq, password_qq)
# 发送邮件，可以传入一个list实现群发，邮件正文是一个str，as_string()把MIMEText对象变成一个String
server.sendmail(from_addr_qq, [to_addr], msg.as_string())
server.quit()

