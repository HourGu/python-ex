# -*- coding: cp936 -*-
#ƫ����partial function
int('12343',base=8)#int���԰��ַ���ת��Ϊ������base�����ַ������������8���ƣ�
                   #������Ϊ10����
#5347

##
#����ת���ĺ���
def str2int(s,base=2):
    return int(s,base)

'''
>>> str2int('0101101')
45
>>> 
'''

##functools.partial���ǰ������Ǵ���һ��ƫ�����ģ�
##����Ҫ�����Լ�����str2int()������ֱ��ʹ������Ĵ��봴��һ���µĺ���int2��
#functools.partial�����þ��ǣ���һ��������ĳЩ�������̶�ס��Ҳ��������Ĭ��ֵ����
#����һ���µĺ�������������º�������򵥡�
import functools
str2int=functools.partial(int,base=2)
