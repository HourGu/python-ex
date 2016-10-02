# -*- coding: cp936 -*-
#������ϡ�˳������Ϊ��ѡ������Ĭ�ϲ������ɱ����(����tuple)�͹ؼ��ֲ���������dict��
def func(a,b,c=0,*args,**kw):
    print 'a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw
    
'''
>>> e=(1,2,3,4)
>>> fg={'x':12,'y':13}
>>>  func(*de,**fg)
>>> func(*e,**fg)
a= 1 b= 2 c= 3 de= (4,) fg= {'y': 13, 'x': 12}
>>> 
'''
