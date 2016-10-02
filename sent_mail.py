# -*- coding: cp936 -*-
##�ο�ʾ��
import smtplib
from email.mime.text import MIMEText
 
to_list = ['974663046@qq.com', '974663046qq@sina.com']
server_host = 'smtp.163.com'
 
username = '18202739487@163.com'
password = '927192718gkff'
 
 
def send(to_list, sub, content):
  '''
  :param to_list: �ռ�������
  :param sub: �ʼ�����
  :param content: ����
  '''
  me = "xiaoshi" + "<" + username + ">"
  # _subtype ������Ϊhtml,Ĭ����plain
  msg = MIMEText(content, _subtype='html')
  msg['Subject'] = sub
  msg['From'] = me
  msg['To'] = ';'.join(to_list)
  try:
    server = smtplib.SMTP()
    server.connect(server_host)
    server.login(username, password)
    server.sendmail(me, to_list, msg.as_string())
    server.close()
  except Exception as e:
    print str(e)
 
if __name__ == '__main__':
  send(to_list, "�����һ���ʼ�", "<h1>Hello, It's test email.</h1>")
