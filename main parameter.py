# -*- coding: cp936 -*-
#�ؼ��ֲ���
def person(name,age,**kw):
    print 'name:',name,'    age:',age,'     other:',kw
    
'''
>>> person('Bob',34,gemder='M',job='engineer')
name: Bob     age: 34      other: {'gemder': 'M', 'job': 'engineer'}
'''

'''
>>> kw={'city':'beijing','job':'Engineer'}
>>> person('Bob',23,**kw)
name: Bob     age: 23      other: {'city': 'beijing', 'job': 'Engineer'}
>>> 
'''

'''
>>> print('name','Bob',45)
('name', 'Bob', 45)
>>> print 'name','Bob',45
name Bob 45
>>> 

'''
