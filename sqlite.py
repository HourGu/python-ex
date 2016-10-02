# -*- coding: cp936 -*-
##SQLite
# ����SQLite����:
>>> import sqlite3
# ���ӵ�SQLite���ݿ�
# ���ݿ��ļ���test.db
# ����ļ������ڣ����Զ��ڵ�ǰĿ¼����:
>>> conn = sqlite3.connect('test.db')
# ���ӵ����ݿ����Ҫ���α꣬��֮ΪCursor��ͨ��Cursorִ��SQL��䣬Ȼ�󣬻��ִ�н��������һ��Cursor:
>>> cursor = conn.cursor()
# ִ��һ��SQL��䣬����user��:
>>> cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
<sqlite3.Cursor object at 0x10f8aa260>
# ����ִ��һ��SQL��䣬����һ����¼:
>>> cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
<sqlite3.Cursor object at 0x10f8aa260>
# ͨ��rowcount��ò��������:
>>> cursor.rowcount
1
# �ر�Cursor:
>>> cursor.close()
# �ύ����:
>>> conn.commit()
# �ر�Connection:
>>> conn.close()
