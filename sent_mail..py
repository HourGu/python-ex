# -*- coding: utf-8 -*-
#��׼�ʼ���Ҫ����ͷ����Ϣ�� From, To, �� Subject ��ÿ����Ϣֱ��ʹ�ÿ��зָ
import smtplib
from email.header import Header
from email.mime.text import MIMEText
server = smtplib.SMTP('smtp.163.com', 25)
server.login('18202739487@163.com', '927192718gkff')#����163smtp�������������ǿͻ�������
#msg = MIMEText('hello, send by Python...', 'plain', 'utf-8') #��ͨ���ı�
msg = MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8')# ��������

msg['From'] = '18202739487@163.com <18202739487@163.com>'
msg['Subject'] = Header(u'text', 'utf8').encode()
msg['To'] = u'De<974663046@qq.com>'
server.sendmail('18202739487@163.com', ['974663046@qq.com'], msg.as_string())



