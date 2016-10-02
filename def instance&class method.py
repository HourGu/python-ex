#def instance&class method by methodType
class Student(object):
    pass

#give instance an attribute
>>> s=Student()
>>> s.name='Michael'
>>> print s.name
Michael
>>> 

#give instance a method,except for other instances
>>> def set_age(self,age):
	self.age=age

	
>>> from types import MethodType
>>> s.set_age=MethodType(set_age,s,Student)
>>> s.set_age(32)
>>> s.age
32


#give class a method,serves for any instance
>>> def set_score(self,score):
	self.score=score

	
>>> Student.set_score=MethodType(set_score,None,Student)
>>> s.set_score (32)
>>> s2=Student()
>>> s2.set_score(12)
>>> s.score
32
>>> s2.score
12

