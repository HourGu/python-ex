# -*- coding: cp936 -*-
#����sorted ,�˺������жϷ���ֵ�жϴ�С-1��x<y,0:x=y,1:x>y,Ȼ��С����ǰ������ں�
>>> sorted([2,32,12,43,34,18])
[2, 12, 18, 32, 34, 43]

def reversed_cmp(x,y):
    if x>y:
        return -1
    if x<y:
        return 1
    return 0

m=sorted([2,32,12,43,34,18],reversed_cmp)
print m

#[43, 34, 32, 18, 12, 2]
