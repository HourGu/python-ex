﻿# -*- coding: cp936 -*-
#multiprocessing,multiprocessingģ���ṩ��һ��Process��������һ�����̶���
#os.getpid()��ǰ���̣�os.getppid()������
from multiprocessing import Process
import os

def run_proc(name):
    print 'run child process %s(%s)...'%(name,os.getpid())

if __name__=='__main__':
    print 'Parent process %s.'%os.getpid()
    p=Process(target=run_proc,args='test')
    print 'Process will start.'
    p.start()
    p.join()#join()�������Եȴ��ӽ��̽������ټ����������У�ͨ�����ڽ��̼��ͬ��
    print 'Process end.'