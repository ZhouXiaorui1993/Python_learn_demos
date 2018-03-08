#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# SMTP是发送邮件的协议，Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件。
# Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件

from email.mime.text import MIMEText
from tkinter import *
import tkinter.messagebox as messagebox
import smtplib


def send_mails(message, from_addr, password, smtp_server, port, to_addr):

    # 首先，我们来构造一个最简单的纯文本邮件
    # 第一个参数是邮件正文，第二个参数是MIME的subtype，传入'plain'表示纯文本，最终的MIME就是'text/plain',
    # 最后一定要用utf-8编码保证多语言兼容性
    msg = MIMEText(message, 'plain', 'utf-8')

    # 然后通过SMTP发出去
    # 输入Email地址和口令， smtp服务器地址
    # server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25,qq邮箱为465(ssl端口)
    server = smtplib.SMTP_SSL(smtp_server, port)
    server.set_debuglevel(1) # 打印出和SMTP服务器交互的所有信息。
    # server.login(from_addr, password) # 用来登录SMTP服务器,qq授权码dhjintgjevrcbdhj
    server.login(from_addr, password)
    # 发送邮件，可以传入一个list实现群发，邮件正文是一个str，as_string()把MIMEText对象变成一个String
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        # pack()方法是最简单的布局
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label_faddr = Label(self, text='Email address：', bg='Pink')
        self.label_faddr.grid(row=1, column=0)
        self.faddr_input = Entry(self)
        self.faddr_input.grid(row=1, column=1)

        self.label_password = Label(self, text='password: ', bg='LightBlue')
        self.label_password.grid(row=2, column=0)
        self.password_input = Entry(self)
        self.password_input.grid(row=2, column=1)

        self.label_SMTPserver = Label(self, text='SMTP server: ', bg='PeachPuff')
        self.label_SMTPserver.grid(row=3, column=0)
        self.SMTPserver_input = Entry(self)
        self.SMTPserver_input.grid(row=3, column=1)

        self.label_SMTPport = Label(self, text='SMTP port: ', bg='PaleGreen')
        self.label_SMTPport.grid(row=4, column=0)
        self.SMTPport_input = Entry(self)
        self.SMTPport_input.grid(row=4, column=1)

        self.label_taddr = Label(self, text=r"other's Email address: ", bg='LightYellow')
        self.label_taddr.grid(row=5, column=0)
        self.taddr_input = Entry(self)
        self.taddr_input.grid(row=5, column=1)

        self.message = Label(self, text='content of your Email: ', bg='Thistle')
        self.message.grid(columnspan=2)
        self.message_input = Entry(self)
        self.message_input.grid(columnspan=2)

        # 当send mail按钮被点击时，触发send_mail()方法
        self.send_button = Button(self, text='send mail', bg='BUrlyWood', command=self.send_mail)
        self.send_button.grid(columnspan=2)

    def send_mail(self):
        message = self.message_input.get() or None
        from_addr = self.faddr_input.get()
        password = self.password_input.get()
        smtp_server = self.SMTPserver_input.get()
        port = int(self.SMTPport_input.get())
        to_addr = self.taddr_input.get()
        try:
            send_mails(message, from_addr, password, smtp_server, port, to_addr)
        except Exception:
            messagebox.showinfo('Error', '发送失败， 请检查后重新输入！')
        else:
            messagebox.showinfo('Success', '恭喜您，邮件发送成功！')
# 实例化Application
app = Application()
app.master.title('邮件发送助手')
# 启动消息循环
app.mainloop()
