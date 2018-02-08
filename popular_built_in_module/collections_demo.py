#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 内建模块collections使用示例
# collections是Python内建的一个集合模块，提供了许多有用的集合类


# nametuple
# nametuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数
# 并且可以用属性而不是索引来引用tuple的某个元素
# 例如，定义一个点的二维坐标
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print('x=%s' % p.x,'y=%s' % p.y)
# 可以验证Point对象是tuple的一种子类
print(isinstance(p, Point), isinstance(p, tuple))


# deque
# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率都很低
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
from collections import deque
q = deque(['a', 'b', 'c'])
# 追加元素
q.append('x')
# 向头部添加
q.appendleft('y')
print(q)
q.pop()
q.popleft()
print(q)


# defaultdict
# 使用dict时，如果引用的Key不存在，就会跑出KeyError。如果希望key不存在时，返回一个默认值，就可以使用defaultdict
# 注意defaultdict是一个类，除了key不存在时会返回默认值之外，它和dict的是完全一样的
from collections import defaultdict
# 默认值是调用函数返回的，而函数是在创建defaultdict对象时传入的
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'hahaha'
print(dd['key1'], dd['key2'])

# OrderedDict
# 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序
# 如果要保持Key的顺序，可以用OrderedDict
from collections import OrderedDict
# 复习一下dict()的用法
# 用传入关键字的方法创建一个字典
d1 = dict(a=1, b=2, c=3)
# 用映射函数的方式构造字典
d2 = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
# 用可迭代对象的方式构造
d3 = dict([('one', 1), ('two', 2), ('three', 3)])
# 可以看出dict的key是无序的
print(d1, '\n', d2, '\n', d3, sep='')
od = OrderedDict(a=1, b=2, c=3)
# 注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序
print(od)
print(list(od.keys()))

# Counter
# Counter是一个简单的计数器，例如统计字符出现的个数
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
# 可以看出Counter也是dict的一个子类
print(c)