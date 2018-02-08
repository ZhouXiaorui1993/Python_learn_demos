#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 用logging记录


import logging
logging.basicConfig(level=logging.INFO)  # logging允许指定记录信息的级别
# 有debug、info、warning、error等几个级别，指定level = INFO时，logging.debug就不起作用了
# 使用logging的另一个好处是：通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。


s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)

