###type
class Hello(object):
    def hello(self,name='world'):
        print 'hello %s!'%name
        
>>> h=Hello()       
>>> h.hello()
hello world!
>>> type(hello)

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    type(hello)
NameError: name 'hello' is not defined
>>> print type(Hello)
<type 'type'>
>>> print type(h)
<class '__main__.Hello'> #instance
>>> 

##type,making a class object
def fn(self,name='world'):
    print 'hello %s!'%name

Hello=type('Hello',(object,),dict(hello=fn))#make a class,type(name,base,dict)
