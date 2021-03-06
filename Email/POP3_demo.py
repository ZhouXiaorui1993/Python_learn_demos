#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# SMTP用于发送邮件，而POP3用于收取邮件
# 收取邮件就是编写一个MUA作为客户端，从MDA把邮件获取到用户的电脑或手机上。收取邮件最常用的协议是POP协议，目前版本号是3，俗称POP3
# Python内置一个poplib模块，实现了pop3协议，可以直接用来收邮件
# 注意到pop3协议收取的不是一个可以阅读的邮件本身，而是邮件的原始文本，这和SMTP协议很像，它发送的也是经过编码后的一大段文本。
# 要把pop3收取的文本变成可以阅读的邮件，还需要用email模块提供的各种类来解析原始文本，变成可阅读的邮件对象。
# 所以收取文件分为两步
# 1.用poplib把邮件的原始文本下载到本地；2.用email解析原始文本，还原为邮件对象

# 通过pop3下载邮件
import poplib

# 输入邮件地址，口令和POP3服务器地址
email = input('Email: ')
password = input('password: ') # qq邮箱用授权码代替
pop3_server = input('POP3 server: ')

# 连接到POP3服务器：
server = poplib.POP3_SSL(pop3_server, 995) # qq邮箱ssl端口为995
# 可以打开或关闭调试信息
server.set_debuglevel(1)
# 可选：打印POP3服务器的欢迎文字
print(server.getwelcome().decode('utf-8'))

# 身份认证
server.user(email)
server.pass_(password)

# stat()返回邮件数量和占用空间
print('Messages: %s. Size: %s' % server.stat())
# list()返回所有邮件的编号
mails = server.list()
# 可以查看返回的列表类似[b'1 82939', b'2 2184', ...]
print(mails)

# 获取最新一封邮件，注意索引号从1开始
index = len(mails)
resp, lines, octets = server.retr(index)

# lines存储了邮件的原始文本的每一行
# 可以获得整个邮件的原始文本
msg_content = b'\r\n'.join(lines).decode('utf-8')


# 稍后解析出邮件
# 解析的过程和构造邮件正好相反
# 首先导入必要的模块
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
# 只要一行代码就可以把邮件内容解析为Message对象
msg = Parser().parsestr(msg_content)
# 但是这个Message对象本身可能是一个MIMEMultipart对象，即包含嵌套的其他MIMEBase对象，嵌套可能还不止一层
# 所以我们要递归地打印出Message对象的层次结构
# indent用于缩进显示
def print_info(msg, indent=0):
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header == 'Subject':
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            print('%s%s: %s' % ('    ' * indent, header, value))
    if (msg.is_multipart()):
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%spart %s' % ('  ' * indent, n))
            print('%s--------------------' % ('  ' * indent))
            print_info(part, indent + 1)
    else:
        content_type = msg.get_content_type()
        if content_type == 'text/plain' or content_type == 'text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print('%sText: %s' % ('  ' * indent, content + '...'))
        else:
            print('%sAttachment: %s' % ('  ' * indent, content_type))


# 邮件中的Subject或者Email中包含的名字都是经过编码后的str，要正常显示，就必须decode
def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value

def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset

# 打印邮件
print_info(msg)

# 可以根据邮件索引号直接从服务器删除邮件：
# server.dele(index)
# 关闭连接
server.quit()

