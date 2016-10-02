# -*- coding: cp936 -*-
##with
#with fun as class,���������õ���
class Sample:
   
    def __enter__(self):
        print "In__enter__()"
        return "Foo" 
 
    def __exit__(self,type,value,trace):
        print "In __exit__()"
 
 
def get_sample():
    return Sample()

'''
>>> with get_sample() as sample:  
	print 'sample:',sample

	
In__enter__()
sample: Foo
In __exit__()
>>> 

'''

class Sample:
    def __enter__(self):
        return self

    def __exit__(self, type, value, trace):
        print "type:", type
        print "value:", value
        print "trace:", trace

    def do_something(self):
        bar = 1/0
        return bar + 10

with Sample() as sample:
    sample.do_something()


'''
type: <type 'exceptions.ZeroDivisionError'>
value: integer division or modulo by zero
trace: <traceback object at 0x02F1B148>

Traceback (most recent call last):
  File "E:\Python27\temporary.py", line 15, in <module>
    sample.do_something()
  File "E:\Python27\temporary.py", line 11, in do_something
    bar = 1/0
ZeroDivisionError: integer division or modulo by zero
>>> 
'''
