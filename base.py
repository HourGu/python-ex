# -*- coding: cp936 -*-
#base64����ͽ���ʱ����Ҫ��=��������
#����ʱ���������ݲ���3�ı���������ʱ����4�ı���
#�� ���ÃȽ�ģ�顷base64
import base64

def __fstr__(fun_str):
    n=len(fun_str)%4
    complete_str=fun_str+'='*(4-n)
    return complete_str

def safe_b64decode(original_str):
    complete_str=__fstr__(original_str)
    return base64.b64decode(complete_str)
