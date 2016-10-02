# -*- coding: cp936 -*-
#쳲���������
def fib(max):
    n,a,b=0,1,1
    while n<max:
        yield a
        a,b=b,a+b
        n=n+1
    

