# -*- coding: cp936 -*-
### __xx__
class Student(object):
    def __init__(self, name):
        self.name = name


print Student('Michael')
#<__main__.Student object at 0x02E51E10>

##__str__ method ,for user
class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name:%s)'%self.name

print Student('Michael')
#Student object (name:Michael)
'''
>>> Student('Michael')
<__main__.Student object at 0x02F99E50>
'''

##__repr__ method , for programmer
class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name:%s)'%self.name

    __repr__=__str__

print Student('Michael')

'''
>>> Student('Michael')
Student object (name:Michael)
>>> print Student('Michael')
Student object (name:Michael)
'''

##__iter__  for loop of class
#ʵ��һ��__iter__()�������÷�������һ����������Ȼ��
#Python��forѭ���ͻ᲻�ϵ��øõ��������next()�����õ�ѭ������һ��ֵ
class Fib(object):
    def __init__(self):
        self.a,self.b=0,1#��ʼ������������a,b

    def __iter__(self):
        return self#ʵ��������ǵ������󣬹ʷ����Լ�


    def next(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a>100000:
            raise StopIteration();
        return self.a

'''
>>> for n in Fib():
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
89
144
233
377
610
987
1597
2584
4181
6765
10946
17711
28657
46368
75025

>>> Fib()[3]

Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    Fib()[3]
TypeError: 'Fib' object does not support indexing
>>> 
'''

##__getitem__ 
class Fib(object):
    def __getitem__(self,n):
        a,b=1,1
        for x in range(n):
            a,b=b,a+b
        return a
  
'''
>>> f=Fib()
>>> f[0]
1
>>> f[7]
21
>>> f[100]
573147844013817084101L
>>> 
'''

##__getitem__,includes slice
class Fib(object):
    def __getitem__(self,n):
        if isinstance(n,int):
            a,b=1,1
            for x in range(n):
                a,b=b,a+b
            return a

        elif isinstance(n,slice):
            start=n.start
            stop=n.stop
            a,b=1,1
            L=[]
            for x in range(stop):
                if x>=start:
                    L.append(a)
                a,b=b,a+b
            return L

'''
>>> f=Fib()
>>> f[4]
5
>>> f[3:12]
[3, 5, 8, 13, 21, 34, 55, 89, 144]
>>>
'''

##__getattr__ ,judge the attr is exist or not and return sth
class Student(object):
    def __init__(self):
        self.name='Michael'

    def __getattr__(self,attr):
        if attr=='score':
            return 99

'''
>>> s=Student()
>>> s.name
'Michael'
>>> print s.fdkj
None
>>> print s.score
99
'''

class Student(object):
    def __init__(self):
        self.name='Michael'

    def __getattr__(self,attr):
        if attr=='score':
            return lambda:32
        raise AttributeError('\'Student\' object has no attribute \'%s\' % attr')
'''
>>> s=Student()
>>> s.score
<function <lambda> at 0x02F9F970>
>>> s.score()
32
>>> print s.fdkj

Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print s.fdkj
  File "E:\Python27\temporary.py", line 8, in __getattr__
    raise AttributeError('\'Student\' object has no attribute \'%s\' % attr')
AttributeError: 'Student' object has no attribute '%s' % attr
>>> 
'''

#��ʽ����
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path
'''
>>> Chain().status.user.timeline.list
<__main__.Chain object at 0x03066790>
>>> print Chain().status.user.timeline.list
/status/user/timeline/list
>>> print Chain().status.user
/status/user
'''

##__call__,����ʵ����instance()�����ö���instance.method()
class Student(object):
    def __init__(self, name):
        self.name = name
    def __call__(self):
        print 'my name is %s.'%self.name

'''
>>> s=Student('skad')
>>> s()
my name is skad.
>>> 
'''
