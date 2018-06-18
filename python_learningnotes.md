# 一、Python简介
## 1.诞生

Python是Guido van Rossum在1989年圣诞期间，为打发无聊的假期而编写的一种编程语言。(说起来，Git也是Linus在圣诞假期写的。。)  

## 2.Python适合的开发方向: 
 
1)网络应用，包括网站、后台服务等；  
2)日常小工具，例如系统管理员需要的脚本任务等；  
3)将其他语言开发的程序再包装起来，方便使用  
---
# 二、安装Python
## 1.安装
目前分为两个版本，Python 2.x和3.x，不同操作系统(mac，Windows，linux)安装方式有所不同，可自行百度具体安装方式。  
## 2.Python解释器:  
### 1)CPython
官方版本的解释器，在命令行下运行`python`或`python3`时启动的就是CPython解释器；  
### 2)IPYthon
基于CPython之上的一个交互解释器，前者用`>>>`作为提示符，后者用`In [序号]`作为提示符。   
### 3)PyPy
采用`JIT技术`，执行速度快，但和CPython有些不同，同样的代码可能执行结果有所不同；  
### 4)Jython
运行在Java平台的Python解释器，可以直接把Python代码编译成Java字节码执行。  
### 5)IronPython
和Jython类似，运行与微软.net平台，可直接将Python代码编译成.Net的字节码  

---
# 三、Python基础

## 输入和输出
输出:`print()`函数；  
输入:`input()`函数，可以让用户输入字符串。  

**注意**`input`返回的数据类型是`str`，如需得到数字，需要用`int()`函数或`float()`函数将其转换。  

## 数据类型和变量
### 整数

注意:Python的整数和浮点数大小都没有限制，但是超出一定的范围就直接表示为`inf`(无限大) 。  

### 浮点数

对于很大或很小的浮点数，如1230000，可以用科学计数法写作:`1.23e6`或`12.3e5`.

### 字符串

用单引号`'`或双引号`"`括起来的文本。  

**转义**:如果字符串中本身包括`"`这样的容易引起歧义的字符，则可以用转义字符`\`来标识。例如:
```
>>>'I\'m \"zhou\"!'
```
表示的为字符串`I'm "zhou"!`。  

转义字符还可以转义很多字符，如`\n`表示换行，`\t`表示制表符，`\\`表示字符`\`本身等等。  

如果字符中有许多字符需要转义，为了简化，Python允许使用`r''`表示`''`内部的字符串默认不转义，即原样打印出来。例如:

```
>>>print(r'\\\\\ff\ff\')
\\\\\ff\ff\
```

**多行文本**:如果字符串内部有很多换行，用`\n`写在一行里阅读不方便。鉴于此，Python允许使用`'''...'''`的格式表示多行内容，例如:
```
>>>print('''this is line1
...this is line2
...this is line3''')
this is line1
this is line2
this is line3
```

注意:上述程序是在命令行中执行的，若写成`.py`文件，则为:

```
print('''this is line1
this is line2
this is line3''')
```
PS:多行字符串`'''...'''`还可以在前面加上`r`使用。  

### 布尔值
只有`True`和`False`两种值。  

逻辑运算:`and`、`or`和`not`  

布尔值常用于条件判断，如:  

```
if score>=60:
    print('pass')
else:
    print('fail')
```
### 空值

Python中的一个特殊的值，用`None`表示。  

### 变量

Python为动态语言，表现在其变量本身类型不固定，在定义变量时无需指定变量类型。  

### 常量

在Python中，通常用全部大写的变量名表示常量:  

### 运算符

**算术运算符**  

|运算符|描述|
|:---:|:---:|
|+|返回两数之和|
|-|返回两数之差，或得到一个负数|
|*|返回两数之积或得到一个被重复若干次的字符串|
|/|精确除法，计算结果为浮点数|
|//|地板除，返回商的整数部分|
|%|取余，返回除法的余数|
|\*\*|幂运算，如`x**y`返回x的y次幂|  

**比较运算符**

|运算符|描述|
|:---:|:---:|
|==|等于，比较对象是否相等|
|!=|不等于，比较对象是否不相等|
|<>|不等于，和!=类似|
|>|大于|
|<|小于|
|>=|大于等于|
|<=|小于等于|  

**逻辑运算符**

|运算符|逻辑表达式|描述|例子|
|:---:|:---:|:---:|:---:|
|and|x and y|布尔"与":遇到假值就返回，即如果x为False，则返回False，否则返回y的计算值。|`3 and 5`返回5|
|or|x or y|布尔"或":遇到真值就返回，即如果x为非0，则返回x的值，否则返回y的计算值|`2 or 7`返回2|
|not|not x|布尔"非":如果x为True，返回False，否则返回True|`not 0`返回True|

**Python成员运算符**

|运算符|描述|
|:---:|:---:|
|in|如果在指定序列中找到值返回True|
|not in|如果在指定序列中没有找到值返回True|

**Python身份运算符**

|运算符|描述|实例|
|:---:|:---:|:---:|
|is|判断两个标识符是不是引用自一个对象|`x is y`，类似与`id(x)==id(y)`，如果引用的是同一个对象则返回True，否则返回false|
|is not|判断两个标识符是不是引用自不同的对象|`x is not y`，相当于`id(x)!=id(y)`|

注:`id()`函数用于获取对象的内存地址。

## 字符串和编码

### 字符编码
**`ASCII`编码**:最早的编码，一个字节表示一个字符，只有127个字符，包括大小写英文字母、数字和一些符号。  

**`GB2312`编码**:中国制定的编码方式，在`ASCII`基础上，加入了中文编码(中文至少两个字节才能表示一个字符)。  

**`Unicode`编码**:将所有语言统一到了一套编码中，但最常用的是两个字节表示一个字符(若需要用到非常偏僻的字符，就需要4个字节)，故此种编码方式占用存储空间较大。  

**`UTF-8`编码**:为节省存储空间，将`Unicode`转化为了可变长度的`UTF-8`编码.它可以根据不同的数字大小编码成1-6个字节，常用的英文字母通常为1个字节，汉字通常为3个字节，生僻字符可能会被编码成4-6个字节。这样，如果传输文本中包含大量英文字符，则使用`UTF-8`可以节省空间。 
 
**注**:现有计算机系统通用的字符编码工作方式为:  
>在计算机内存中，同一使用`Unicode`编码，当需要保存到硬盘或者需要传输时，将其转换为`UTF-8`编码。  

###Python的字符串

在最新的Python3版本中，字符串是以Unicode编码的，也就是说，Python的字符串支持多语言。  

**编码和字符的转换**:对于单个字符的编码，可以用`ord()`函数获取字符的整数表示，`chr()`函数把编码转换为对应的字符:  
```
>>> ord('A')
65
>>> chr(66)
'B'
```
如果知道字符的整数编码，还可以用十六进制写`str`:  
```
>>> ’\u4e2d\u6587‘
'中文'
```
这两种写法是等价的，其中`\uxxxx`表示值为16位十六进制xxxx的字符。(也可以用'\U'，表示32位十六进制xxxx的字符)  

**字符和字节的转换**:由于Python的字符串类型是`str`，在内存中以Unicode表示，一个字符对应若干个字节(`byte`)。如果要在网络上传输或是存储到磁盘，则需要把`str`转化为`bytes`。  
Python对`bytes`类型的数据用带`b`前缀的单引号(或双引号)表示:
```
x=b'ABC'
```
以Unicode表示的`str`可以通过`encode()`方法编码为指定的`bytes`，如:  
```
>>> 'ABC'.encode('ascii')
b'ABC'
>>> '中文'.encode('utf-8')
b'\xe4\xb8\xad\xe6\x96\x87'
```
注:纯英文的`str`可以用`ASCII`编码为`bytes`,内容是一样的；但含有中文的`str`无法用`ASCII`编码为`bytes`，可以用`UTF-8`编码。  
反过来，若从网络或磁盘读取了字节流，这些数据就是`bytes`，可以用`decode()`方法将其解码为`str`，例如:  
```
>>> b'ABC'.decode('ascii')
'ABC'
>>> b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
'中文'
```
如果`bytes`中包含无法解码的字节，`decode()`方法就会报错，若其中只有一小部分无效的字节，可以传入`errors='ignore'`忽略错误的字节，如:  
```
>>> b'\xe4\xb8\xad\xe6\x96\x87\xff'.decode('utf-8',errors='ignore')
'中文'
```
注:在操作字符串时，经常会遇到`str`和'bytes'互相转换的问题，为避免乱码，应当始终坚持使用`UTF-8`对二者进行转换。  

**计算字符数/字节数**:要计算`str`包含多少个字符或`bytes`包含多少个字节，可以利用`len`函数:  
```
>>> len(’中文‘)
2
>>> len('中文'.encode('utf-8'))
6
```
**格式化输出**
1) 在Python中，采用的格式化方式和C语言一致，用`%`实现，例如:  
```
>>> 'Hello, %s!' % 'Bart'
'Hello,Bart!'
>>> 'Hi, %s, your score is %d.'%('Lisa', 99)
'Hi, Lisa, your score is 99.'
```
常见的占位符有:  

|占位符|替换内容|
|:---:|:---:|
|%d   |整数  |
|%f   |浮点数|
|%s   |字符串|
|%x   |十六进制整数|

**注**:如果不确定应该用什么，都可以使用`%s`代替，它会将任何数据类型转换为字符串；  
如果要输出的字符串中有`%`,此时需要转义，用`%%`表示一个`%`；  
如果输出浮点数要保留3位小数，则使用`%.3f`来将其格式化。  

2) 另一种格式化字符串的方式是使用`format()`方法，它可以用传入的参数依次替换字符串内的占位符`{0}`、'{1}'......,不过这种方式比较麻烦。举例如下:  
```
>>> 'Hello, {}, 你的成绩是{1:.2f}'.format('Lisa'，99.00)
'Hello, Lisa, 你的成绩是99.0'
```

## 使用list和tuple
### list

list是Python内置的一种数据类型，也成为列表。它是一种有序的集合，可以随时添加和删除其中的元素。  
例如，列出班级中所有同学的名字:  
```
>>> classmates = ['Michael', 'Bob', 'Tracy']
```
**获取元素个数**:上面的变量`classmates`就是一个list。可以用`len()`函数来获取list元素的个数:  
```
>>> len(classmates)
3
```
**索引**:可以用索引来访问list中每一个位置的元素，索引是从`[0]`开始的:  
```
>>> classmates[0]
'Micheal'
>>> classmate[2]
'Tracy'
```
当索引超出范围，Python会报错`IndexError`。所以，为确保索引不越界，记得最后一个元素的索引号是`len(classmates)-1`。  
若要取得最后一个元素，还可以用`-1`做索引:  
```
>>> classmate[-1]
'Tracy'
```
**添加元素**:list是一个可变的有序表，可以使用`.append()`方法追加元素至末尾:  
```
>>> classmates.append('Lisa')
>>> classmates
['Micheal', 'Bob', 'Tracy', 'Lisa']
```
也可以使用`.insert()`方法在指定位置插入元素，比如索引号为1的位置:  
```
>>> classmates.insert(1,‘Jean’)
>>> classmates
['Micheal', 'Jean', 'Bob', 'Tracy', 'Lisa']
```
**删除元素**:可以用`.pop()`方法删除末尾的元素:  
```
>>> classmate.pop()
'Lisa'
>>> classmates
['Micheal', 'Jean', 'Bob', 'Tracy']
```
用`.pop(i)`方法删除指定索引号`i`的元素:  
```
>>> classmate.pop(1)
'Jean'
>>> classmates
['Micheal', 'Bob', 'Tracy']
```
**元素替换**:如果要将某个元素替换成别的元素，可以直接赋值给对应的索引位置:  
```
>>> classmates[1] = 'Vale'
>>> classmates
['Micheal', 'Vale', 'Tracy']
```

**数据类型**:list中的元素的数据类型可以不同，比如:  
```
>>> student = ['Bart', 'boy', 8, True]
```
list中的元素也可以是另一个list，比如:  
```
>>> job = [student 'teacher' 'docotor' 'engineer']
>>> job
[['Bart', 'boy', 8, True] 'teacher' 'docotor' 'engineer']
>>> len(job)
4
```
如果要取得`'boy'`，可以写`student[1]`或`job[0][1]`,因此`job`可以视为一个二维数组。  

**注**:若list中一个元素也没有，就是一个空的list，长度为0.

### tuple

tuple是Python中的另一种有序列表，它和list非常类似，可以使用`[i]`来索引其中的元素。但不同点在于tuple一旦初始化后就不修改，它不存在`append()`、`insert()`和`pop()`方法，也不能通过赋值将某个元素替换成其他元素。例如:  
```
>>> t = (1,2,'number')
>>> t
(1, 2, number)
>>> t.pop()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'pop'
```
由于tuple不可变，故相对list来讲，使用tuple代码会更加安全。  

**定义tuple**:如果要定义一个空的tuple，可以写成:  
```
>>> t = ()
>>> t
()
```
但是，如果要定义一个只有一个元素的tuple，为避免和小括号歧义，Python规定，这种情况下必须加一个逗号`,`，来消除歧义:  
```
>>> t = (1,)
>>> t
(1,)
```
**"可变"的tuple**:tuple所谓的"不变"指的是，tuple的每个元素指向不变,利用这一规定，可以将tuple指向一个list，而这个list本身的元素是可变的，举例如下:  
```
>>> t = ('a', 'b', ['C', 'D'])
>>> t[2][0] = 'A'
>>> t[2][1] = 'B'
>>> t
('a', 'b', ['A', 'B'])
```
要注意，如果是间接赋值，tuple中的内容不会改变，举例如下:  
```
>>> l=['x','y']
>>> t=['a','b',l]
>>> l=['c','d']
>>> t
['a','b',['x','y']]
>>> t[2][0]='c'
>>> t
['a','b',['c','y']]
```
可见，通过索引改变list中的内容是单纯的内容修改，而指向的地址没有变化，故tuple中的内容改变了；而如果直接对list重新赋值，则是重新开辟一块内存空间，指向的地址发生了变化，但tuple指向的地址是不变的，依然是原来的地址，故tuple中的内容没有改变。  

## 条件判断

Python中的条件判断是通过`if...elif...else...`语句来实现的。举例如下:  

```
age = int(input())
if age >= 18:
    print('adult')#语句1
else:
    print('minor')#语句2
```
如果`if`语句判断是`True`，就执行缩进的语句1，否则执行语句2。(可以省略`else`判断)注意，一定要加冒号`:`。  
还可以加上`elif`做更细致的判断，可以有多个`elif`，`if`语句的完整形式为:  

```
if <条件判断1>:
    <执行1>
elif <条件判断2>:
    <执行2>
elif <条件判断3>:
    <执行3>
...
else:
    <执行4>
```
'if'判断条件还可以简写，比如:  
```
if x:
    print('True')
```
以上语句中，只要`x`是非零数值、非空字符串、非空list等，就判断为`Ture`，否则为`False`。  

## 循环
### for循环

Python的循环分为两种，一种是`for...in`循环，依次把list或tuple中的每个元素迭代出来，例如:  
```
names = ['Micheal', 'Lisa', 'Bob']
for name in names:
    print(name)
```
执行上述语句就是将`names`中的每个元素代入到变量`name`，然后执行缩进块中的语句。
**range()函数**:  
`range()`函数的原型为:`range(start, end[, step])`
参数含义为:  

- start:计数从start开始，若缺省，则默认为0；
- end:计数到end结束，但不包括end；
- step:步长，默认为1。  

注:`range()`函数返回的结果是一个整数序列对象，而非list。若想要得到list，可通过`list()`函数可以将其转化为list。如:  
```
>>> list(range(5))
[0, 1, 2, 3, 4]
```
整数序列也可以直接用来迭代，如:  
```
sum = 0
for x in range(101):
    sum = sum+x
print(sum)
```
### while循环

Python的第二种循环是while循环，只要条件满足，就不断循环，当条件不满足时退出循环。例如:  
```
sum = 0
n = 0
while n<=100:
    sum = sum+n
    n+=1
print(sum)
```
### break

在循环中，`break`语句可以提前退出循环。例如:  
```
L = [1,2,3,4]
for i in L:
    if i==3:
        break
    print(i)
```
打印出的结果为:  
```
1
2
3
```
### continue

在循环过程中，可以通过`continue`语句，跳过当前循环，直接开始下一次循环。例如:  
```
n = 0
while n<10:
    n=n+1
    if n%2==0:
        continue
    print(n)
```
执行以上的代码得到的结果为1,3,5,7,9  

**注**:不要滥用`break`和`continue`语句，它们容易造成代码执行逻辑分叉过多，容易出错。大多数循环并不需要用到它们，上面两个例子，都可以通过修改循环条件或者修改循环逻辑去掉`break`和`continue`。

## 使用dict和set
### dict
dict是Python内置的字典对象，在其他语言中也成为map，使用键-值(key-value)的格式存储，查找速度很快。  
**定义**:举例如下:  
```
>>> d = {'Bob':89, 'Lisa':99, 'Bart':30}
>>> d['Bob']
89
```
**放入数据**:除了初始化时指定外，还可以通过key放入，也可以通过此种方式改变数据或添加数据:  
```
>>> d['Homer']=12
>>> d
{'Bob':89, 'Lisa':99, 'Bart':30, 'Homer':12}
>>> d['Bob']=67
>>> d
{'Bob':67, 'Lisa':99, 'Bart':30, 'Homer':12}
```
可见，一个key只能对应一个value，所以若多次对一个key放入value，后面的值会冲掉前面的。  
**判断key是否存在**:  

- 1.通过`in`来判断  
```
>>> 'Tom' in d
False
```
- 2.通过dict提供的`get()`方法，如果key存在，则返回对应的value；如果key不存在，可以返回`None`或自己指定的value  
```
>>> d.get('Tom')
>>> d.get('Tom',-1)#第二个参数为key不存在时的指定返回值
-1

```
**注意**:dict内部存放顺序和key放入的顺序是没有关系的。  

**特点**:

- 和list相比，dict查找和插入速度极快，不会随着key的增加而变慢；但dict需要占用大量的内存，内存浪费多。  
- dict的key必须是**不可变对象**。在Python中，字符串、整数、tuple、None等都是不可变的，因此可以放心的作为key使用(注意，若tuple中含有list元素，则不可以作为key使用)。而list和dict是可变的，就不能作为key。  
- key不能重复。

### set
set和dict类似，也是一组key的集合，但不存储value。  
**定义**  
要创建一个set，需要提供一个list作为输入集合:  
```
>>> s = set([1,2,3])
>>> s
{1, 2, 3}
```
注意:虽然传入的参数是一个list，是有序的，但是生成的set中的元素是无序的，只是表面`s`中有1,2,3这三个元素而已。  
对于重复元素，在set中会被自动过滤:  
```
>>> s = set({1,1,2,2,3,3,3})
>>> s
{1, 2, 3}
```
**添加和删除元素**  

- 通过`add(key)`方法添加元素到set中，可重复添加，但不会有效果:  
```
>>> s.add(4)
>>> s
{1, 2, 3, 4}
```
- 通过`remove(key)`方法删除元素:  
```
>>> s.remove(2)
>>> s
{1, 3, 4}
```
**交集和并集**  
set可以看出数学上无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作:  
```
>>> s1 = set([1,2,3])
>>> s2 = set([2,3,4])
>>> s1 & s2
{2, 3}
>>> s1 | s2
{1, 2, 3, 4}
```

---
# 三、函数
## 调用函数
要调用一个函数，需要知道其名称和参数，可以查阅[Python官方函数文档](http://docs.python.org/3/library/functions.html#abs)来获取这些信息。  
也可以在交互式命令行通过`help(function_name)`来查看某函数的帮助信息。  
在调用函数时，如果传入的参数数量不对或类型错误，会报`TypeError`的错误，并给出报错信息。  
**函数名**:其实是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个"别名":  
```
>>> a = abs # 变量a指向abs函数
>>> a(-1) # 所以也可以通过a调用abs函数
1
```
## 定义函数
在Python中，定义一个函数要使用`def`语句，依次写出函数名、括号、括号中的参数和冒号`:`，然后，在缩进块中编写函数体，函数的返回值用`return`语句返回。  
举例说明:定义一个求幂函数:  
```
def power(x, y):#y只能为正整数
    i=1
    result=x
    while i<y:
        result=result*x
        i=i+1
    return result
```
### 返回值
函数体内部的语句在执行时，一旦执行到`return`时，函数就执行完毕，并将结果返回。  
如果没有`return`语句，函数执行完毕后也会返回结果，只是结果为`None`。`return None`可以简写为‘return’。  

### 交互环境定义函数
Python会出现`...`的提示，函数定义结束以后需要按两次回车重新回到`>>>`提示符下。  

## 空函数
如果想定义一个什么事也不做的空函数，可以用`pass`语句:  
```
def nop():
    pass
```
`pass`也可以用在其他语句中，在程序未完全想好之前做占位符使用。  

## 参数检查
数据类型的检查可以通过内置函数`isinstance()`实现，举例如下:  
```
def power(x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, int):  # 对参数类型做检查
        raise TypeError('bad operand type')
    i = 0
    result = 1
    while i < abs(y):
        if y >= 0:
            result = result*x
        else:
            result = result/x
        i = i+1
    return result
```
详细用法如下:  
```
isinstance(object, classinfo)
```
参数:  

- object:实例对象
- classinfo:可以使直接或间接类名、基本类型或由它们组成的tuple。  

返回值: 如果对象类型与参数2类型相同则返回`True`，否则返回`False`。

## 返回多个值
在实际应用中，常常需要函数返回多个值。比如在游戏中，从一个点移动到另一点，给出现坐标、位移和角度，就可以计算出新的坐标:  
```
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx,ny
```
这样，我们就获得了两个返回值:
```
>>> x, y = move(100, 100, 60, math.pi / 6)
>>> print(x, y)
151.96152422706632 70.0
```
但其实这是一种假象，Python函数返回的仍然是单一值:  
```
>>> r = move(100, 100, 60, math.pi / 6)
>>> print(r)
(151.96152422706632, 70.0)
```
可以看出，返回值其实是一个tuple。但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值。  

## 函数的参数
Python的函数定义非常简单，但灵活度很大。除了正常定义的必选参数外，还可以使用默认参数、可变参数和关键字参数，使得函数定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码。  
### 位置参数
例如上面定义的计算幂的函数`power(x,y)`就有两个参数:`x`和`y`，这两个参数都是位置参数，调用函数时，传入的两个值按照位置顺序依次赋值给参数`x`和`y`。
### 默认参数
仍考虑函数`power(x,y)`，由于我们经常会需要计算一个数的平方，所以完全可以将第二个参数的默认值设定为2:  
```
def power(x, y=2):
    pass
```
这样当我们调用`power(5)`时，相当于调用了`power(5, 2)`:  
```
>>> power(5)
25
```
而对于其他情况，则必须明确的传入'y',例如`power(5 ,4)`。  
设置默认参数时，以下几点需要**注意**:  

- 必选参数在前，默认参数在后，否则Python解释器可能会报错；
- 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
- **牢记**默认参数必须指向不变对象，不然可能会出现调用结果错误。

### 可变参数
顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。  
例如，给定一组数字a,b,c......，请计算a^2+b^2+c^2+......。可以利用可变参数定义如下:  
```
def calc(*nums):
    sum=0
    for n in nums:
        sum = sum + n**2
    return sum
```
调用如下:  
```
>>> calc(1,2,3)
14
>>> calc(1,2)
5
>>> calc()
0
```
在函数内部，参数`nums`接收到的其实是一个tuple。  
如果已经有一个list或tuple，要调用一个可变参数，可直接在前面加`*`调用，如下:  
```
>>> n = [1, 4, 5]
>>> calc(*n)
42
```
`*n`表示将这个list中的所有元素作为可变参数传进去，这种写法很有用也很常见。  

### 关键字参数
可变参数允许传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。示例如下:  
```
def person(name, age, **kw):
    print('name:',name,'age:',age,'other:',kw)
```
函数`person`除了必选参数`name`和`age`之外，还接受关键字参数`kw`。在调用该函数时，可以只传入必选参数:  
```
>>> person('Lisa',10)
name: Lisa age: 10 other: {}
```
也可以传入任意个数的关键字参数:
```
>>> person('Bob', 30, city='Tokyo', job='teacher')
name: Bob age: 30 other: {'city': 'Tokyo', 'job': 'teacher'}
```
可见，关键字参数可以扩展函数的功能。  
和可变参数类似，也可以先组装一个dict，再将其转换为关键字参数传递进去:  
```
>>> extra = {'city': 'Tokyo', 'job': 'teacher'}
>>> person('Bob', 30, **extra)
name: Bob age: 30 other: {'city': 'Tokyo', 'job': 'teacher'}
```
`**extra`表示把`extra`这个dict的所有key-value用关键字参数传入到函数的\*\*kw参数，`kw`将获得一个dict，注意`kw`获得的dict是extra的一份拷贝，对`kw`的改动不会影响到函数外的`extra`。

### 命名关键字参数
对于关键字参数，函数调用者可以传入任意不受限制的关键字参数。但是如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收`city`和`job`作为关键字参数。此时可以用命名关键字参数，如下:  
```
def person(name, age, *, city, job):
    print(name,age,city,job)
```
和关键字参数`**kw`不同，命名关键字参数需要一个特殊的分隔符`*`，分隔符后面的参数被视为命名关键字参数。  
调用方式和关键字参数相同。  
如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要分隔符`*`了:  
```
def person(name, age, *args, city, job):
    print(name, age, args, city, job)
```
命名关键字参数必须传入参数名，这和位置参数不同。若没有参数名，调用将报错:  
```
>>> person('hiro', 15, 'tokyo', 'student') 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: person() missing 2 required keyword-only arguments: 'city' and 'job
>>> person('hiro', 15,city='tokyo',job='student')
hiro 15 () tokyo student
```
由于调用时缺少参数名`city`和`job`，Python解释器把这4个参数均视为位置参数，但`person()`函数仅接受2个位置参数。  
命名关键字参数可以有缺省值，从而简化调用:  
```
def person(name, age, *args, city='Tokyo', job):
    print(name, age, args, city, job)
```
由于命名关键字参数`city`具有默认值，故调用时可以不传入`city`参数。  

### 参数组合
在Python中定义函数时，可以用必选参数、默认参数、可变参数、关键字参数、和命名关键字参数，这五种参数组合使用。但是需要注意的是，**参数定义的顺序必须是**:必选参数-默认参数-可变参数-命名关键字参数-关键字参数。  
比如定义一个函数:  
```
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
```
函数调用时，Python解释器会自动按照参数位置和参数名把对应的参数传进去。  
```
>>> f1(1, 2, 3, 4, 5, x=6, y=7)
a = 1 b = 2 c = 3 args = (4, 5) kw = {'x': 6, 'y': 7}
>>> f2(1, 2, d='kunimi hiro', x='amamiya hikari', y='tachibana hideo')
a = 1 b = 2 c = 0 d = kunimi hiro kw = {'x': 'amamiya hikari', 'y': 'tachibana hideo'}
```
另外，通过一个tuple和一个dict，也可以实现上述函数的调用:
```
>>> tp1 = (1, 2, 3, 4, 5)
>>> dic1 = {'x': 6, 'y': 7}
>>> f1(*tp1, **dic1)
a = 1 b = 2 c = 3 args = (4, 5) kw = {'x': 6, 'y': 7}
>>> tp2 = (1, 2)
>>> dic2 = {'d':'kunimi hiro', 'x': 'amamiya hikari', 'y': 'tachibana hideo'}
>>> f2(*tp2, **dic2)
a = 1 b = 2 c = 0 d = kunimi hiro kw = {'x': 'amamiya hikari', 'y': 'tachibana hideo'}
```
可见，对于任意函数，都可以通过类似`func(*args, **kw)`的形式调用它，无论其参数是如何定义的。  

## 递归函数
在函数内部，可以调用其他函数。如果一个函数在内部调用自身，这个函数就是递归函数。  
例如计算阶乘:`n! = 1×2×3×...×n`，用函数`fact(n)`表示，可写作`fact(n)=fact(n-1)×n`，只有`n=1`时需要特殊处理。用递归的方式写出来就是:  
```
def fact(n):
    if n==1:
        return 1
    else:
        return fact(n-1)*n
```
递归函数优点是定义简单、逻辑清晰。理论上来讲，所有递归函数都可以写成循环的形式，但循环的逻辑不如递归清晰。而递归函数的缺点是容易造成栈溢出，在计算机中，函数调用是通过栈(stack)这种数据结构来实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，故调用次数过多，会导致栈溢出。  

解决递归调用栈溢出的方法是通过**尾递归**优化，尾递归是指，在函数返回时，调用自身，并且`return`语句不能包含表达式。这样编译器或解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。  

然而，遗憾的是大多数编程语言都没有针对尾递归做优化，Python解释器也没有做优化，所以即使改成尾递归的形式也是会导致栈溢出的。  

---

# 四、高级特性

## 切片(Slice)
切片操作符是用来取一个list或tuple中的部分元素，例如:  
```
>>> L=['hiro', 'hideo', 'hikari', 'haruka', 'tatsuya', 'minami']
>>> L[0:3]
['hiro', 'hideo', 'hikari']
```
`L[0:3]`表示，从索引`0`开始取，直到索引`3`为止，但不包括索引`3`。即取出了索引`0`、'1'、'2'三个元素。  

如果第一个索引是`0`，还可以省略:  
```
>>> L[:3]
['hiro', 'hideo', 'hikari']
```
类似的，既然Python支持`L[-1]`取倒数第一个元素，那么它同样支持倒数切片，如下:  
```
>>> L[-3:-1]
['haruka', 'tatsuya']
>>> L[-3:]
['haruka', 'tatsuya', 'minami']
```
还可以设置步长取出元素，例如前5个元素，每两个取一个:  
```
>>> L[:5:2]
['hiro', 'hikari', 'tatsuya']
```
甚至什么都不写，只写`[:]`就可以原样复制一个list:  
```
>>> L[:]
['hiro', 'hideo', 'hikari', 'haruka', 'tatsuya', 'minami']
```

tuple也是一种list，唯一的区别在于tuple不可变。因此tuple也可以用切片操作，只是操作结果仍是tuple:  
```
>>> (0,1,2,3,4,5)[:3]
(0,1,2)
```
**字符串也可以看成一种list**，每个元素就是一个字符，因此字符串也可以用切片操作，只是操作结果仍是字符串:  
```
>>> 'abcdef'[:3]
abc
```
## 迭代
如果给定一个list或tuple，我们可以通过`for`循环来遍历这个list或tuple，这种遍历我们称之为迭代(Iteration)。  

在`Python`中，迭代是通过`for...in`来完成的。相对于其他使用下标完成迭代的语言，Python的`for`循环抽象程度是要高于它们的，因为Python的`for`循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上。  

list这种数据类型是有下标的，但在Python中，只要是可迭代对象，无论有无下标，都可以迭代，比如**dict**:  
```
>>> d = {'a': 1, 'b': 2, 'c': 3}
>>> for k in d:
... print(k)
...
...
b
c
a
```
由于dict的存储不是按照list的方式顺序排列的，所以迭代出的结果顺序可能不一样。  

从以上程序可以看出，默认情况下，dict迭代的是key。如果要迭代value，可以用`for value in d.values()`，如果要同时迭代key和value，可以用`for k,v in d.items()`分别得到key和value，或用`for kv in d.items()`得到一个包含key和value的tuple。  

**字符串也是可迭代对象**，也可用于`for`循环:  
```
>>> for ch in 'Hiro'
...     print(ch)
...
H
i
r
o
```
### 判断一个对象是否是可迭代对象
通过`collections`模块的`Iterable`类型判断:  
```
>>> from collections import Iterable
>>> isinstance('tatsuya', Iterable)  # str是否可迭代
True
>>> isinstance(123, Iterable)  # 整数是否可迭代
False
```
如果要对list实现下标循环，可使用Python内置的**`enumerate`函数**，将一个list变成索引-元素对，这样就可以在`for`循环中同时迭代索引和元素本身:  
```
for i, value in enumerate(['a', 'b', 'c'])
    print(i, value)
```
## 列表生成式
列表生成式，即List Comprehension，是Python内置的非常简单却强大的可以用来创建list的生成式。  
例如，要生成list`[1×1, 2×2,..., 10×10]`，如果用循环的方法则是:  
```
>>> L = []
>>> for i in range(1,11):
...     L.append(i*i)
...
>>> L
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```
但是循环太繁琐，使用列表生成式则可以用一行语句代替循环生成上面的list:  
```
>>> [x*x for x in range(1,11)]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```
写列表生成式时，把要生成的元素`x * x`放到前面，后面跟`for`循环，就可以把list创建出来，十分有用。  
`for`循环后还可以加上`if`判断，这样我们就可以筛选出仅偶数的平方:  
```
>>> [x * x for x in range(1,11) if x%2 == 0]
[4, 16, 36, 64, 100]
```
还可以使用两层循环，生成全排列:  
```
>>> [m + n for m in 'XYZ' for n in 'ABC']
['XA', 'XB', 'XC', 'YA', 'YB', 'YC', 'ZA', 'ZB', 'ZC']
```
三层和三层以上的循环很少用到。  

由于`for`循环可以同时使用两个甚至多个变量，故列表生成式也可以使用两个变量来生成list:  
```
>>> d = {'h2':'hiro', 'miyuki':'masato', 'touch':'tatsuya' }
>>> [k + '=' + v for k,v in d.items()]
['touch=tatsuya', 'h2=hiro', 'miyuki=masato']
```
## 生成器
通过列表生成式，可以直接创建一个列表。但由于收到内存限制，列表容量是有限的。在Python中，有一种一边循环一边计算的机制，称为生成器:generator。它不用创建完整的list，从而可以节省大量的空间。   

### 创建生成器的方法

- 将列表生成式的`[]`改为`()`就可以得到一个generator
```
>>> g = (x * x for x in range(3))
>>> g
<generator object <genexpr> at 0x7facac806d00>
```
列表生成式创建的list可以被直接打印出来，但如何打印generator的每一个元素呢?  
如果要一个一个打印出来，可以通过`next()`函数获得generator的下一个返回值:  
```
>>> next(g)
0
>>> next(g)
1
>>> next(g)
4
>>> next(g)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```
generator保存的是算法，每次调用`next(g)`，就计算出`g`的下一个元素的值，直到计算到最后一个元素，没有更多元素时，跑出`StopIteration`的错误。  
上面不断调用的方法一般不使用，正常是使用`for`循环，因为**generator也是可迭代对象**，但是需要注意的是，生成器只能读取一次:  
```
>>> g = (x * x for x in range(3))
>>> for n in g:
...     print(n)
...
0
1
4
```

- 如果推算的算法比较复杂，用类似列表生成式的`for`循环无法实现时，还可以用函数来实现。 要成为一个列表生成式，函数中需要包含**关键字`yield`**:  
```
def fib(m):
    n, a, b = 0, 0, 1
    while n < m:
        yield b
        a, b = b, a+b
        n = n+1
    return 'done'
```
这就是定义generator的另一种方法:  
```
>>> f = fib(6)
>>> f
<generator object fib at 0x104feaaa0>
```
**generator的执行流程**:不同于普通函数，普通函数是顺序执行，遇到`return`语句或最后一行函数就返回，而且只能返回一次。但一个生成器只有在每次调用`next()`函数的时候执行，遇到`yield`语句就返回，再次执行时从上次返回的`yield`语句处继续执行。  
要取得返回值，可使用`for`循环迭代:  
```
>>> for n in fib(4):
...     print(n)
...
1
1
2
3
```
但是发现，用`for`循环调用generator时，拿不到generator的`return`语句的返回值。如果想要得到该返回值，必须捕获`StopIteration`错误，返回值包含在`StopIteration`的`value`中。捕获错误的方法在后面的错误处理部分介绍。  

**isgeneration判断**
```
>>> from inspect import isgeneratorfunction
>>> isgeneratorfunction(fab)
True
```

## 迭代器
### 可迭代对象(Iterable)
我们已经知道，可直接作用于`for`循环的数据类型有以下几种:  

- 一类是集合数据类型，如`list`、'tuple'、`dict`、'set'、'str'等；
- 一类是`generator`，包括生成器和带yield的generator function。

这些可直接作用于`for`循环的对象统称为可迭代对象:`Iterable`。  
**判断是否是可迭代对象**
用`isinstance()`判断一个对象是否是`Iterable`对象。  
```
>>> from collections import Iterable
>>> isinstance([], Iterable)
True
>>> isinstance({}, Iterable)
True
>>> isinstance('hiro', Iterable)
True
>>> isinstance(123, Iterable)
False
```
### Iterator对象
通过前面的介绍我们已经知道，生成器不但可以作用于`for`循环，还可以被`nex()`函数不断调用并返回下一个值，直到最后抛出`StopIteration`错误表示无法继续返回下一个值了。

可以被next()函数调用并不断返回下一个值的对象称为迭代器: Iterator。  

**判断是否是Iterator**  
用`isinstance()`判断一个对象是否是`Iterator`对象。  
```
>>> from collections import Iterator
>>> isinstance([], Iterator)
False
>>> isinstance((x*x for x in range(10)), Iterator)
True
>>> isinstance('Hideo', Iterator)
False
```
从上面的例子可以看出，生成器都是`Iterator`对象，同时也是`Iterable`对象；但`list`、'tuple'、`dict`、'set'、'str'等虽然是`Iterable`，却不是`Iterator`。  

### 将Iterable转变为Iterator
把`list`、`dict`、`str`等`Iterable`变成`Iterator`可以使用**`iter()`函数**:  
```
>>> isinstance(iter('Hideo'), Iterator)
True
>>> isinstance(iter([1,2,3]), Iterator)
True
```
### Iterable和Iterator的区别

- Python的`Iterator`对象表示的是一个数据流，它可以被`next()`函数调用，不断返回下一个数据，直到没有数据时抛出`StopIteration`错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以`Iterator`的计算是惰性的，只有在需要返回下一个数据时它才会计算。
- `Iterator`甚至可以表示一个无限大的数据流，例如全体自然数，而使用list是不可能存储全体自然数的。  

---

# 函数式编程(Functional Programming)

函数是Python内建支持的一种封装，通过把大段的代码拆成函数，然后一层一层的调用函数，从而把复杂的任务分解为简单的任务，这种分解可以称为**面向过程的程序设计**。函数就是面向过程的程序设计的基本单元。  

而函数式编程，虽然也可以归结到面向过程的程序设计，但其思想更接近于数学计算。函数式编程是一种抽象程度很高的编程范式，纯粹的函数式编程语言编写的函数没有变量，而Python允许使用变量，故它不是纯函数式编程语言，它只对函数式编程提供部分支持。  

函数式编程的一个特点是:允许把函数本身作为参数传入另一个函数，还允许返回一个函数。  

## 高阶函数(High-order-function)

**变量可以指向函数**  
```
>>> f_abs=abs
>>> f_abs
<built-in function abs>
>>> f_abs(-10)
10
>>> id(f_abs) == id(abs)
True
```
可见函数本身也可以赋值给变量，且变量`f_abs`指向`abs`函数本身。  

**函数名也是变量**  
函数名的本质是一个指向函数的变量:对于`abs()`这个函数，完全可以把函数名`abs`看做一个变量，它指向一个可以计算绝对值的函数。  

如果将`abs`指向其他对象，会导致无法通过`abs(-10)`来调用该函数。  
```
>>> abs = 10
>>> abs(-10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not callable
```
因为此时`abs`这个变量已经不指向求绝对值函数而是指向一个整数`10`，所以实际代码中要注意，定义变量时不要和内置函数名冲突。  

**传入函数**  
既然变量可以指向函数，而函数的参数可以接收变量，故一个函数就可以接收另一个函数作为参数，这种函数就称为高阶函数。  

举例说明:  
```
def add(x, y, f):
    return f(x) + f(y)

def f1(t):
    return t**2

def f2(t):
    return t*3
 #调用
print('r1=',add(-2, -4, f1), 'r2=', add(-2, -4, f2))
```
得到:`r1= 20 r2= -18`，可见两次调用时参数`f`分别接收`f1`和'f2'函数。  

### map/reduce
Python内建了`map()`和`reduce()`函数。  

**`map()`**函数接收两个参数，一个是函数，一个是`Iterable`对象，`map`将传入的函数依次作用到序列的每个元素，并把结果作为新的`Iterator`返回。  

例如:  
```
>>> def f(x):
...     return x**2
... 
>>> list(map(f, [1, 2, 3, 4, 5]))
[1, 4, 9, 16, 25]
```
**reduce()**也接收两个参数，一个是函数，一个是序列。`reduce`把这个函数作用在序列`[x1, x2, x3, ...]`上，该函数必须接收两个参数，`reduce`把结果继续和序列的下一个元素做累积运算，效果如下:  
```
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
```
举例如下，将序列`[1,2,4,6]`转换为整数`1246`:  
```
>>> from functools import reduce
>>> def f(x,y):
...     return 10*x+y
... 
>>> reduce(f, [1, 2, 4, 6])
1246
```
### filter过滤序列
Python内建函数`filter()`用于过滤序列。和`map()`类似，它也接收一个函数和一个Iterab对象。但和`map()`不同的是，`filter()`将传入的函数 依次作用在某个元素，然后根据返回值是`True`或是`False`来决定保留还是丢弃该元素。  
例如，删掉一个list中的偶数，只保留奇数:  
```
>>> a = list(range(1,11))
>>> list(filter(lambda x: x % 2 == 1, a))
[1, 3, 5, 7, 9]
```
注意: `filter()`的返回值是一个`Iterator`，也就是一个惰性序列，所以要强迫其完成计算结果，需要用`list()`函数获得所有结果并返回一个`list`。  

### sorted排序
排序也是程序中经常用到的算法，Python内置的`sorted()`函数可以对list进行排序:  
```
>>> sorted([36, 5, -12, 9, -21])
[-21, -12, 5, 9, 36]
```
此外，`sorted()`也是一个高阶函数，它可以接收一个`key`函数来实现自定义的排序，例如按照绝对值大小排序:  
```
>>> sorted([36, 5, -12, 9, -21], key=abs)
[5, 9, -12, -21, 36]
```
key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序。  

要进行反向排序，不必改动`key`函数，可以传入第三个参数`reverse=True`。
```
>>> sorted([36, 5, -12, 9, -21], key=abs, reverse=True)
[36, -21, -12, 9, 5]
```
## 返回函数
### 函数作为返回值
高阶函数除了可以接受函数作为参数以外，还可以将函数作为返回值。  
例如:  
```
def lazy_sum(*args):
    def my_sum():
        ax = 0
        for n in args:
            ax = ax +n
        return ax
    return my_sum
```
当我们调用`lazy_sum()`时，返回的并不是求和结果，而是求和函数:  
```
>>> f = lazy_sum(*[1, 3, 5, 7, 9])
>>> f
<function lazy_sum.<locals>.mysum at 0x101c6ed90>
```
调用`f`时，才真正计算求和结果:  
```
>>> f()
25
```
上述例子的，内部函数`my_sum`可以引用外部函数的参数和局部变量，当`lazy_sum`返回函数`sum`时，相关参数和变量都保存在返回的函数中，这种程序结构称为**闭包(Closure)**。  
注意:当我们调用`lazy_sum`时，每次调用都会返回一个新的函数。即使传入相同的参数得到的函数也是不同的，它们的调用结果互不影响。  

### 闭包(Closure)
看一个例子:  
```
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs
f1, f2, f3 = count()  # 可将一个list中的元素分别赋值给不同的变量
print(f1())
print(f2())
print(f3())
```
上面的例子中，每次循环都创建了一个新的函数，然后将三个函数都返回了。  
可能期望得到的结果是`1`，`4`，`9`,但实际得到的是`9`，`9`，`9`。  

原因在于返回的函数引用了变量`i`，但它并非立刻执行。等到三个函数都返回时，它们所引用的变量`i`已经变成了`3`，因此最终结果都是`9`。  

**注意: 返回闭包时需要牢记，返回函数不要引用任何循环变量，或后续会发生变化的变量。**  

修改方法见(`~/pylearn/FunctionalProgramming/5_closure_demo.py`)  

## 匿名函数

在我们传入函数时，有时无需显示的定义函数，此时直接传入匿名函数更方便。  
关键字`lambda`表示匿名函数，例如:  
```
>>> f=lambda x: x*x
>>> f
<function <lambda> at 0x7f92a9a0e9d8>
>>> f(2)
4
```
冒号`:`前面的`x`表示函数的参数。匿名函数只能有一个表达式，不用写`return`，返回值就是该表达式的结果。上面例子里的匿名函数`lambda x: x*x`实际上就是:  
```
def f(x):
    return x*x
```
不过匿名函数没有函数名，也正因如此，使用匿名函数不必担心函数名冲突。从上面的例子也可以看出，由于匿名函数是一个函数对象，所以可以将其赋值给一个变量，通过该变量来调用函数也是可行的。  

同样的，也可以把匿名函数作为返回值返回，例如:  
```
>>> def b(x, y):
...     return lambda: x+y
... 
>>> b(1,2)
<function b.<locals>.<lambda> at 0x7f92a7636a60>
```
## 装饰器
比如有一个函数`now()`，假设我们要增强该函数的功能，如在函数调用前后自动打印日志，但又不希望修改`now()`函数的定义，此时可以用到装饰器，它是一种可以在代码运行期间动态增加功能的方式。  
```
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
```
上面就是一个decorator的例子。本质上，装饰器就是一个返回函数的高阶函数。用法如下:  
```
@log
def now(n):
    print('2018-1-9',n)
```
要借助Python的@语法，将decorator至于函数的定义出。把`@log`放到`now()`函数的定义处，相当于执行了语句：  
```
now = log(now)
```
由于`log()`是一个decorator，返回一个函数，所以原来的`now()`函数仍存在，只不过现在同名的`now`变量指向了新的函数，于是调用`now()`将执行新函数，即在`log()`函数中返回的`wrapper()`函数。  

`wrpper()`函数的参数定义是`(*args, **kw)`，因此它可以接受任意参数的调用。在`wrpper()`函数内，首先打印日志，再紧接着调用原始函数。  
过程如下:  
```
now(3)
>>> log(now)(3) >>> wrapper(3) >>> now(3)
```
由于函数也是一种对象，它有`__name__`等属性，但检查后可发现，经过decorator装饰后的数，它们的`__name__`已经从原来的`now`变成了`wrapper`:  
```
>>> now.__name__
'wrapper'
```
因为返回的那个`wrapper()`函数名字就是'wrapper'，所以，需要把原始函数的`__name__`等属性复制到`wrapper()`函数中，否则，有些依赖函数签名的代码执行就会出错。  
不需要编写`wrapper.__name__ = func.__name__`这样的代码，Python内置的`functools.wraps`就是干这个事的，所以，一个完整的`decorator`的写法如下：  
```
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
```
**注意**:在面向对象的设计模式中，decorator被称为装饰模式。OOP的装饰模式需要通过继承和组合来实现。  
所以，Python的decorator可以用函数实现，也可以用类实现。  

## 偏函数
Python里的偏函数和数学上的偏函数概念不同，它存在于functools模块中，`functools.partial()`可以帮助我们创建一个偏函数，例如:  
```
>>> import functools as ft
>>> int2 = ft.partial(int, base=2)
>>> int2('1010101')
85
```
可以看出，`functools.partial()`的作用是，将一个函数的某些参数固定住，也就是设置默认值，返回一个新的函数，调用这个新函数会更加方便。  
同时注意到例子中新的`int2()`函数，仅仅是把`int()`函数的`base`参数重新设定默认值为`2`，这时也可以在函数调用时传入其他值:  
```
>>> int2('121212', base=3)
455
```
**注意**创建偏函数时，实际上可以接收函数对象、`*args`和`**kw`这三个参数。在上述第一个例子中，实际上是相当于传入了:  
```
kw = {'base': 2}
int('1010101', **kw)
```
而当传入:  
```
max2 = ft.partial(max, 10)
```
此时，实际上会将`10`作为`*args`的一部分加到左边，即:  
```
max2(1,3,5)
10
```
相当于:  
```
args = (10, 1, 3, 5)
max(*args)
10
```
**使用**:当函数的参数过多，需要简化时，可使用`functools.partial()`创建一个新的函数，这个函数可固定住原函数的部分参数，从而简化调用。  

---

# 模块(Module)
为了使代码更易于维护，我们把很多函数分组，放在不同的文件里，这样每个文件包含的代码就相对较少。在Python中，一个`.py`文件就称之为一个模块(Module)。  

## 使用模块
**使用模块的好处**  

- 提高可代码的可维护性
- 编写代码不必从零开始，Python有许多内置模块和第三方模块。
- 避免函数名和变量名冲突，相同名字的函数和变量完全可以分别存在于不同的模块中。但是也要注意，尽量不要与内置函数名字冲突。
- 为了避免模块名冲突，Python还引入了按目录来组织模块的方法，称为包(Package)。  
例如，一个`h2.py`的文件就是一个名字叫做`h2`的模块，同样的，一个叫做`touch.py`的文件就是一个名为`touch`的模块。  

现在假设`h2`模块和`touch`模块与其他模块名字冲突了，这时我们可以通过包来组织模块，方法是选择一个顶层包名，比如`mycomics`，按照如下目录存放:  
```
mycomics
├─ __init__.py
├─ h2.py
└─ touch.py
```
这时，只要顶层包名不与别人的冲突，那所有模块都不会与别人的冲突。现在，`h2`和`touch`模块的名字就变成了`mycomics.h2`和`mycomics.touch`。  

**注意**:每个package目录下面都会有一个`__init__.py`文件，这个文件是必须存在的，否则Python将把这个目录视为普通目录，而不是一个包。`__init__.py`可以是空文件，也可以有Python代码，因为`__init__.py`本身就是一个模块，它的模块名为`mycomics`。  

**多级目录**，如:  
```
mycomics
 ├─ atachi
 │  ├─ __init__.py
 │  ├─ touch.py
 │  └─ h2.py
 ├─ __init__.py
 ├─ touch.py
 └─ orange.py
```
两个`touch.py`的模块名分别为:`mycomic.atachi.touch`和`mycomics.touch`。  

**创建自己的模块时要注意**  

- 模块名要遵循Python变量命名规范，不要使用中文或特殊符号；注:标识符第一个字符必须为字母或下划线，不可以是数字。
- 模块名不要和系统模块名冲突，最好先查看系统是否已存在该模块，检查方法是在交互环境下执行`import xxx`，若成功则说明系统已存在此模块。  

### 作用域
在一个模块中，有的函数和变量我们希望给别人使用，有的希望仅在模块内部使用。区分作用域，在Python中是通过前缀`_`来实现的。  

正常的函数和变量名是公开的(public)，可以被直接引用，比如: `a`,'x123','PI'等。  

类似`__xxx__`这样的变量是特殊变量，可以被直接引用，但有其特殊的用途，例如:`__author__`,`__name__`就是特殊变量，模块内定义的文档注释可以用特殊变量`__doc__`来访问，我们自己的变量一般不要用这种变量名。  

类似`_xxx`和`__xxx`这样的函数或变量就是非公开的(private)，不应该被直接引用。  

之所以说私有的函数或变量"不应该"被直接引用，而不是"不能"，是因为Python并没有一种方法可以完全限制访问private函数或变量，但是从编程习惯来讲不应引用private函数或变量。  

**注**:将外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。  

---

# 面向对象编程
Object Oriented Programming，简称OOP，是一种程序设计思想。它将对象作程序的基本单元，一个对象包含了数据和操作数据的函数。  

面向过程的程序设计把计算机程序视为一系列的命令集合，即一组函数的顺序执行。为简化程序设计，面向过程把函数继续切分为子函数，即把大块函数切割为小块函数来降低系统的复杂度。  

而面向对象的程序设计把计算机程序视为一组对象的集合，每个对象都可以接收其他对象发过来的消息，并处理这些消息，计算机程序的执行就是一系列消息在各个对象之间传递。  

在Python中，所有数据类型都可以视为对象，也可以自定义对象，自定义的对象数据类型就是面向对象中类(class)的概念。  

面对对象的设计思想是从自然界中来的，因为在自然界中，类(Class)和实例(Instance)的概念是很自然的。Class是一种抽象概念，比如我们定义一个Class为`Student`，指学生这个概念，而实例(Instance)则是一个个具体的`Student`，例如，Bart和Lisa。  
给对象发消息其实就是调用对象对应的关联函数，我们称之为对象的方法(Method)。  

所有，面向对象的设计思想是抽象出Class，根据Class创建Instance。其抽象成程度要高于函数，因为一个Class既包含数据，又包含操作数据的方法。  

## 类和实例
面向对象最重要的概念就是类(Class)和实例(Instance)，必须牢记类是抽象的模板，而实例是根据类创建出来的一个个具体的"对象"，每个对象拥有相同的方法，但各自的数据可能不同。  

### 类的定义
在Python中，定义类是通过`class`关键字,`class`后面紧跟着的是类名，即`Student`，类名通常用大写开头的单词，紧接着是`(object)`，表示该类是从哪个类继承下来的。通常如果没有合适的继承类，就使用`object`类，这是所有类都会继承的类。  

例如，下面定义一个`Student`类:  
```
class Student(object):
    pass
```
定义好以后就可以根据它创建实例，创建实例是通过类名+`()`实现的:  
```
>>> bart = Student()
>>> bart
<__main__.Student object at 0x10a67a590>
>>> Student
<class '__main__.Student'>
```
可以看到，变量`Bart`指向的就是一个`Student`的实例，后面的`0x10a67a590`是内存地址，每个object的地址都不一样，而`Student`本身是一个类。  

可以给一个实例自由绑定属性，比如:  

```
>>> bart.name = 'Bart Simpson'
>>> bart.score = 59
```
由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。通过定义一个特殊的`__init__`方法，在创建实例的时候，就把`name`，`score`等属性绑上去：  
```
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score
```
注意到`__init__`方法的第一个参数永远是`self`，表示创建的实例本身，因此，在`__init__`方法内部，就可以把各种属性绑定到`self`，因为`self`就指向创建的实例本身。  

有了`__init__`方法，在创建实例的时候，就不能传入空的参数了，必须传入与`__init__`方法匹配的参数，但`self`不需要传，Python解释器自己会把实例变量传进去。  

和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量`self`，并且，调用时，不用传递该参数。除此之外，类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数。  

### 数据封装
面向对象编程的一个重要的特点就是数据封装。也就是在类内部定义访问实例本身数据的函数，这些封装数据的函数是和类本身关联起来的，我们称之为类的方法:  
```
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))
```
要定义一个方法，除了第一个参数是`self`外，其他和普通函数一样。要调用一个方法，只需要在实例变量上直接调用，除了`self`不用传递，其他参数正常传入：
```
>>> bart.print_score()
Bart Simpson: 59
```
这样一来，我们从外部看`Student`类，就只需要知道，创建实例需要给出`name`和`score`，而如何打印是在类内部定义的，这些数据和逻辑被封装了起来，调用时无需知道内部实现的细节。  

**注意**:和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称却可能不同。  

## 访问限制
在Class内部，可以有属性和方法，外部变量可以通过直接调用实例变量的方法来操作数据，这样就隐藏了内部的复杂逻辑。  

但是，从前面的例子可以看出，外部代码还是可以自由的修改一个实例的`name`，`score`等属性:  
```
>>> bart = Student('Bart simpson', 59)
>>> bart.score = 99
>>> bart.score
99
```
此时，如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线`__`，这样它就变成了一个私有变量(private)，只有内部可以访问，外部不能访问:  
```
class Student():
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
```
改完后则无法外部访问name和score属性了:  
```
>>> import a_class_demo2 as cls2
>>> bart = cls2.Student("Bart Simpson", 59)
>>> bart.__name
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute '__name'
>>> bart.print_score()
Bart Simpson: 59
```
如果外部代码要获取name和score，可以给`Student`类增加类似`get_name`这样的方法:  
```
class Student(object):
    ...

    def get_name(self):
        return self.__name
```
**注意**  

- 有些时候，会看到以一个下划线开头的实例变量名，比如`_name`，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。
- 双下划线开头的实例变量其实也不是一定不能从外部访问，不能直接访问`__name`是因为Python解释器对外将`__name`改成了`_Student__name`，所以仍可以通过`_Student__name`来访问该变量:  
```
>>> bart._Student__name
'Bart Simpson'
```
但是建议不要这样做，因为不同版本的Python解释器可能会把`__name`改成不同的变量名。  

## 继承和多态
在OOP设计中，当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类(Subclass)，而被继承的class称为父类、基类或超类(Base class、Super class)。  

比如，我们已经编写了一个名为`Animal`的class，有一个`run()`方法可以调用:  
```
>>> class Animal(object):
...     def run(self):
...             print('Animal is running...')
```
当我们需要编写`Dog`类时，就可以直接从`Animal`类继承:
```
>>> class Dog(Animal):
        pass
```
对于`Dog`而言，`Animal`就是他的父类，而`Dog`就是`Animal`的子类。继承以后，子类获得了父类的全部功能:  
```
>>> pang = Dog()
>>> pang.run()
Animal is running...
```
**子类继承父类的属性**:需要在子类的`__init__()`方法中调用父类的`__init__()`:  
```
class Plant(object):  # 父类
    def __init__(self, color):
        self.color = color


class Tree(Plant):  # Plant的子类
    def __init__(self, height, age, color='green'):
        # Plant.__init__(self, color)  # 在子类中调用父类的属性--方法一
        super().__init__(color)  # 在子类中调用父类属性--方法二
        self.height = height
        self.age = age
```
**注意**:当子类和父类存在相同的`run()`方法时，子类的`run()`方法会覆盖父类的`run()`方法，在代码运行时，总是调用子类的`run`。  

这样，我们就获得了继承的另一个好处--多态。  

**关于数据类型**:当我们定义一个class时，我们实际上就定义了一种数据类型。我们定义的数据类型和Python自带的数据类型，比如str,list,dict等没什么两样:  
```
a = list() # a是list类型
b = Animal() # b是Animal类型
c = Dog() # c是Dog类型
```
判断一个变量是否是某个类型可以用`isinstance()`判断:  
```
>>> isinstance(a, list)
True
>>> isinstance(b, Animal)
True
>>> isinstance(c, Dog)
True
```
考虑到继承关系，我们尝试:  
```
>>> isinstance(c, Animal)
True
>>> isinstance(b, Dog)
False
```
可见，在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被视为父类，但是反过来是不可以的。  

现在将`Dog`修改为:  
```
class Dog(Animal):
    def run(self):
        print(Dog is running)
```
再增加一个新的子类`Cat`:  
```
class Cat(Animal):
    def run(self):
        print(cat is running)
```
定义一个函数`run_twice()`，该函数接收`Animal`类型的参数:  
```
def run_twice(animal):
    animal.run()
    animal.run()
```
当我们分别传入`Animal`、`Dog`、'Cat'的实例时，run_twice()就打印出：  
```
>>> run_twice(Animal())
Animal is running...
Animal is running...
>>> run_twice(Dog())
Dog is running...
Dog is running...
>>> run_twice(Cat())
Cat is running...
Cat is running...
```
多态的好处就是，当我们需要传入`Dog`、'Cat'或者其他拥有`run()`方法的`Animal`子类实例时，我们只需要接收`Animal`类型，然后按照父类操作就可以了。由于`Animal`类型有`run()`方法，因此，传入任意类型，只要是`Animal`类或其子类，就会自动调用实际类型的`run()`方法。  

这就是著名的**"开闭"原则**:  

- 对扩展开放: 允许新增`Animal`子类；
- 对修改封闭: 不需要依赖修改`Animal`类型的`run_twice()`等函数，只要保证各个子类中的`run()`方法编写正确即可。  

继承还可以一级一级的继承下来，而任何类最终都可以追溯到根类object。  

### 静态语言和动态语言
对于静态语言(如Java)来讲，如果需要传入`Animal`类型，则传入的对象必须是`Animal`类型或其子类，否则将无法调用`run()`方法。  

而对于Python这样的动态语言来说，则不一定需要传入`Animal`类型，只需要保证传入的对象有一个`run()`方法就可以了。  

这就是动态语言的**"鸭子类型"**，它并不要求严格的继承体系，一个对象只要"看起来像鸭子，走起路来像鸭子"，那它就可以被视为鸭子。  

Python的"file-like object"就是一种鸭子类型。对于真正的文件对象，有一个`read()`方法，返回其内容。但是，许多其他对象，只要有`read()`方法，都被视为"file-like object"。  

因此，动态语言的鸭子类型特点，决定了继承不像静态语言那样是必须的。  

## 获取对象的信息

### 使用type()
在Python中，常用内置函数`type()`来判断一个对象的类型:  
例如基本类型:  
```
>>> type(123)
<class 'int'>
>>> type('hikari')
<class 'str'>
>>> type(None)
<class 'NoneType'>
>>> type(True)
<class 'bool'>
```
如果一个变量指向函数或者类，也可以用`type()`来判断:  
```
>>> type(type)
<class 'type'>
>>> type(sum)
<class 'builtin_function_or_method'>
```
`type()`函数返回的是对应的Class类型，如要在`if`语句中判断，则需要比较两个变量的type类型是否相同:  
```
>>> type(sum) == type(abs)
True
>>> type('hiro') == int
False
```
判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：  
```
>>> def fn():
...     pass
...
>>> type(fn)
<class 'function'>
>>> import types
>>> type(fn) == types.FunctionType
True
>>> type(sum) == types.BuiltinFunctionType
True
>>> type(lambda x: x**2) == types.LambdaType
True
>>> type((x**2 for x in range (10))) == types.GeneratorType
True
```
### 使用isinstance()
虽然`type()`可以用来判断一些对象的类型，但对于class的继承关系，使用它就很不方便。  

**type()和isinstance()的区别**  

- `type()`不会认为子类是一种父类类型；
- `isinstance()`考虑了继承关系，它会认为子类是一种父类类型。

在此基础上，能用`type()`判断的基本类型也可以用`isinstance()`判断。  

并且，`isinstance()`还可以判断一个变量是否是某些类型中的一种，如:  
```
>>> isinstance([1, 2, 3], (list, tuple))
True
```
因此，总是优先选择使用`isinstance()`判断对象类型，可以将指定类型及其子类"一网打尽"。  

### 使用dir()
如果要获得一个对象的所有属性和方法，可以使用`dir()`函数，它返回一个包含字符串的list，如:  
```
>>> dir(['h2', 'touch'])
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__
ibute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```
其中，类似`__xxx__`的属性和方法在Python中是有特殊用途的，比如`__len__`方法返回长度。在Python中，如果调用`len()`函数试图获取一个对象的长度，实际上，在`len()`函数内部，它会自动去调用该对象的`__len__()`方法，所以，下面的代码是等价的:  
```
>>> len('abc')
3
>>> 'abc'.__len__()
3
```
如果我们自己写的类，也想用`len()`函数去调用的话，就需要自己写一个`__len__()`方法。  

配合`getattr()`、`setattr()`以及`hasattr()`，我们可以直接操作一个对象的状态:  
```
>>> class Myobject(object):
...     def __init__(self):
...             self.x = 9
...     def power(self):
...             return (self.x)**2
... 
>>> obj = Myobject()
```
测试对象的属性:  
```
>>> hasattr(obj, 'x')  # 有属性'x'吗?
True
>>> obj.x  # 获取属性‘x’
9
>>> hasattr(obj, 'y')  # 有属性‘y’吗?
False
>>> setattr(obj, 'y', 100)  # 设置一个属性‘y’
>>> getattr(obj, 'y')  # 获取属性‘y’
100
```
如果试图获取的属性不存在，会抛出`Attribute Error`，可以传入一个default参数，若属性不存在，则返回默认值:  
```
>>> getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404
404
```
也可以获取对象的方法:  
```
>>> hasattr(obj, 'power') # 有属性'power'吗？
True
>>> getattr(obj, 'power') # 获取属性'power'
<bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
>>> fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
>>> fn # fn指向obj.power
<bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
>>> fn() # 调用fn()与调用obj.power()是一样的
81
```

## 实例属性和类属性
可以在class中定义属性，这种属性是类属性，归该类所有。  

当我们定义了一个类属性后，这个属性虽然归类所有，但类的所有实例都可以访问到。  

不要对实例属性和类属性使用相同的名字，这样用实例访问类属性时，实例属性会覆盖掉类属性，产生难以发现的错误。  

---

# 面向对象高级编程

数据封装、继承和多态只是面向对象程序设计中最基础的3个概念。在Python中，面向对象还有很多高级特性。  

## 使用__slots__

如果在实例定义中，想要限制其属性，如只允许对Student实例添加`name`和`age`属性。  

为达到该目的，Python允许在定义class的时候，定义一个特殊的`__slots__`变量，来限制class实例能添加的属性:  
```
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
```
然后尝试创建实例并给它绑定属性:  
```
>>> s = Student()
>>> s.name = 'Azuma'
>>> s.age = 27
>>> s.score = 99
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'score'
```
由于`score`没有被加入到`__slots__`中，所以不能绑定`score`属性。  

**注意**:`__slots__`定义的属性仅对当前类实例起作用，对继承的子类是不起作用的。  
除非在子类中也定义`__slots__`，这样子类实例允许定义的属性就是自身的`__slots__`加上父类的`__slots__`。

## 使用@property
Python内置的`@property`装饰器是用来将一个方法编程属性调用的:  
```python
class Student(object):

    @property
    def birth(self):  # 相当于getter方法
        return self._birth

    @birth.setter
    def birth(self, value):   # 相当于setter方法
        self._birth = value

    @property
    def age(self):  # 没有setter方法就是只读属性
        return 2015 - self._birth
```

## 多重继承

继承是面向对象编程的一个重要的方式，因为通过继承，子类就可以扩展父类的功能。  

假设我们要实现以下四种动物:  

- Dog-狗
- Bat-蝙蝠
- Parrot-鹦鹉
- Ostrich-鸵鸟

如果按照哺乳动物和鸟类归类，我们可以设计出这样的层次:  
```
Animal
├─ Mammal────|── Dog
|            └─ Bat
└─ Bird───|─ Parrot
          └─ Ostrich
```
如果按照"能跑"和"能飞"归类，我们可以设计出这样的层次:  
```
Animal
├─ Runnable────|── Dog
|              └─ Ostrich
└─ Flyable───|─ Parrot
             └─ Bat
```
如果要把上面两种分类都包含进来，就需要设计更多的层次。这样一来，类的层次就会变得非常复杂。  

正确的做法是采用多重继承，通过多重继承，一个子类就可以获得多个父类的所有功能。(程序示例见c_multi_inherit_demo.py)  

在设计类的继承关系时，通常，主线都是单一继承下来的。但是，如果需要“混入”额外的功能，通过多重继承就可以实现，这种设计通常称之为**MixIn**。  

MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系。  

## 定制类

前面介绍了两种形如`__xxx__`的变量或函数名，即`__len__()`和`__slots__`,这些在Python中是有特殊用途的。除此之外，Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类。  

- `__str__`和`__repr__`
可以用来定义用户看到的字符串和程序开发者看到的字符串
- `__iter__`和`__next__`
如果一个类想要被用于`for`循环，类似list或tuple那样，就必须实现一个`__iter__()`方法，该方法返回一个迭代对象，然后Python的`for`循环就会不断调用该迭代对象的`__next__()`方法拿到循环的下一个值，直到遇到`StopIteration`错误时退出循环。  
- `__getattr__`
在寻找某不存在的属性时，Python会自动调用`__getattr__()`方法。
- `__call__`
任何类，只需要定义一个`__call__()`方法，就可以直接对该实例进行调用。  
`__call__()`还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。  
判断一个对象是否是函数，很多时候是看该对象是否能被调用(能调用不一定是真函数)，能被调用就是一个`Callable`对象，比如普通的函数和带有`__call()__`的类实例。

## 使用枚举类

### type()
动态语言和静态语言最大的不同，就是函数和类的定义。动态语言不是编译时定义的，而是运行时动态创建的。  

`type()`函数可以查看一个类型或变量的类型。  

我们说class的定义是动态运行时创建的，而创建class的方法就是使用`type()`函数。  

`type()`函数既可以返回一个对象的类型，又可以创建出新的类型。比如，我们可以通过`type()`函数创建出`Student`类，而无需通过`class Student(object) ...`定义:  
```
def init_fun(self, name):
    self.name = name

def hello_name(self):
    print('hello, %s' % self.name)
    
Student = type('Student', (object,), dict(__init__=init_fun, hello=hello_name ))
hiro = Student('Kunimi Hiro')
hiro.hello()
```
要创建一个class对象，`type()`函数需要依次传入3个参数:  

1. class的名称；
2. 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法;
3. class的方法名称与函数绑定，这里我们把函数`fn`绑定到方法名`hello`上。  

### metaclass

除了使用`type()`动态创建类以外，要控制类的创建行为，还可以使用metaclass。  
具体解释见[廖雪峰的Python教程--使用元类](https://www.liaoxuefeng.com/wiki)  

---

# 错误、调试和测试

## 错误处理

**try...excpet...finally**  
当我们认为某段代码可能会出错时，就可以用`try`来执行这段代码，如果执行出错，则后续代码不会继续执行，而是直接跳转到错误处理代码，即`except`语句块，执行完`except`后，如果有`finally`语句块，则执行`finally`语句块，至此，执行完毕。  

Python的错误其实也是class，所有的错误类型都继承自`BaseException`，所以使用`except`时要注意，它不但捕获该类型的错误，还把其子类也"一网打尽"。例如:  
```
try:
    foo()
except ValueError as e:
    print('ValueError')
except UnicodeError as e:
    print('UnicodeError')
```
第二个`except`永远也捕获不到`UnicodeError`，因为它是`ValueError`的子类。  

[常见的错误类型和继承关系](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)  

使用`try...except...finally`还有一个巨大的好处，就是可以跨越多层调用，比如`main()`调用`foo()`，`foo()`调用`bar()`，结果`bar()`出错了，这时只要`main()`捕获到了，就可以对其进行处理。  

### 调用栈

如果错误没有被捕获，他就会一直向上抛，最后被Python解释器捕获，打印一个错误信息，然后退出程序。  

**注意**:出错时一定要分析错误的调用栈信息，才能定位错误的位置(从上往下看)。  

### 自定义错误类型

因为错误是class，捕获一个错误就是捕获到该class的一个实例。因此，错误并不是凭空产生的，而是有意创建并抛出的。Python的内置函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误。  

如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例。  

## 调试

程序能一次写完并正常运行的概率很小，总会有各种各样的bug需要修正。因此，需要一整套调试程序的手段来修复bug。  

### 用print打印
最简单粗暴的方法就是把可能有问题的变量打印出来看看。  
使用`print()`最大的坏处是将来还得删掉它，运行结果也会包含很多垃圾信息。所以，有第二种方法。  

### 断言

凡是用`print()`来辅助查看的地方，都可以用断言(assert)来代替:  
```
 # assert_demo.py
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'  # assert的意思是其后的表达式应该是True，否则根据程序运行逻辑，后面的代码肯定会出错
    return 10 / n

def main():
    foo('0')

main()
```
如果断言失败，`assert`语句本身就会抛出`AssertionError`。  

但是如果程序中到处充斥着`assert`，和`print()`相比也好不到哪里去。不过，启动Python解释器时，可以通过`-0`参数来关闭`assert`:  
```
$ python -O assert_demo.py
Traceback (most recent call last):
  ...
ZeroDivisionError: division by zero
```
关闭后，可以把所有的`assert`语句视为`pass`。  

### logging

把`print()`替换为`logging`是第3种方式，和`assert`比，`logging`不会抛出错误，而且可以输出到文件  

### pdb

第四种方式是启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态。  
```
$ python3 -m pdb d_logging_debug.py 
> /home/zhouxiaorui/pylearn/exception_handle/d_logging_debug.py(6)<module>()
-> import logging
```
以参数`-m pdb`启动后，pdb定位到下一步要执行(还未执行)的代码。可以输入命令`l`来查看代码:
```
(Pdb) l
  1  	#!/usr/bin/env python3
  2  	# -*- coding: utf-8 -*-
  3  	# 用logging记录
  4  	
  6  ->	import logging
  7  	logging.basicConfig(level=logging.INFO)  # logging允许指定记录信息的级别
  8  	# 有debug、info、warning、error等几个级别，指定level = INFO时，logging.debug就不起作用了
  9  	# 使用logging的另一个好处是：通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。
```
输入命令`n`可以单步执行代码。  
任何时候都可以输入命令`p 变量名`来查看变量。  
输入命令`q`可以结束调试。  

**pdb.set_trace()**:如果代码过多，但只想测试一部分，可以用这种方法。  
首先在文件中`import pdb`，然后在可能出错的地方放一个`pdb.set_trace()`，就可以设置一个断点:  
```
 # err.py
import pdb

s = '0'
n = int(s)
pdb.set_trace() # 运行到这里会自动暂停
print(10 / n)
```
运行代码，程序会自动在`pdb.set_trace()`处暂停并进入调试环境，可以用命令`p`查看变量，或者命令`c`继续运行。   
这个方法比直接启动pdb单步调试效率要高很多。  

### IDE

如果要比较爽的设置断点、单步执行，就需要一个支持调试功能的IDE，比如pycharm。  

## 单元测试

单元测试是用来对一个模块、一个函数或者一个类来进行正确性检验的测试的。  

如果单元测试通过，说明我们测试的这个函数能够正常工作。如果单元测试不通过，要么函数有bug，要么测试条件输入不正确，总之，需要修复使单元测试能够通过。  

单元测试通过后有什么意义呢？如果我们对某函数代码做了修改，只需要再跑一遍单元测试，如果通过，说明我们的修改不会对该函数原有的行为造成影响，如果测试不通过，说明我们的修改与原有行为不一致，要么修改代码，要么修改测试。  

**setUp与tearDown**
可以在单元测试中编写两个特殊的｀setUp()和tearDown()｀方法。这两个方法会分别在每调用一个测试方法的前后分别被执行。  

## 文档测试

Python内置的"文档测试"(doctest)模块可以直接提取注释中的代码并执行测试。  

doctest严格按照Python交互式命令行的输入和输出来判断测试结果，只有测试异常时可以用`...`来表示一大段`TraceBack`的输出。  

---

# IO编程

IO指Input/Output，也就是输入/输出。所谓的输入输出是以计算机内存作为主体，从外界读取数据到内存称为Input(如从磁盘读取文件)，把内存数据传送到外界称为Output(如将数据写入到磁盘文件)。  

由于CPU和内存的速度远远高于外设速度，所以在IO编程中，就存在着严重的速度不匹配问题。比如要把100M的数据写入磁盘，CPU输出100M的数据只需要0.01秒，可是磁盘接收可能需要10秒，这时有两种方法:  
**同步I/O**  
让CPU等着，也就是程序暂停执行后续代码，等100M的数据在10秒后写入磁盘，再接着往下执行；

**异步I/O**
CPU不等待，只是告诉磁盘，让它继续接收，CPU则继续执行后续代码。  

同步IO和异步IO的区别就在于是否等待IO执行的结果。  
很明显，使用异步IO来编写程序性能会远远高于同步IO，但异步IO的缺点是编程模型复杂。  

操作IO的能力都是由操作系统提供的，每一种编程语言都会把操作系统提供的低级C接口封装起来方便使用，Python也不例外。  

## 文件读写

读写文件是最常见的IO操作，Python内置了读写文件的函数，用法和C是兼容的。  

需要知道的是，在磁盘上读写文件的功能都是由操作系统提供的，现代操作系统不允许普通的程序直接操作磁盘，所以，读写文件就是请求操作系统打开一个文件对象(通常称为文件描述符)，然后，通过操作系统提供的接口从这个文件对象中读取数据(读文件)，或者把数据写入这个文件对象(写文件)。  

### 读文件

要以读文件的模式打开一个文件对象，可使用Python内置的`open()`函数，传入文件名和标识符:  
```
>>> f = open('./test.txt', 'r')  # 如果文件不存在将会被自动创建
```
标识符`r`表示读，这样我们就成功打开了一个文件。  

如果文件打开成功，接下来，调用`read()`方法可以一次性读取文件的全部内容，Python把内容读到内存，用一个`str`对象表示:  
```
>>> f.read()
'Hello world!'
```
最后一步是调用`close()`方法关闭文件。文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的:  
```
>>> f.close()
```
由于文件读写时都可能产生`IOError`，一旦出错，后面的`f.close()`就不会调用。所以，为了保证无论是否出错都能正确的关闭文件，我们可以使用`try...finally`来实现:  
```
try:
    f = open('/path/to/file', 'r')
    print(f.read())
finally:
    if f:
        f.close()
```
但是每次都这么写比较繁琐，所以Python引入了`with`语句来自动帮我们调用`close()`方法:  
```
with open('/path/to/file', 'r') as f:
    print(f.read())
```
这条语句的效果和`try...finally`是一样的，但是代码更简洁。  

调用`read()`会一次性读取文件的全部内容，如果文件很大，内存就爆了。因此，为保险起见，可以反复调用`read(size)`方法，每次最多读取size个字节的内容。另外，调用`readline()`可以每次读取一行内容，调用`readlines()`一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用。  

### file-like-Object

像`open()`函数返回的这种有个`read()`方法的对象，在Python中统称为file-like Object。除了file以外，还可以是内存的字节流、网络流、自定义流等等。file-like Object不要求从特定类继承，只要写个`read()`方法就可以。  

`StringIO`就是在内存中创建的file-like Object，常用作临时缓冲。

### 二进制文件

前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件。要读取二进制文件，比如图片、视频等等，用`'rb'`模式打开文件即可：
```
>>> f = open('./test.jpg', 'rb')
>>> f.read()
b'\xff\xd8\xff\xe1\x00\x18Exif\x00\x00...' # 十六进制表示的字节
```

### 字符编码

要读取非UTF-8编码的文本文件，需要给`open()`函数传入`encoding`参数，例如，读取GBK编码的文件:  
```
>>> f = open('./gbk.txt', 'r', encoding='gbk')
>>> f.read()
'测试'
```
### 写文件

写文件和读文件是一样的，唯一的区别就是在调用`open()`函数时，传入标识符`w`或`wb`表示写文件或写二进制文件:  
```
>>> f = open('./test.txt', 'w')  # 以模式w打开会重写文件，原有内容被覆盖，若想要追加内容，可用模式a打开(append)
>>> f.write('Hello, world!')
>>> f.close()
```
## StringIO和BytesIO

### StringIO

很多时候，数据读写不一定是文件，也可以在内存中读写。  

`StringIO`就是在内存中创建的file-like Object，常用作临时缓冲。  

StringIO顾名思义就是在内存中读写str。  

要把str写入StringIO，我们需要先创建一个StringIO，然后像写文件一样写入即可:  
```
>>> from io import StringIO
>>> f = StringIO()  # 要把str写入StringIO，需要先创建一个StringIO
>>> f.write('kunimi hiro wa amamiya hikari wo da yi su ki de su')
50
>>> f.write('  ')  # 写入后返回写入字符串的字节数
2
>>> f.write('end')
3
>>> f.getvalue()  # getvalue()方法用于获得写入后的str
'kunimi hiro wa amamiya hikari wo da yi su ki de su  end'
```
要读取StringIO，可以用一个str初始化StringIO，然后像文件一样去读取:  
```
>>> f = StringIO('Hiro\nHikari\nHideo')
>>> while True:
...     s = f.readline()  # readline()方法逐行读取
...     if s == '':
...             break
...     print(s.strip())
... 
Hiro
Hikari
Hideo
```
### BytesIO

StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。  

BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes:  
```
>>> from io import BytesIO
>>> f = BytesIO()
>>> f.write('中文'.encode('utf-8'))  # 写入的不是str，而是经过utf-8编码的bytes。
6
>>> f.getvalue()
b'\xe4\xb8\xad\xe6\x96\x87'
```
读取类似于StringIO。

**stream position**:StringIO和BytesIO有一个stream position的概念，可以用`tell()`方法来查看目前的position，用`seek()`方法移动position。  

## 操作文件和目录

如果我们要操作文件、目录，可以在命令行下面输入操作系统提供的各种命令来完成。比如`dir`、`cp`等命令。  

如果要在Python程序中执行这些目录和文件的操作怎么办？其实操作系统提供的命令只是简单地调用了操作系统提供的接口函数，Python内置的`os`模块也可以直接调用操作系统提供的接口函数。  

`os`模块的基本功能:  
```
>>> import os  # 导入os模块
>>> os.name  # 操作系统的类型，posix代表是linux、unix或mac os x，如果结果是nt，就是Windows
'posix'
>>> os.uname() # 获取系统的详细信息，注意uname()函数在Windows上不支持，也就是说，os模块的某些函数是和操作系统相关的。
posix.uname_result(sysname='Linux', nodename='zhouxiaorui-Lenovo-IdeaPad-Y400', release='4.13.0-26-generic', version='#29~16.04.2-Ubuntu SMP Tue Jan 9 22:00:44 UTC 2018', machine='x86_64')
```
### 环境变量

在操作系统中定义的环境变量，全部保存在`os.environ`这个变量中，可以直接查看.  

要获取某个环境变量的值，可以调用`os.environ.get('key')`:  
```
>>> os.environ.get('HOME')
'/home/zhouxiaorui'
```
### 操作文件和目录

操作文件和目录的函数一部分放在`os`模块中，一部分放在`os.path`模块中。  
```
>>> import os
>>> os.path.abspath('.')  # 查看当前目录的绝对路径
'/home/zhouxiaorui'
>>> os.path.join('/home/zhouxiaorui', 'testdir')  # 在某目录下创建一个新目录，首先将新目录的完整路径表示出来
'/home/zhouxiaorui/testdir'
>>> os.mkdir('/home/zhouxiaorui/testdir')  # 创建一个目录
>>> os.rmdir('/home/zhouxiaorui/testdir')  # 删除一个目录
```
把两个路径合成一个时，不要直接拼接字符串，而要通过`os.path.join()`函数，这样可以正确处理不同操作系统的路径分隔符。  

同理，要拆分路径时，应该通过`os.path.split()`函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名:  
```
>>> os.path.split('/home/zhouxiaorui/testdir')  # 返回一个tuple
('/home/zhouxiaorui', 'testdir')
>>> os.path.split('/home/zhouxiaorui/test.txt')
('/home/zhouxiaorui', 'test.txt')
>>> os.path.splitext('/home/zhouxiaorui/test.txt')  # splitext()方法可以直接得到文件的扩展名
('/home/zhouxiaorui/test', '.txt')
```
这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。  

**文件操作**，假定当前目录下有一个`test.txt`文件:  
```
>>> import os
>>> os.mknod('test.txt')  # 创建空文件
>>> os.listdir('.')  # 返回指定目录下的所有文件和目录名(这里是当前目录)
['.config', '.ros', '.xsession-errors', '.ipython', ..., '文档', '.idea']
>>> os.rename('test.txt', 'test.py')  # 文件重命名
>>> os.remove('test.py')  # 删除文件
```
注意:在os模块中不存在复制文件的函数，原因是复制文件并非由操作系统提供的系统调用。  

但是`shutil`模块提供了`copyfile()`函数，还可以在`shutil`模块中找到很多实用的函数，它们可以看做`os`模块的补充。  

## 序列化

我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling。  

序列化之后，就可以将序列化后的内容写入磁盘，或者通过网络传输到别的机器上。  

反之，将变量内容从序列化对象重新读到内存里称之为反序列化，即unpickling。  

Python提供了`pickle`模块来实现序列化。  

首先，尝试把一个对象序列化并写入文件:  
```
>>> import pickle
>>> d = dict(name='Feihong', age=14, score=20)
>>> pickle.dumps(d)  # dumps()方法把任意对象序列化为一个`bytes`，然后就可以把这个bytes写入文件
b'\x80\x03}q\x00(X\x05\x00\x00\x00scoreq\x01K\x14X\x04\x00\x00\x00nameq\x02X\x07\x00\x00\x00Feihongq\x03X\x03\x00\x00\x00ageq\x04K\x0eu.'
>>> f = open('dump.txt', 'wb')
>>> pickle.dump(d, f)  # 或者用另一个方法dump()可以直接把对象序列化以后写入一个file-like Object
>>> f.close()
```
当我们要把对象从磁盘读到内存时，可以先把内容读到一个`bytes`，然后用`pickle.loads()`方法反序列化出对象，也可以直接用`pickle.load()`方法从一个file-like Object中直接反序列化出对象。  
```
>>> with open('dump.txt', 'rb') as f:
...     print(pickle.load(f))
... 
{'score': 20, 'name': 'Feihong', 'age': 14}
```
Pickle的问题和所有其他编程语言特有的序列化问题一样，就是他只能用于Python，并且可能不同版本的Python彼此都不兼容，因此，只能用Pickle保存那些不重要的数据，不能成功反序列化也没关系。  

### Json

Python语言特定的序列化模块是`pickle`，但如果要把序列化搞得更通用、更符合Web标准，就可以使用`json`模块。

如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式。比如XML，但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。JSON不仅是标准格式，并且比XML更快，可以直接在Web页面中读取，非常方便。  

JSON表示的对象就是标准的额JavaScript语言的对象。JSON和Python内置的数据类型对应如下:  

|JSON类型|Python类型|
|:-----:|:-----:|
|`{}`|dict|
|`[]`|list|
|"string"|str|
|1234.56|int或float|
|true/false|True/False|
|null|None|

Python内置的`json`模块提供了非常完善的Python对象到JSON格式的转换。  
把Python对象转换为一个JSON:  
```
>>> import json
>>> d = dict(name='Bob', age=20, score=88)
>>> json.dumps(d)
'{"age": 20, "score": 88, "name": "Bob"}
```
`dumps()`方法返回一个`str`，内容就是标准的JSON。类似的，`dump()`方法可以直接把JSON写入一个file-like Object。  

要把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化：
```
>>> json_str ='[true, "haha", 123]'
>>> json.loads(json_str)
[True, 'haha', 123]
```
由于JSON标准规定JSON编码是UTF-8，所以我们总是能正确的在Python的`str`与JSON的字符串之间转换。  

### JSON进阶

`json.dumps()`和`json.loads()`有很多可选参数，灵活运用它们可以更好的进行转换，例如对class对象进行转换，就需要对`default`和`object_hook`进行设定。  

---

# 进程和线程

**多任务**:简单来讲，就是操作系统可以同时运行多个任务。比如，一边用浏览器上网，一遍用网易云听歌，一边又用word写论文，这就是多任务，至少有3个任务正在运行。  
对于单核CPU而言，它也可以执行多任务，但看似所有任务都在同时执行，其实每个任务都是交替执行的，只是因为CPU的执行速度太快了，感觉就像是同时执行的一样。  

而真正的并行执行多任务只能在多核CPU上实现，但是，由于任务数量远大于CPU的核心数量，所以操作系统也会自动把很多任务轮流调度到每个核心上执行。  

对于操作系统而言，每个任务就是一个进程(Process)，比如打开一个记事本就是启动了一个记事本进程。  

有些进程工作时并不止做一件事，比如word，它可以同时进行打字、拼写检查、打印等多项工作。我们把这些进程内的"子任务"称为线程(Thread)。  

由于每个进程至少要干一件事，所以，一个进程至少有一个线程。当然，像Word这种复杂的进程可以有多个线程，多个线程可以同时执行，多线程的执行方式和多进程是一样的，也是由操作系统在多个线程之间快速切换，让每个线程都短暂地交替运行，看起来就像同时执行一样。当然，真正地同时执行多线程需要多核CPU才可能实现。  

我们前面编写的Python程序，都是执行单任务的进程，也就是只有一个线程。如果我们要同时执行多个任务，有两种解决方案:  

- 一种是启动多个进程，虽然每个进程只有一个线程，但多个进程可以一起执行多个任务；
- 另一种是启动一个进程，在一个进程内启动多个线程。这样，多个线程也可以一块执行多个任务。  
- 第三种方法就是启动多个进程，每个进程再启动多个线程，这样同时执行的任务就更多了，但由于这种模型更复杂，所以在实际工作中很少采用。  

## 多进程

### fork()
Unix/Linux操作系统提供了一个`fork()`系统调用，它非常特殊。普通的函数调用，调用一次，返回一次，但是`fork()`调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。  

子进程永远返回`0`，而父进程返回子进程的ID。这样做的理由是，一个父进程可以fork出很多子进程，所以，父进程要记下每个子进程的ID，而子进程只需要调用`getppid()`就可以拿到父进程的ID。  

Python的`os`模块封装了常见的系统调用，其中就包括`fork`，可以在Python程序中轻松创建子进程。  

### multiprocessing

由于Windows没有`fork()`，而Python是跨平台的，自然也应该提供一个跨平台的多进程支持。`multiprocessing`模块就是跨平台版本的多进程模块。  

multiprocessing模块提供了一个Process类来代表一个进程对象。  

创建子进程时，只需要传入一个执行函数和函数的参数，创建一个`Process`实例，用`start()`方法启动，这样创建进程比`fork()`还要简单。  

`join()`方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。

### Pool
如果要启动大量的子进程，可以用进程池的方式批量创建子进程。  

### 子进程
很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出。  

`subprocess`模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。  

### 进程间的通信

`Process`之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。Python的`multiprocessing`模块包装了底层的机制，提供了`Queue`、`Pipes`等多种方式来交换数据。  

## 多线程
Python的标准库提供了两个模块：`_thread`和`threading`，`_thread`是低级模块，`threading`是高级模块，对`_thread`进行了封装。绝大多数情况下，我们只需要使用`threading`这个高级模块。  

启动一个线程就是把一个函数传入并创建`Thread`实例，然后调用`start()`开始执行。

### Lock

多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。  

如果我们要确保变量最后计算正确，就要给改变它的函数上一把锁，当某个线程开始执行该函数时，我们说，该线程因为获得了锁，因此其他线程不能同时执行此函数，只能等待，直到锁被释放后，获得该锁以后才能改。由于锁只有一个，无论多少线程，同一时刻最多只有一个线程持有该锁，所以，不会造成修改的冲突。创建一个锁是通过threading.Lock()来实现的。  

获得锁的线程用完后一定要释放锁，否则那些苦苦等待锁的线程将永远等待下去，成为死线程。所以我们用`try...finally`来确保锁一定会被释放。  

### GIL锁

Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global Interpreter Lock，任何Python线程执行前，必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。这个GIL全局锁实际上把所有线程的执行代码都给上了锁，所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。  

## ThreadLocal

一个`ThreadLocal`变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。`ThreadLocal`解决了参数在一个线程中各个函数之间互相传递的问题。  

`ThreadLocal`最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源

## 进程 vs 线程

首先，要实现多任务，我们通常会设计Master-Worker模式，Master负责分配任务，Worker负责执行任务。而在多进程/多线程模式中，主进程/线程就是Master，而子进程/线程就是Worker。  

多进程模式最大的优点就是稳定性高，因为一个子进程崩溃了，不会影响主进程和其他子进程。（当然主进程挂了所有进程就全挂了，但是Master进程只负责分配任务，挂掉的概率低）。  

多进程模式的缺点是创建进程的代价大，在Unix/Linux系统下，用`fork`调用还行，在Windows下创建进程开销巨大。另外，操作系统能同时运行的进程数也是有限的，在内存和CPU的限制下，如果有几千个进程同时运行，操作系统连调度都会成问题。  

多线程模式通常比多进程快一点，但也快不到哪里去，而且多线程模式致命的缺点是，任何一个线程挂掉都可能直接造成整个进程崩溃，因为所有线程共享进程的内存。  

### 计算密集型 vs IO密集型

是否采用多任务需要考虑任务的类型。我们可以把任务分为计算密集型和IO密集型。  

计算密集型任务的特点是消耗CPU资源，这种情况下如果采用多任务，则任务越多，花在任务切换的时间就越多，CPU的执行效率越低。因此，要最高效的利用CPU，计算密集型任务同时进行的数量应当等于CPU的核心数。  

而IO密集型任务的特点是CPU消耗很少，任务的大部分时间都在等待IO操作完成。因此，对于此类任务，任务越多，CPU效率越高，但也要有一个限度。  

## 分布式进程

在Thread和Process中，应当优选Process，因为Process更稳定，而且，Process可以分布到多台机器上，而Thread最多只能分布到同一台机器的多个CPU上。  

Python的`multiprocessing`模块不但支持多进程，其中的`managers`模块还支持把多进程分布到多台机器上。一个服务进程可以作为调度者，将任务分布到其他多个进程中，依靠网络通信。  




















