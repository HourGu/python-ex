# -*- coding: cp936 -*-
#threading.Thread����:targetָҪִ�еĺ�������argsΪ����Ĳ�������a����������ʽ���룬
#���õĽ����ں���������ģ����ڡ�name��Ϊ�߳��������֣���threading.current_thread().name��ֵ
#ThreadLocal,
import threading

# ����ȫ��ThreadLocal����:
local_school = threading.local()

def process_student():
    print 'Hello, %s (in %s)' % (local_school.student, threading.current_thread().name)

def process_thread(std_name):
    # ��ThreadLocal��student:
    local_school.student = std_name#����ʱ���dict
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
