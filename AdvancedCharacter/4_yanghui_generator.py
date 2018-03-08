#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 利用generator输出杨辉三角，参考了别人的代码


def yang_hui(row):
    l = [1]
    while len(l) <= row:
        yield l
        l = [0] + l + [0]
        l = [l[i] + l[i + 1] for i in range(len(l)-1)] # 这里不存在下面的问题，因为对l重新赋值后，其id发生了变化。
    return 'done'
# yh = yang_hui(4)
# print(yh)
result = []
for t in yang_hui(4):
    print(t,id(t))
    result.append(t)
print(result)


#第二种
def triangles():
    t = []
    while True:
        for i in range(len(t) - 1):
            t[i] = t[i] + t[i+1]
        t.insert(0, 1)

        #yield t[:]
        # 这里需要理解一下变量存储的原理，如果不进行切片复制，则t的id一直不变，测试时append进result变会出现问题。
        yield t
# test
n = 0
results = []
for s in triangles():
    print(s, id(s))
    results.append(s)
    n = n + 1
    if n == 3:
        break
print(results)