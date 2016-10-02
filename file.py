# -*- coding: cp936 -*-
#file
f = open('/Users/michael/test.txt', 'r')
f.read()
'Hello, world!
f.close()
##
try:
    f = open('/path/to/file', 'r')
    print f.read()
finally:
    if f:
        f.close()

##
with open('/path/to/file','r') as f:
    print f.read()

#����ļ���С��read()һ���Զ�ȡ��㣻�������ȷ���ļ���С��
    #��������read(size)�Ƚϱ��գ�����������ļ�������readlines()��㣺

>>> with open('E:\Python27\ABC.txt','r') as f:
	 for line in f.readlines():
		 print(line.strip())

		 
skdfld
fsder
sdfgr
fwl
>>> with open('E:\Python27\ABC.txt','r') as f:
	 for line in f.readlines():
		 print(line)

		 
skdfld

fsder

sdfgr

fwl
