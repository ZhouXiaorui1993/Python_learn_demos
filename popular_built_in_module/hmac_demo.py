#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 通过哈希算法，我们可以验证一段数据是否有效。而为了防止黑客通过彩虹表根据哈希值反推原始口令，在计算哈希的时候，不能仅针对原始输入计算，
# 需要增加一个salt来使得相同的输入也能得到不同的哈希，这样，大大增加了黑客破解的难度。
# 和我们自定义的加salt算法不同，Hmac算法针对所有哈希算法都通用，无论是MD5还是SHA-1。
# 采用Hmac替代我们自己的salt算法，可以使程序算法更标准化，也更安全。
# Python自带的hmac模块实现了标准的Hmac算法。

# 我们首先需要准备待计算的原始消息message，随机key，哈希算法，这里采用MD5

import hmac
message = b'Hello, world!'
key = b'secret'
h = hmac.new(key, message, digestmod='MD5')
# 如果消息很长，可以多次调用h.update(msg)
print(h.hexdigest())
# 可见使用hmac和普通hash算法非常类似。hmac输出的长度和原始哈希算法的长度一致。需要注意传入的key和message都是bytes类型，str类型需要首先编码为bytes。

