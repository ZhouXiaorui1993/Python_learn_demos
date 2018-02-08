#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# unittest文件 for Student 类


import unittest
from f_exercise_unittest import Student


class StudentTest(unittest.TestCase):

    def test_80to100(self):
        s1 = Student('Bart', 80)
        s2 = Student('Lisa', 100)
        self.assertEqual(s1.get_grade(), 'A')
        self.assertEqual(s2.get_grade(), 'A')

    def test_60to80(self):
        s1 = Student('Bart', 60)
        s2 = Student('Lisa', 79)
        self.assertEqual(s1.get_grade(), 'B')
        self.assertEqual(s2.get_grade(), 'B')

    def test_0to60(self):
        s1 = Student('Bart', 0)
        s2 = Student('Lisa', 59)
        self.assertEqual(s1.get_grade(), 'C')
        self.assertEqual(s2.get_grade(), 'C')

    def test_error(self):
        s1 = Student('Bart', 'ling')
        s2 = Student('Lisa', 101)
        s3 = Student('saki', -1)
        with self.assertRaises(TypeError):
            s1.get_grade()
        with self.assertRaises(ValueError):
            s2.get_grade()
            s3.get_grade()

if __name__ == '__main__':
    unittest.main()
