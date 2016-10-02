# -*- coding: cp936 -*-
#filter ,��map()���ƣ�filter()Ҳ����һ��������һ������filter()�Ѵ���ĺ�������������ÿ��Ԫ�أ�
#Ȼ����ݷ���ֵ��True����False����������Ƕ�����Ԫ�ء�


#�������
def odd(n):
    return n%2==1
'''
>>> filter(odd,[23,43,12,3,456])
[23, 43, 3]
'''

#���1-100������
def composite_num(n):
    if n==1:
        return True
    else:
        return [n%i for i in range(1,n)].count(0)>=2
        
m=filter(composite_num,range(101))
print m
