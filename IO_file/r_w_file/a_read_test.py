#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 文件读写


class TestFile(object):

    def show_test_file(self):
        try:
            self.name = open('./test.txt', 'r')
            print(self.name.read())  # read()读取整个文件，将文件内容放到一个字符串变量中
        finally:
            if self.name:
                self.name.close()  # 对文件操作结束后必须关闭

    def show_size_file(self):
        n = int(input('please input size value that you wanna get: n = \n'))
        with open('./test.txt', 'r') as self.name:  # 用with语句打开会自动调用close()方法，写法更简洁
            print(self.name.read(n))  # read(size)方法：每次最多读取size个字节的内容

    def show_line_file(self):
        with open('./test.txt', 'r') as self.name:
            for line in self.name.readlines():  # readlines()一次性读取全部内容并按行返回一个list
                print(line.strip())  # 按行打印，由于返回的list中会自动给每一行末尾加上一个`\n`，这里将末尾的换行符删去

    def add_line(self):
        with open('./test.txt', 'a') as self.name:  # 以模式a打开，在末尾追加写入
            self.name.write('\n追加一行文字')

    def rewrite(self):
        with open('./test.txt', 'w') as self.name:  # 以模式w打开，写入且覆盖原有文件内容
            self.name.write('写入一行文字')
test = TestFile()
print("原文件内容：")
test.show_test_file()
# test.show_size_file()
print("\n\n")
test.add_line()
print("改动后文件内容：")
test.show_line_file()
