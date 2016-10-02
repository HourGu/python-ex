# -*- coding: cp936 -*-
###metaclass Ԫ��.�ȶ���metaclass���Ϳ��Դ����࣬��󴴽�ʵ����
#����԰��࿴����metaclass���������ġ�ʵ������
#metaclass�Ǵ����࣬���Ա����`type`����������
class ListMetclass(type):
    def __new__(cls,name,bases,attrs):
        attrs['add']=lambda self,value:self.append(value)
        return type.__new__(cls,name,bases,attrs)

class MyList(list):
     __metaclass__=ListMetclass #ָʾʹ��ListMetaclass��������


'''
>>> L=MyList()
>>> L.add(1)
>>> L
[1]
>>> L.add(8)
>>> L
[1, 8]
>>> 
'''
