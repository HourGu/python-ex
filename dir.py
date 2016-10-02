# -*- coding: cp936 -*-
#file and direction

>>> os.path.abspath('.') #��ǰ����·��
'E:\\Python27\\python ex\\_'
>>> os.path.join('E:\Python27','test') #����ĳ����·���Ⱥϳ�·��
'E:\\Python27\\test'
>>> os.mkdir('E:\\Python27\\test')#������·��

>>> os.path.split('E:\\Python27\\test')#���·��Ϊ�����֣���һ����������󼶱��Ŀ¼���ļ���
('E:\\Python27', 'test')
>>> os.path.splitext('E:\\Python27\\test')
('E:\\Python27\\test', '')
>>> os.path.splitext('E:\\Python27\\test.txt')#����ֱ�ӵõ��ļ���չ��
('E:\\Python27\\test', '.txt')
>>> 

[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
