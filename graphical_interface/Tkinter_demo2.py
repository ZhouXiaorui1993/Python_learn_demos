#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 对第一个GUI程序进行改进，加入一个文本框，让用户可以输入文本，然后点击按钮后，弹出消息对话框


# 先导入Tkinter的所有内容
from tkinter import *
import tkinter.messagebox as messagebox

# 再从Frame派生一个Application类，这是所有Widget（窗口小部件）的父容器

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        # pack()方法把Widget加入到父容器中，并实现布局
        # pack()是最简单的布局，grid()可以实现更加复杂的布局
        self.pack()
        # 在下面的方法中，我们创建一个Label和一个button
        self.create_widgets()

    def create_widgets(self):
        self.Lable = Label(self, text = '请输入您的姓名：')
        self.Lable.pack()
        self.nameInput = Entry(self)
        self.nameInput.pack()
        # 当Button被点击时，将触发self.hello()方法
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello, %s!' % name)
# 在Python中，每个Button、Label、输入框等， 都是一个Widget。
# Frame则是可以容纳其他Widget的Widget，所有的Widget组合起来就是一棵树

# 第三步：实例化Application，并启动消息循环
app = Application()
# 设置窗口标题
app.master.title('first test of GUI')
# 主消息循环
app.mainloop()
# GUI的主程序负责监听来自操作系统的消息，并依次处理每一条消息。因此，如果消息处理非常耗时，就需要在新线程中处理
