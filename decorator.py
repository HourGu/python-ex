# -*- coding: cp936 -*-
#������ decorator
def now():
    print '2016-9-6'

##

def lazy_sum(*args):
    def sum():
        ax=0
        for n in args:
            ax=ax+n
        return ax
    return sum
'''
>>> f=lazy_sum(1,2,3,21)
>>> f()
27
>>> lazy_sum(1,2,3,21)()
27
>>> lazy_sum(1,2,3,21)
<function sum at 0x03192970>
����sum������ʵ���õ��ĺ������൱��lazy_sum(1,2,3,21)()����lazy_sum��һ����װ�Եĺ���
����ƿ�Ӻ�ƿ�����ˮһ��
'''
##

#*args���Ե��������ɶ��������ɵ�tuple,**kwargs���Ե������ɶ��key��value��dictionary
#���߶���Ϊ��ȷ���������뺯�����βΣ�
#wrapper()�����Ĳ���������(*args, **kw)����ˣ�wrapper()�������Խ�����������ĵ���
def log(text): #now = log('execute')(now)
    def decorator(fun):#log���������������ܣ�1.��ԭ���ĺ����������У�2.��������ǰ��ӡ��־
        def wrapper(*args, **kw):   
            print 'call %s():' % fun.func_name
            return fun(*args, **kw)
        return wrapper
    return decorator

@log #��ִ��now()ʱ��ֻ��Ĭ��ִ��log����������now��Ϊʵ�δ���fun���βΣ�
     #log�����ٵ���now��
def now():
    print '2013-12-25'

'''
>>> now()
call now():
2013-12-25
>>> now.func_name
'wrapper'
'''
##
#����now�ĺ��������ձ����wrapper�����Կ��Ե���ģ��functools���������������ڵ���
#wrapper����ǰ��@functoos.wraps(fun)
# -*- coding: cp936 -*-
import functools
def log(fun):
        @functools.wraps(fun)
        def wrapper(*args, **kw):   
            print 'call %s():' % (fun.func_name)
            return fun(*args, **kw)
        return wrapper
    

@log
def now():
    print '2013-12-25'
'''
call now():
2013-12-25
>>> now.func_name
'now'
'''


##
def log(func):
    print 'call %s():' % func.__name__
    return func()
    
@log
def now():
    print '2013-12-25'
'''    
call now():
2013-12-25
�����Ľ�����Զ��ó������û�о��������ߵĵ��ã�����log��Ҫ����һ������
'''



##homework:
#1.���дһ��decorator��
#���ں������õ�ǰ���ӡ��'begin call'��'end call'����־��
import functools
def log(fun):
    @functools.wraps(fun)
    def wrapper(*args,**kwargs):
        print 'begin call %s():'%fun.func_name
        fun(*args,**kwargs)
        print 'end call %s().'%fun.func_name   
    return wrapper

@log
def now():
    print '2016-9-6'

'''
begin call now():
2016-9-6
end call now().
'''

#2.��дһ��ͨ�õ�log���������㲻��text��������ܵ���
# -*- coding: cp936 -*-
import functools

def log(text):
    if callable(text):#����Ǻ���ʱ���ɵ���
        @functools.wraps(text)
        def wrapper(*args,**kwargs):
            print 'begin call %s():'%text.func_name
            text(*args,**kwargs)
            print 'end call %s().'%text.func_name   
        return wrapper
    
    else: #���text���ַ���ʱ�����ɵ���
        def decorator(fun):
            @functools.wraps(fun)
            def wrapper(*args, **kwargs):   
                print 'begin call %s %s():'%(text,fun.func_name)
                fun(*args,**kwargs)
                print 'end call %s %s().'%(text,fun.func_name)
            return wrapper
        return decorator  

@log
def now():
    print '2016-9-6'

@log('next')
def later():
    print '2016-9-7'
    
'''
>>> later()
begin call next later():
2016-9-7
end call next later().
>>> now()
begin call now():
2016-9-6
end call now().
>>>
'''
