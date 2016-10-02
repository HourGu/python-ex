#!/usr/bin/env python3  
#coding: utf-8  

import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText  
from email.mime.image import MIMEImage  
  
sender = '18202739487@163.com'  
receiver = '974663046@qq.com'  
subject = 'python email test'  
smtpserver = 'smtp.163.com'    
password = '927192718gkff'  

#文件头说明 
msgRoot = MIMEMultipart('related')  
msgRoot['From'] = '小诗<18202739487@163.com>'
msgRoot['Subject'] = Header(u'this is a smtp_test', 'utf-8').encode()
msgRoot['To'] = u'De<974663046@qq.com>'

#正文内容
#文本部分
msgText1 = MIMEText('<b>Some <i>HTML</i> text</b> and an image.<br><img src="cid:image1"><br>good!','html','utf-8')  
msgRoot.attach(msgText1)  

#附件部分
fp = open(r'E:\Python27\001.png', 'rb')  
msgImage = MIMEImage(fp.read())  
fp.close()  
  
msgImage.add_header('Content-ID', '<image1>')  
msgRoot.attach(msgImage)

#登陆服务器并发送邮件
smtp = smtplib.SMTP('smtp.163.com',25)   
smtp.login(sender, password)  
smtp.sendmail(sender, receiver, msgRoot.as_string())  
smtp.quit()
