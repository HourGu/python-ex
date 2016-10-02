# -*- coding: cp936 -*-
#Ĭ�ϲ���ֵ�����ǲ������
#����������end
#�����������ȼ��㺯����ֵ���ٸ�����Ӧ�ı�����
'''
def add_end(L=[]):
    L.append('end')
    return L

>>> x=add_end([1,2])
>>> x
[1, 2, 'end']
>>> y=add_end()
>>> y
['end']
>>> y=add_end()
>>> y
['end', 'end']
>>> 
'''


#Ҫ�޸���������ӣ����ǿ�����None������������ʵ�֣�
def add_end(L=None):
    if L is None:
        L=[]
    L.append('end')
    return L
