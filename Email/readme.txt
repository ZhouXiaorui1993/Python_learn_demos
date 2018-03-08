名词：
MUA:Mail User Agent--邮件用户代理，就是电子邮件软件，比如Outlook、Foxmail等。
MTA:Mail Transfer Agent--邮件传输代理，就是Email服务提供商，比如网易、新浪等。
MDA:Mail Delivery Agent--邮件投递代理

邮件的传输过程：
发件人 -> MUA -> MTA -> 若干个MTA -> MDA <- MUA <- 收件人

因此，编写程序发送和接收邮件，本质上就是：
1.编写MUA把邮件发到MTA
2.编写MUA从MDA上收邮件

发邮件时，MUA和MTA使用的协议就是SMTP(Simple Mail Transfer Protocol)
，后面的MTA到另一个MTA也是用的SMTP协议。

收邮件时，MUA和MTA使用的协议有两种：POP(POst Office Protocol)，目前版本是3，俗称POP3;
IMAP(Internet Message Access Protocol)，优点是不但能取邮件，还可以直接操作MDA上存储的
邮件，比如从收件箱移动到垃圾箱等等。

邮件客户端软件在发邮件时，会让你先配置SMTP服务器，也就是要发送到哪个MTA上。假设你正在使用163
邮箱，你就不能直接发送到新浪的MTA上，因为它只服务于新浪的用户，所以需要填写163提供的SMTP服务
器地址：stmp.163.com，为证明自己是163的用户，STMP服务器还要求填写邮箱地址和油箱口令，这样，
MUA才能正常的把Email通过SMTP协议发送到MTA。

类似的，从MDA收取邮件时，MDA服务器也要求验证邮箱口令，确保不会有人冒充你收取你的邮件。所以，
Outlook之类的邮件客户端也会要求你填写POP3或IMPA服务器地址、邮箱地址和口令。这样，MUA才能顺利
地通过POP或IMAP协议从MDA取到邮件。



