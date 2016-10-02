#__slots__  , limits attributes of instance,just serves for the class
class Student(object):
    __slots__=('name','age')
    
>>> s=Student()
>>> s.name=23
>>> s.age=32
>>> s.score=32

Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    s.score=32
AttributeError: 'Student' object has no attribute 'score'
>>> 

>>> class GraduateStudent(Student):
	pass

>>> g=GraduateStudent()
>>> g.score=78
>>> 
