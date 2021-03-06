程序运行时，数据都是在内存中的。当程序终止时，通常需要将数据保存到磁盘上，
无论是保存到本地磁盘，还是通过网络保存到服务器上，最终都会将数据写入磁盘文件。

而如何定义数据的存储格式就是一个大问题，如果我们自己来定义存储格式，比如保存一
个班级所有学生的成绩单，你可以用一个文本文件保存，一行保存一个学生，用逗号隔开：

Michael,99
Bob,85
Bart,55
Lisa,87

你还可以用JSON格式保存，也就是文本文件：
[
    {"name":"Michael","score":99},
    {"name":"BOb","score":85},
    {"name":"Bart","score":55},
    {"name":"Lisa","score":87}
]

你还可以定义各种保存格式，但是按此种方式存储，一来格式太多，无法统一；二来无法
做快速查询，因为以这样的方式存储的数据只有将数据全部读入到内存中才可遍历，但有
时数据大小远超过了内存大小，根本无法全部读入内存。

为了便于程序保存和读取数据，且能直接通过条件快速查询到指定的数据，就出现了数据
库（Database）这种专门用于集中存储和查询的软件。

数据库软件诞生的历史非常久远，早在1950年数据库就诞生了。经历了网状数据库、层次
数据库，我们现在广泛使用的关系数据库是20世纪70年代基于关系模型的基础上诞生的。

关系模型有一套复杂的数学理论，但从概念上是十分容易理解的。举个例子：

假设某个小学有三个年级，要表示出这三个年级，可以在Excel中用一个表格画出来：

Grade_ID Name
    1    一年级
    2    二年级
    3    三年级

每个年级又有若干个班级，要把所有班级表示出来，可以在Excel中再画一个表格：

Grade_ID  Class_ID    Name
    1       11      一年级一班
    1       12      一年级二班
    1       13      一年级三班
    2       21      二年级一班
    2       22      二年级二班
    2       33      二年级三班
   ...      ...        ...

这两个表格有个映射关系，就是根据Grade_ID可以在班级表中查找对应的所有班级。

也就是Grade表的每一行对应Class表的多行，在关系数据库中，这种基于表（Table）的
一对多的关系就是关系数据库的基础。

根据某个年级的ID就可以查找所有班级的行，这种查询语句在关系数据库中称为SQL语句，可以写成：

SELECT * FROM classes WHERE grade_id = '1';

结果也是一个表：

---------+----------+----------
grade_id | class_id | name
---------+----------+----------
1        | 11       | 一年级一班
---------+----------+----------
1        | 12       | 一年级二班
---------+----------+----------
1        | 13       | 一年级三班
---------+----------+----------

类似的，Class表的一行记录又可以关联到Student表的多行记录，等等。


数据库的类别：

目前广泛使用的几种关系数据库：

A) 付费的商用数据库
1. Oracle，典型的高富帅；
2. SQL server，微软自己的产品，Windows定制专款；
3. DB2，IBM的产品，听起来很高端；
4. Sybase，曾跟微软是好基友，后来关系破裂，目前境况惨淡。

B) 免费的开源数据库：
1. MySQL，大家都在用，一般错不了；
2. PostgreSQL，学术气息浓厚，其实不错，但知名度没有MySQL高；
3. sqlite，嵌入式数据库，适合桌面和移动应用。

由于MySQL普及率高，而且围绕它有一大堆监控和运维的工具，安装和使用很方便，
故我们选择MySQL。




