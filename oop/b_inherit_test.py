#!usr/bin/env python3
# -*- coding: utf-8 -*-
# 继承和多态,单元测试练习


import unittest
from b_inherit_demo import Tree


class TestInherit(unittest.TestCase):

    def test_init(self):
        t = Tree('30m', 98)
        self.assertEqual(t.height, '30m')
        self.assertEqual(t.age, 98)
        self.assertEqual(t.color, 'green')

    def test_error(self):
        with self.assertRaises(TypeError):
            t = Tree('red')
        with self.assertRaises(AttributeError):
            t = Tree('30m', 98)
            name = t.name
