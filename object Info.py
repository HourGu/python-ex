# -*- coding: cp936 -*-
#object Info
>>> type('dsa')
<type 'str'>
>>> type(abs)
<type 'builtin_function_or_method'>

>>> import types
>>> type('fsda')
<type 'str'>

>>> type([])==types.ListType
True

>>> type(int)==types.TypeType
True


##

# -*- coding: cp936 -*-
#super class & subclass
class Animal(object):
    def __init__(self,name):
        self.name=name
    def run(self):
        print '%s is running'%self.name
        
class Tortoise(Animal):
    def run(self):
        print 'tortoise is running slowly'
    
class Dog(Animal):
    def run(self):
        print 'dog is running'

class Cat(Animal):
    def run(self):
        print 'cat is running'

class Black_hair(Dog):
    def run(self):
        print 'the dog wants to bite me!'


def run_twice(animal):
    animal.run()
    animal.run()

'''
>>> a=Animal('a')
>>> b=Dog('b')
>>> c=Black_hair('c')
>>> c.run ()
the dog wants to bite me!
>>> run_twice(Black_hair('c'))
the dog wants to bite me!
the dog wants to bite me!
>>> isinstance(c,Dog)
True
'''
#�� dir ��ȡ��������Ժͷ���
>>> dir(a)
['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'name', 'run']
>>> 
>>> hasattr(a,'run')
True
>>> setattr(c,'age',3)
>>> c.age
3
>>> getattr(c,'age')
3
>>> 
 
