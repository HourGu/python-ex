# -*- coding: cp936 -*-
#pickling,���л����ѱ������ڴ��б�ɿɴ洢����Ĺ��̳�֮Ϊ���л�
try:
    import cPickle as pickle#���ȴ���cPickle,�ٶȽϿ�
except ImportError:
    import pickle

d=dict(name='Bob',age=23,score=44)
f=open('dump.txt','wb')
pickle.dump(d,f)
f.close()

f=open('dump.txt','rb')
d=pickle.load(f)
f.close()

>>> d
{'age': 23, 'score': 44, 'name': 'Bob'}
>>> 
