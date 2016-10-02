# -*- coding: cp936 -*-
#�������WSGI������������application()����
from wsgiref.simple_server import make_server
#�����Լ�д��application
from hello_web import application

#����һ����������IP��ַΪ�գ��˿�8000�����������application
httpd=make_server('',8000,application)
print "Serving HTTP on port 8000..."

#��ʼ����HTTP����
httpd.serve_forever()

#���д˳���������д򿪣�localhost:8000
