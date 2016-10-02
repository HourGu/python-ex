# -*- coding: cp936 -*-
##debug
#assert
def foo(s):
    n=int(s)
    assert n!=0,'n is zero!'#����ĳ��ʧ�ܣ��׳�����AssertionError+��������
    return 10/n

def main():
    foo('0')

'''

Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    main()
  File "E:\Python27\python ex\debug.py", line 9, in main
    foo('0')
  File "E:\Python27\python ex\debug.py", line 5, in foo
    assert n!=0,'n is zero!'
AssertionError: n is zero!
>>> 
'''

##pdb
s = '0'
n = int(s)
print 10 / n

'''CMD�����²���
C:\Users\KF>python -m pdb E:\Python27\temporary.py
> e:\python27\temporary.py(1)<module>()
-> s = '0'
(Pdb) n
> e:\python27\temporary.py(2)<module>()
-> n = int(s)
(Pdb) n
> e:\python27\temporary.py(3)<module>()
-> print 10 / n
(Pdb) p s
'0'
(Pdb) p n
0
(Pdb) q

C:\Users\KF>
'''

s = '0'
n = int(s)
pdb.set_trace()#set a breakpoint
print 10 / n

'''
CMD
C:\Users\KF>python E:\Python27\temporary.py
> e:\python27\temporary.py(5)<module>()
-> print 10 / n
(Pdb) p n
0
(Pdb) c  #continue
Traceback (most recent call last):
  File "E:\Python27\temporary.py", line 5, in <module>
    print 10 / n
ZeroDivisionError: integer division or modulo by zero

C:\Users\KF>
'''

