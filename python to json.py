# -*- coding: cp936 -*-
#�ڲ�ͬ�ı������֮�䴫�ݶ��󣬾ͱ���Ѷ������л�Ϊ��׼��ʽ������JSON
>>> import json
>>> d=dict(name='Bob', age=20, score=88)
>>> json.dumps(d)
'{"age": 20, "score": 88, "name": "Bob"}'
>>> json.loads(json.dumps(d))#�����л��õ�����Unicode����ַ�������
{u'age': 20, u'score': 88, u'name': u'Bob'}
>>> 


##json����,��class�����ڵ�ʵ���������л�
import json
class Student(object):
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score

s=Student('Bob',23,55)
print json.dumps(s)

'''

Traceback (most recent call last):
  File "E:\Python27\temporary.py", line 9, in <module>
    print json.dumps(s)
  File "E:\Python27\lib\json\__init__.py", line 243, in dumps
    return _default_encoder.encode(obj)
  File "E:\Python27\lib\json\encoder.py", line 207, in encode
    chunks = self.iterencode(o, _one_shot=True)
  File "E:\Python27\lib\json\encoder.py", line 270, in iterencode
    return _iterencode(o, 0)
  File "E:\Python27\lib\json\encoder.py", line 184, in default
    raise TypeError(repr(o) + " is not JSON serializable")
TypeError: <__main__.Student object at 0x02FE81F0> is not JSON serializable
>>> 
'''
#json(object) ֻ�ܶ�dict�������л�����class��ת��
import json
class Student(object):
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score


def student2dict(std):
    return {
        'name':std.name,
        'age':std.age,
        'score':std.score
        }


s=Student('Bob',23,55)
print json.dumps(s,default=student2dict)

'''
>>> 
{"age": 23, "score": 55, "name": "Bob"}
>>> 
'''


#class�����л����ȶ���һ������json�͵��ַ�����������ĺ���
def dict2student(d):
    return Student(d['name'],d['age'],d['score'])
json_str='{"age": 23, "score": 55, "name": "Bob"}'
print json.loads(json_str,object_hook=dict2student)

'''
>>> 
<__main__.Student object at 0x02FB8270>
>>> 
'''


##Ҳ����ֱ�ӽ�class��ת��Ϊdict�ำ��default,��Ϊclass�е�ʵ��__dict__���Դ洢ʵ������
import json
class Student(object):
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score

s=Student('Bob',23,55)
print(json.dumps(s,default=lambda obj:obj.__dict__)

'''
>>> 
{"age": 23, "score": 55, "name": "Bob"}
>>> 
'''

