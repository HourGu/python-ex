# -*- coding: cp936 -*-
#������Ϊ����ֵ���հ�,ÿ�ε��ö��᷵�ز�ͬ�ĺ�������ʹ������ͬ
def lazy_sum(*args):
    def sum():
        ax=0
        for n in args:
            ax=ax+n
        return ax
    return sum

'''
>>> f=lazy_sum(1,3,43,2)
>>> f
<function sum at 0x02FA2970>
>>> f()
49
>>> 
'''

#�ȿ����صĺ�����ʽ������������õĺ�����
def count():
    fs=[]
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
f1,f2,f3=count()

'''
>>> f1() 
9
>>> f3()
9
>>>count()�������ص���fs��list������f�����f���ڷ���ʱ�ؼ���ֵ������ʱi=3
'''



def count():
    fs=[]
    for i in range(1,4):
        
        def f(j):
            def g():
                return j*j
            return g  #���ﷵ�ص���g�����������f(j)��һ��������ɵ�list��
        fs.append(f(i))
    return fs

f1,f2,f3=count()


# -*- coding: cp936 -*-
def count():
    fs=[]
    for i in range(1,4):
        def f(i):
            return i*i
        fs.append(f(i))#���ﷵ�ص����Ѿ����������f��i�������,����f1,f2,f3��
                       #����ɵ�list�����Ҫ��f1�����ĺ�����ʽ���ã��ǲ��ܵ�������
                        #ֻ����f1��f2,f3����
        return fs
f1,f2,f3=count()

def count():
    fs = []
    for i in range(1, 4):
        def f(j=i):#���ｫi����j�Ĺ����а󶨵�ǰ����������
             return j*j
        fs.append(f)
    return fs

f1, f2, f3 = count()



def build(x, y):
    return lambda: x * x + y * y#����������Ϊֵ����
>>> build(3,3)()
18

