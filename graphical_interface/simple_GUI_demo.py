#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 用GUI做简单的BIM测试界面

from tkinter import *
import tkinter.messagebox as messagebox


def cal_bim(weight, height):
    """
    计算BIM
    :param weight:
    :param height:
    :return:
    """
    bim = float(weight) / (float(height)/100) ** 2
    print(weight, height, bim)

    if float(weight) <= 0 or float(height) <= 0:
        return "输入有误，请检查后重新输入！"
    elif 0 < bim <= 18.5:
        return "您的BIM值为：%.2f,体重过轻." % bim
    elif bim <= 25:
        return "您的BIM值为：%.2f,体重正常." % bim
    elif bim <= 28:
        return "您的BIM值为：%.2f,体重过重." % bim
    elif bim <= 32:
        return "您的BIM值为：%.2f,身体肥胖." % bim
    elif bim > 32:
        return "您的BIM值为：%.2f,严重肥胖." % bim

# 从Frame派生一个Application类，是所有Widget的父容器
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # 身高输入提示语句
        self.HeightLable = Label(self, text = '请输入您的身高(单位：cm):')
        self.HeightLable.pack()
        # 输入文本框
        self.HeightInput = Entry(self)
        self.HeightInput.pack()
        # 体重输入提示语句
        self.WeightLable = Label(self, text='请输入您的体重(单位：kg)：')
        self.WeightLable.pack()
        # 输入文本框
        self.WeightInput = Entry(self)
        self.WeightInput.pack()
        # 计算按钮，点击后触发计算方法
        self.cal_button = Button(self, text='计算BIM', command=self.calculate_bim)
        self.cal_button.pack()

    def calculate_bim(self):
        w = self.WeightInput.get()
        h = self.HeightInput.get()
        try:
            bim = cal_bim(w, h)
        except Exception:
            messagebox.showinfo('Error', '参数应为数字!')
        else:
            messagebox.showinfo('BIM指数', '%s' % bim)

# 实例化Application
app = Application()
app.master.title('BIM计算器')
# 启动消息循环
app.mainloop()
