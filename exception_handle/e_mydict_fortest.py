#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 单元测试示例，需要测试的文件


class MyDict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):  # 在寻找某不存在的属性时，Python会自动调用`__getattr__()`方法。
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):  # 设置类实例属性时自动调用该方法
        self[key] = value

