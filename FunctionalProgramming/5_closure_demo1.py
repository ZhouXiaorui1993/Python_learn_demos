# coding:utf-8


def count():
    """闭包容易出错的点，返回的函数引用了循环变量"""
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs
f1, f2, f3 = count()  # 可将一个list中的元素分别赋值给不同的变量
print(f1())
print(f2())
print(f3())  # 得到的结果都是3


def count2():
    """修改上面的函数，方法一：定义时先用默认参数的方法绑定i"""
    fs = []
    for i in range(1, 4):
        def f(i=i):
            return i*i
        fs.append(f)
    return fs
g1, g2, g3 = count2()  # 可将一个list中的元素分别赋值给不同的变量
print(g1())
print(g2())
print(g3())  # 得到的结果都是3


def count3():
    """修改上面的函数，方法二：再定义一个函数，用该函数的参数绑定循环变量当前的值"""
    def h(i):
        def f():
            return i * i
        return f
    fs = []
    for i in range(1, 4):
        fs.append(h(i))
    return fs
p1, p2, p3 = count3()  # 可将一个list中的元素分别赋值给不同的变量
print(p1())
print(p2())
print(p3())  # 得到的结果都是3
