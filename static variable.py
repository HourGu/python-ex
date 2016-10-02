# -*- coding: cp936 -*-
#�ɱ����

def calc(*numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum
'''    
>>> a=(1,3,4)
>>> calc(*a)
26

#������趨��һ��tuple����list����
def calc(numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum

>>> a=([1,3,4])
>>> calc(a)
26
