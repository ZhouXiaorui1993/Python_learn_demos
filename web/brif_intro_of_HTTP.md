# HTTP协议简介

在web应用中，服务器把网页传给浏览器，实际上就是把网页的HTML代码发
送给浏览器，让浏览器显示出来。而浏览器和服务器之间的传输协议是HTTP：  

- HTML是一种用来定义网页的文本，会HTML，就可以编写网页；
- HTTP是一种在网络上传输HTML的协议，用于浏览器和服务器的通信。

##关于get、post和请求头、响应头

- get：表示一个读取请求，将从服务器获得网页数据。
- host：表示请求的域名。
- 200 ok：响应码和说明。
- Content-Type：指示响应的内容,浏览器就是依靠它来判断响应的内容是
网页还是图片、视频还是音乐的。（并不是依靠URL来判断的）
- 响应Body：就是HTML源码。
- Post：一个包含用户数据的请求，相对get多一个包含请求的Body。

##HTTP请求的流程

1. 浏览器首先向服务器发送HTTP请求，请求包括：

**方法：** Get还是Post，前者仅请求资源，后者会附带用户数据；

**路径：** /full/url/path；

**域名：** 由Host指定，例如：www.sina.com.cn

以及其他相关的Header；

2. 服务器向浏览器返回HTTP响应，响应包括：

**响应代码：** 200表示成功，3xx表示重定向，4xx表示客户端发送的请求
有错误，5xx表示服务器端处理时发生了错误；

**响应类型：** 由Content-Type指定；

以及其他相关的header；

通常服务器的HTTP响应会携带内容，也就是有一个Body，包含响应的内容，网
页的HTML源码就在Body中。

3. 如果浏览器还需要继续向服务器请求其他资源，比如图片，就再次发出HTTP请求，重复步骤1、2。

##HTTP请求格式

**Get请求格式**
```buildoutcfg
GET /path HTTP/1.1
Header1: Value1
Header2: Value2
Header3: Value3
```
每个Header一行一个，换行符是\r\n。

**Post请求格式**
```buildoutcfg
POST /path HTTP/1.1
Header1: Value1
Header2: Value2
Header3: Value3

body data goes here...
```
当遇到连续两个\r\n时，Header部分结束，后面的数据全部是Body。

**HTTP响应格式**
```buildoutcfg
200 OK
Header1: Value1
Header2: Value2
Header3: Value3

body data goes here...
```
HTTP响应如果包含body，也是通过\r\n\r\n来分隔的。

