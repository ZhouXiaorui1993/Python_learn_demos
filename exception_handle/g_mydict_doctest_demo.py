#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 文档测试示例


class MyDict(dict):
    """
    Simple dict but also support access as x.y style

    >>> d1 = MyDict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = MyDict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'MyDict' object has no attribute 'empty'
    """

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):  # 在寻找某不存在的属性时，Python会自动调用`__getattr__()`方法。
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'MyDict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):  # 设置类实例属性时自动调用该方法
        self[key] = value

if __name__ == '__main__':  # 当模块正常导入时，doctest不会被执行，只有在命令行直接运行时，才执行doctest。
    # 所以，不必担心doctest会在非测试环境下执行。
    import doctest
    doctest.testmod()