# -*- coding: cp936 -*-
#������generator
g=(x*x for x in range(10))

'''
>>> g.next()
0
>>> g.next()
1
>>> g.next()
4
>>> for n in g:
	print n

	
9
16
25
36
49
64
81
>>>

'''

#쳲���������
# -*- coding: cp936 -*-
#쳲���������
def fib(max):
    n,a,b=0,1,1
    while n<max:
        print a
        a,b=b,a+b
        n=n+1
'''
>>> fib(10)
1
1
2
3
5
8
13
21
34
55
'''

#��print����yield�������ͱ��generator����
def fib(max):
    n,a,b=0,1,1
    while n<max:
        yield a
        a,b=b,a+b
        n=n+1
'''
>>> fib(10)
<generator object fib at 0x02FA05F8>
>>> for n in fib(10):
	print n

	
1
1
2
3
5
8
13
21
34
55
'''

