#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Python支持多种图形界面的第三方库，包括：1）Tk 2）wxWidgets 3）Qt 4）GTK
# 但是Python自带的库支持Tk的Tkinter，无需安装任何包，就可以直接使用
# 下面简单介绍使用Tkinter进行GUI编程

# 第一个GUI程序
# 先导入Tkinter的所有内容
from tkinter import *

# 再从Frame派生一个Application类，这是所有Widget（窗口小部件）的父容器

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        # pack()方法把Widget加入到父容器中，并实现布局
        # pack()是最简单的布局，grid()可以实现更加复杂的布局
        self.pack()
        # 在下面的方法中，我们创建一个Label和一个button，当Button被点击时，触发self.quit()使得程序退出
        self.create_widgets()

    def create_widgets(self):
        self.helloLabel = Label(self, text='Hello, world!')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Qiut', command=self.quit)
        self.quitButton.pack()

# 在Python中，每个Button、Label、输入框等， 都是一个Widget。
# Frame则是可以容纳其他Widget的Widget，所有的Widget组合起来就是一棵树

# 第三步：实例化Application，并启动消息循环
app = Application()
# 设置窗口标题
app.master.title('first test of GUI')
# 主消息循环
app.mainloop()
# GUI的主程序负责监听来自操作系统的消息，并依次处理每一条消息。因此，如果消息处理非常耗时，就需要在新线程中处理
