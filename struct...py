﻿# -*- coding: cp936 -*-
#struct

#ִ��base����
>>> ================================ RESTART ================================
>>> import struct
>>> import base64
>>> f=open(r'E:\Python27\test.bmp','rb')
>>> m=base64.b64encode(f.read())
>>> f.close()
>>> a=m[:40] #����unpack��Ҫ��ȡ������30���ַ�������base64Ҫ��30*4/3=40���ַ�
>>> b=safe_b64decode(a)
>>> b
'BM\xd6\xe30\x00\x00\x00\x00\x006\x00\x00\x00(\x00\x00\x00\xe8\x03\x00\x00,\x04\x00\x00\x01\x00\x18\x00'
>>> struct.unpack('<ccIIIIIIHH', b)
('B', 'M', 3204054, 0, 54, 40, 1000, 1068, 1, 24)
>>> 
'<ccIIIIIIHH'�����
I��ʾ4�ֽ��޷�������
H��ʾ2�ֽ��޷�������
c������ĸ��
�ڴ�洢��
<������ֽڷ���little-endian
>������ֽڷ���big-endian�������򣬱���Ϊ����

���н����
�����ֽڣ�'BM'��ʾWindowsλͼ��'BA'��ʾOS/2λͼ��
һ��4�ֽ���������ʾλͼ��С��
һ��4�ֽ�����������λ��ʼ��Ϊ0��
һ��4�ֽ�������ʵ��ͼ���ƫ������
һ��4�ֽ�������Header���ֽ�����
һ��4�ֽ�������ͼ���ȣ�
һ��4�ֽ�������ͼ��߶ȣ�
һ��2�ֽ�������ʼ��Ϊ1��
һ��2�ֽ���������ɫ����
