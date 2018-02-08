#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 摘要算法的应用
# 程序改进，对口令加盐存储


import hashlib,random


# 得到口令的MD5
def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()


# User类
class User(object):
    def __init__(self, name, password):
        self.name = name
        # 对原始口令加一个复杂的字符串，俗称加盐处理
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(password + self.salt)

# 数据库
db = {}


# 注册函数
def register(username, password):
    db[username] = User(username, password)


# 登录验证
def login(name, password):
    user = db[name]
    return user.password == get_md5(password + user.salt)

# 测试:
register('michael', '123456')
register('bob', 'abc999')
register('alice', 'alice2008')

assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')

print('ok')


