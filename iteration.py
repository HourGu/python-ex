# -*- coding: cp936 -*-
#����iteration
## for```in```

>>> d={'a':1,'b':2,'c':3}

##
>>> for key in d:
	print key

	
a
c
b


##
>>> for value in d.itervalues():
	print value

	
1
3
2


##
>>> for value in d:
	print value

	
a
c
b


##
>>> for key,value in d.iteritems():
	print key,value

	
a 1
c 3
b 2
>>> 

##
>>> for ch in 'ABC':
     print ch

     
A
B
C

#ֻҪ�ǿɵ��������ݶ�����for����isinstance���ж϶������͵����ú�������iterable���������͵�һ�֣��ж��Ƿ���ѭ��
from collections import Iterable
>>> isinstance([1,2,3],Iterable)
True
>>> isinstance(123,Iterable)
False
>>> 

#��enumerate������ѭ���������
for i,value in enumerate(['a','b','c']):
    print i,value

0 a
1 b
2 c
