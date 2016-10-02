# -*- coding: cp936 -*-
#re:regular expression,������ʽ
#r''��ʾ
>>> import re
>>> re.match(r'^\d{3}\-\d{3,8}$','010-123456')
<_sre.SRE_Match object at 0x0303B218>
>>> re.match(r'^\d{3}\-\d{3,8}$','010 123456')

##
test = '�û�������ַ���'
if re.match(r'������ʽ', test):
    print 'ok'
else:
    print 'failed'


##group,���飬()
m=re.match(r'^(\d{3})-(\d{3,8})$','010-123456')
>>> m
<_sre.SRE_Match object at 0x02E00D10>
>>> m.group(1)
'010'
>>> m.group(2)
'123456'
>>> m.group(0)#group(0)��Զ��ԭʼ�ַ���
'010-123456'
>>> 
##ʱ��ƥ��
t='12:26:09'
m=re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
>>> m
<_sre.SRE_Match object at 0x0303A2A0>
>>> m.groups()
('12', '26', '09')
>>> m.group(1)
'12'

##̰��ƥ��
>>> re.match(r'^(\d+?)(0*)$', '102300').groups()#?ʹ֮�����ٵ�ƥ��
('1023', '00')
>>> re.match(r'^(\d+)(0*)$', '102300').groups()#\d+Ҳ��ƥ������0��0*ֻ��ƥ����ַ���
('102300', '')

##����
>>> import re
>>> re_telephone=re.compile(r'^(\d{3})-(\d{3,8})$')
>>> re_telephone.match('010-12345').groups()
('010', '12345')

>>> re_telephone.match('010-7867').groups()
('010', '7867')
>>> 


##findall and (.*?)
>>> p=re.compile(r'(.*?)')

>>> print p.findall('  dfggj<>sdj dsjdfhk jds      /')
['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

>>> p=re.compile(r'(.*?)d')
>>> print p.findall('  dfggj<>sdj dsjdfhk jds      /')
['  ', 'fggj<>s', 'j ', 'sj', 'fhk j']
>>> 
