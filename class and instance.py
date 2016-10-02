# -*- coding: cp936 -*-
#class & instance ���ʵ��


#��������ͨ��class�ؼ��֣�
class Student(object):
    pass

#class������������������Student������ͨ���Ǵ�д��ͷ�ĵ��ʣ��������(object)��
#��ʾ�����Ǵ��ĸ���̳������ģ��̳еĸ������Ǻ����ٽ���ͨ�������û�к��ʵļ̳��࣬
#��ʹ��object�࣬�������������ն���̳е��ࡣ


#����ʵ����ͨ������+()ʵ�ֵģ�
a=Student()
'''
>>> a
<__main__.Student object at 0x03012E30>
>>> Student
<class '__main__.Student'>
>>> 
'''

#���Ը�һ��ʵ�����������ԣ����磬��ʵ��bart��һ��name����
>>> a.name='zhaoheng'
>>> a.name
'zhaoheng'


class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score
#ͨ������һ�������__init__�������ڴ���ʵ����ʱ�򣬾Ͱ�name��score�����԰���ȥ
#ע�⵽__init__�����ĵ�һ��������Զ��self����ʾ������ʵ���������ˣ���__init__�����ڲ���
#�Ϳ��԰Ѹ������԰󶨵�self����Ϊself��ָ�򴴽���ʵ�������
#����__init__�������ڴ���ʵ����ʱ�򣬾Ͳ��ܴ���յĲ����ˣ�
#���봫����__init__����ƥ��Ĳ�������self����Ҫ����Python�������Լ����ʵ����������ȥ��
a=Student('zhaoheng',90)



##���ݷ�װ
#���ǣ���ȻStudentʵ�������ӵ����Щ���ݣ�Ҫ������Щ���ݣ���û�б�Ҫ������ĺ���ȥ���ʣ�
#����ֱ����Student����ڲ�����������ݵĺ������������Ͱѡ����ݡ�����װ�����ˡ�
#��Щ��װ���ݵĺ����Ǻ�Student�౾���ǹ��������ģ����ǳ�֮Ϊ��ķ���
#Ҫ����һ�����������˵�һ��������self�⣬��������ͨ����һ����
#Ҫ����һ��������ֻ��Ҫ��ʵ��������ֱ�ӵ��ã�����self���ô��ݣ�����������������

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print '%s: %s' % (self.name, self.score)

>>> bart.print_score()
Bart Simpson: 59

#����һ�������Ǵ��ⲿ��Student�࣬��ֻ��Ҫ֪��������ʵ����Ҫ����name��score��
#����δ�ӡ��������Student����ڲ�����ģ���Щ���ݺ��߼�������װ�������ˣ����ú����ף�
#��ȴ����֪���ڲ�ʵ�ֵ�ϸ�ڡ�

#��װ����һ���ô��ǿ��Ը�Student�������µķ���������get_grade��
class Student(object):
    ...

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

#ͬ���ģ�get_grade��������ֱ����ʵ�������ϵ��ã�����Ҫ֪���ڲ�ʵ��ϸ�ڣ�

>>> bart.get_grade()
'C'


##��ֹ�ⲿ���ʣ������Ե�����ǰ��__�����private����,ֻ���ڲ�����ͨ���������ʲ��޸�
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def print_score(self):
        print '%s:%s'%(self.__name,self.__score)

'''
>> a=Student('zhao',98)
>>> a.print_score()
zhao:98
>>> a.__name

Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    a.name
AttributeError: 'Student' object has no attribute 'name'
>>> 
'''


##�����Ҫ�޸ģ��������÷���,���ԶԴ�������ݽ��м��
class Student(object):
    ```
    def set_score(self,score):
        if 0<=score<=100:
            self.__score=score
        else:
            raise ValueError('�������'��

'''
>>> a=Student('zhao',98)
>>> a.print_score()
zhao:98
>>> a.get_grade ()
'A'
>>> a.set_score (56)

>>> a.get_grade()
'C'
>>> a.set_score(289)

Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    a.set_score(289)
  File "E:\Python27\python ex\class std.py", line 32, in set_score
    raise ValueError('bad score')
ValueError: bad score
>>> 

'''
                             
        





