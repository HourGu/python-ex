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
    

'''
>>> a=Dog('songzhe')
>>> a.run ()
songzhe is running                ��dog��cat����pass
>>> b=Cat('marong')
>>> b.run ()
marong is running
>>> ================================ RESTART ================================
>>> 
>>> ���Ǹ����ͬ������
>>> a=Dog('songzhe')
>>> a.run ()
dog is running
>>> b=Cat('marong')
>>> b.run ()
cat is running
>>> 
'''

def run_twice(animal):
    animal.run()
    animal.run()
'''
>>> run_twice(Tortoise('songzhe'))
tortoise is running slowly
tortoise is running slowly
>>> run_twice(Dog('songzhe'))
dog is running
dog is running
>>> 
'''
