# -*- coding: cp936 -*-
#itertools..
>>> import itertools
>>> natuals=itertools.count(1)
>>> for n in natuals:
	print n

#���������޸�����Ȼ����count�����������ָ�Ӽ���ʼ

>>> import itertools
>>> cs=itertools.cycle('ABC')
>>> for c in cs:
	print c

	
A
B
C
A
B
C
A
B


>>> ns=itertools.repeat('A',10)
>>> for n in ns:
	print n

	
A
A
A
A
A
A
A
A
A
A
>>> natuals=itertools.count(1)
>>> ns=itertools.takewhile(lambda x:x<=10,natuals)
>>> for n in ns:
	print n

	
1
2
3
4
5
6
7
8
9
10
>>> 


##groupby()
for key,group in itertools.groupby ('AAABBBCDDDEE'):
        print key,list(group)


A ['A', 'A', 'A']
B ['B', 'B', 'B']
C ['C']
D ['D', 'D', 'D']
E ['E', 'E']
>>> 

#ʵ������ѡ������ͨ��������ɵģ�ֻҪ�����ں���������Ԫ�ط��ص�ֵ��ȣ�
#������Ԫ�ؾͱ���Ϊ����һ��ģ�
#����������ֵ��Ϊ���key���������Ҫ���Դ�Сд���飬�Ϳ�����Ԫ��'A'��'a'��������ͬ��key��
for key,group in itertools.groupby ('AAabBBCDdDeE',lambda c:c.upper()):
        print key,list(group)

>>> for key,group in itertools.groupby ('AAabBBCDdDeE',lambda c:c.upper()):
        print key,list(group)

        
A ['A', 'A', 'a']
B ['b', 'B', 'B']
C ['C']
D ['D', 'd', 'D']
E ['e', 'E']
>>> 

##imap,���Դ�����������
#ע��imap()����һ���������󣬶�map()����list���������map()ʱ���Ѿ�������ϣ�
#����ifilter��filter
>>> for x in itertools.imap(lambda x,y:x*y,[10,20,30],itertools.count(1)):
	print x

	
10
40
90

>>> r= itertools.imap(lambda x:x*x,itertools.count(1))
>>> for n in itertools.takewhile (lambda x: x<100,r):
	print n

	
1
4
9
16
25
36
49
64
81
>>> 
>>> 
