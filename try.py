# -*- coding: cp936 -*-
##try
try:
    print 'try```'
    r=10/0
    print 'result',r
except ZeroDivisionError,e:
    print 'except',e
finally:
    print 'finally```'
print 'END'

'''
try```
except integer division or modulo by zero
finally```
END
>>> 
'''

try:
    print 'try...'
    r = 10 / int('a')
    print 'result:', r
except ValueError, e:
    print 'ValueError:', e
except ZeroDivisionError, e:
    print 'ZeroDivisionError:', e
else:
    print 'no error!'
finally:
    print 'finally...'
print 'END'

'''
>>> 
try...
ValueError: invalid literal for int() with base 10: 'a'
finally...
END
>>> 

#BaseException>StandartError>ValueError
'''
#ʹ��try...except���������һ���޴�ĺô������ǿ��Կ�Խ������
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except StandardError, e:
        print 'Error!'
    finally:
        print 'finally...'



#logging����¼���󣬲��������˳�
# err.py
import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except StandardError, e:
        logging.exception(e)

main()
print 'END'

'''
ERROR:root:integer division or modulo by zero
Traceback (most recent call last):
  File "E:\Python27\temporary.py", line 12, in main
    bar('0')
  File "E:\Python27\temporary.py", line 8, in bar
    return foo(s) * 2
  File "E:\Python27\temporary.py", line 5, in foo
    return 10 / int(s)
ZeroDivisionError: integer division or modulo by zero
END
>>> 
'''


##def fault class
class FooError(StandardError):
    pass

def foo(s):
    n=int(s)
    if n==0:
        raise FooError('invalid value:%s'%s)
    return 10/n

'''
>>> foo('0')

Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    foo('0')
  File "E:\Python27\temporary.py", line 7, in foo
    raise FooError('invalid value:%s'%s)
FooError: invalid value:0
>>> foo('4')
2
>>> 
'''

