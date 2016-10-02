# -*- coding: cp936 -*-
#�б����� list comprehensions
#���ɡ�1����2������������n����
#����һ��ѭ��
L=[]
for x in range(1,11):
    L.append(x*x)
'''
>>> L
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
'''

#���������б�����ʽ
[x*x for x in range(1,11)]
'''
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

'''
#���Լ�������ɸѡ
[x*x for x in range(1,11) if x%2==0]
'''
[4, 16, 36, 64, 100]
'''
#������ʹ������ѭ������������ȫ����
[m+n for m in 'ABC' for n in 'XYZ']
'''
['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
'''

#�г���ǰĿ¼�µ������ļ���Ŀ¼��
import os
[d for d in os.listdir('.')]
'''
['default variable.py', 'ex0709.py', 'group parameter.py', 'iteration.py', 'list comprehensions.py', 'main parameter.py', 'make list.py', 'nmi.py', 'recurrence f.py', 'slice.py', 'static variable.py', 'tail recursion.py']
'''

#forѭ����ʵ����ͬʱʹ�����������������������dict��iteritems()����ͬʱ����key��value��
d={'x': 'A', 'y': 'B', 'z': 'C' }
for k,v in d.iteritems():
    print k,'=',value
'''
y = B
x = A
z = C
'''
d={'x': 'A', 'y': 'B', 'z': 'C' }
[k+'='+v for k,v in d.iteritems()]
    
>>> d = {'x': 'A', 'y': 'B', 'z': 'C' }
>>> [k + '=' + v for k, v in d.iteritems()]
['y=B', 'x=A', 'z=C']

>>> L = ['Hello', 'World', 'IBM', 'Apple']
>>> [s.lower() for s in L]
['hello', 'world', 'ibm', 'apple']
