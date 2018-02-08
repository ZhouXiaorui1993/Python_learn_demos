#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 单元测试文件

import unittest
from e_mydict_fortest import MyDict


class TestDict(unittest.TestCase):

    def setUp(self):  # 单元测试中的两个特殊的方法，这两个方法分别在每调用一个测试方法的前后分别被执行。
        print('setUp...')

    def tearDown(self):
        print('tearDown...')

    def test_init(self):  # 以`test`开头的方法就是测试方法，不以test开头的方法不被认为是测试方法
        # 测试的时候不会被执行
        d = MyDict(a=1, b='test')
        self.assertEqual(d.a, 1)  # 断言d.a的返回结果与1相等
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = MyDict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = MyDict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = MyDict()
        with self.assertRaises(KeyError):  # 另一种重要的断言：期待抛出指定类型的error
            value = d['empty']

    def test_attrerror(self):
        d = MyDict()
        with self.assertRaises(AttributeError):
            value = d.empty

    if __name__ == '__main__':  # 加上这两行代码就可以把mydict_test.py当做正常的Ｐｙｔｈｏｎ脚本运行
        unittest.main()




