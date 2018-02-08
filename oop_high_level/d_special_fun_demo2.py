#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 利用完全动态的__getattr__，写出链式调用的例子


class Chain(object):

    def __init__(self, path=''):
        self.path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self.path, path))

    def __str__(self):
        return self.path

    __repr__ = __str__

print(Chain().status.user.timeline.list)
print(Chain().a.b.c.d)