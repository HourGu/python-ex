# -*- coding: cp936 -*-
#multithreading,���һ���߳̾��ǰ�һ���������벢����Threadʵ����Ȼ�����start()��ʼִ��
import time,threading
def loop():
    print 'thread %s is running...'%threading.current_thread().name
    n=0
    while n<5:
        n=n+1
        print 'thread %s >>> %s'%(threading.current_thread().name,n)
        time.sleep(1)#�м������е�����
    print 'thread %s is ended.'%threading.current_thread().name


print 'thread %s is running...'%threading.current_thread().name
t=threading.Thread(target=loop,name='LoopThread')
t.start()
t.join()
print 'thread %s ended.'%threading.current_thread().name

'''
thread MainThread is running...
thread LoopThread is running...
thread LoopThread >>> 1
thread LoopThread >>> 2
thread LoopThread >>> 3
thread LoopThread >>> 4
thread LoopThread >>> 5
thread LoopThread is ended.
thread MainThread ended.
>>> 
'''

'''
�����κν���Ĭ�Ͼͻ����һ���̣߳����ǰѸ��̳߳�Ϊ���̣߳����߳��ֿ�������µ��̣߳�
Python��threadingģ���и�current_thread()����������Զ���ص�ǰ�̵߳�ʵ����
���߳�ʵ�������ֽ�MainThread�����̵߳������ڴ���ʱָ����������LoopThread�������̡߳�
���ֽ����ڴ�ӡʱ������ʾ����ȫû���������壬
�����������Python���Զ����߳�����ΪThread-1��Thread-2����
���̺߳Ͷ�������Ĳ�ͬ���ڣ�������У�ͬһ��������������һ�ݿ���������ÿ�������У�
����Ӱ�죬�����߳��У����б������������̹߳�������ԣ�
�κ�һ�����������Ա��κ�һ���߳��޸ģ���ˣ�
�߳�֮�乲����������Σ�����ڶ���߳�ͬʱ��һ�������������ݸ������ˡ����£�
'''
import time, threading

# �ٶ�����������д��:
balance = 0

def change_it(n):
    # �ȴ��ȡ�����Ӧ��Ϊ0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        change_it(n)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print balance
'''
>>> ================================ RESTART ================================
>>> 
2743
>>> ================================ RESTART ================================
>>> 
-608
>>> 
'''

#lock,threading.Lock()
# -*- coding: cp936 -*-
import time, threading

# �ٶ�����������д��:
balance = 0
lock=threading.Lock()

def change_it(n):
    # �ȴ��ȡ�����Ӧ��Ϊ0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        #��Ҫ��ȡ��
        lock.acquire()
        try:
            #���ĸ�
            change_it(n)
        finally:
            lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print balance
'''
>>> ================================ RESTART ================================
>>> 
0
'''


