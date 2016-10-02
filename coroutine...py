# -*- coding: cp936 -*-
import time

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %d...' % n)
        time.sleep(1)
        r = '200 OK'

def produce(c):
    c.next()
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %d...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

if __name__=='__main__':
    c = consumer()
    produce(c)

#next������sent��value�������Ը�yieldִ��
#c��һ��consumer��������generator��ֵ��r��Ȼ����produce�������ε���ִ��
#��һ�ε���c.next()�޷���ֵ��ֻ�����generator��generater���б����е�һ����ֵ��������е�����r��ֵ
#whileѭ����c.send(value)����valueֵ����n��if�ж�ʧ�ܣ�����return��
#���consumer��n������ͣʱ�䣬����rֵ����yield����r������һ��ѭ����
        
