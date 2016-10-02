# -*- coding: cp936 -*-
#mutiple inheritance,ͬһ�����̳п�ǰ��
class Animal(object):
    pass

class Runnable(object):
    def run(self):
        print 'Running```'
class Flyable(object):
    def run(self):
        print 'Flying```'


class Mammal(Animal):
    pass
class Bird(Animal):
    pass


class Dog(Mammal,Runnable):
    pass
class Bat(Mammal,Flyable):
    pass
class Parrot(Bird,Flyable):
    pass
class Ostrich(Bird,Runnable):
    pass

#Mixin  other inheritance except super class
class Dog(Mammal,RunnableMixin):
    pass

class MyTCPServer(TCPServer,ForkingMixin):#�����ģʽ��TCP����
    pass

class MyUDPServer(UDPserver,ThreadngMixin):#���߳�ģʽ��UDP����
    pass

class MyTCPServer(TCPServer,CoroutineMixin):#Э��TCP����
    pass
