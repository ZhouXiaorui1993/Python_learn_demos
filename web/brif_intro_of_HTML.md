#HTML简介

HTML定义了一套语法规则，来告诉浏览器如何把一个丰富多彩的页面显示出来。

一个简单的例子：
```html
<html>
<head>
    <title>Hello,html</title>
</head>
<body>
    <h1>Hello,world!</h1>
</body>
</html>
```
##CSS简介

CSS是Cascading Style Sheet（层叠样式表）的简称，CSS用来控制HTML里
的所有元素如何展现。比如，给标题元素`<h1>`加一个样式，变成48号字体，
灰色，带阴影：
```html
<html>
<head>
    <title>Hello,html</title>
    <style>
        h1{
        color: #333333;
        font-size: 48px;
        text-shadow: 3px 3px 3px #666666;
        }
    </style>
</head>
<body>
    <h1>Hello,world!</h1>
</body>
</html>
```
