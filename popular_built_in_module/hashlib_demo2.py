#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 摘要算法的应用
# 例如：存储用户登录的用户名和口令密码，一般要存到数据库表中，但如果以明文保存用户口令，若数据库泄露，则所有用户的
# 口令会落到黑客的手里。此外，网站运维人员是可以访问数据库的，也就是能获取到所有用户的口令
# 因此，正确的保存口令的方式是不存储用户的明文口令，而是存储用户口令的摘要，比如MD5
# 当用户登录时，首先计算用户输入的明文口令的MD5，然后和数据库存储的MD5对比，如果一致，说明口令输入正确，如果不一致，口令肯定错误。


# 练习： 设计一个验证用户登录的函数，根据用户输入的口令是否正确，返回True或False

import hashlib
# 数据库
db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}


# 判断函数
def login(user, password):
    # name = input('please enter your name:')
    if user not in db.keys():
        return 'wrong name!'
    md5_pw = hashlib.md5()
    md5_pw.update(password.encode('utf-8'))
    return db[user] == md5_pw.hexdigest()

# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')
print(login('aaa', 'Alice2008'))



