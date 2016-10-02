# -*- coding: cp936 -*-
##mysql
>>> import MySQLdb
>>> MySQLdb.connect('localhost','python','123456','test')

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    MySQLdb.connect('localhost','python','123456','test')
  File "E:\Python27\lib\site-packages\MySQLdb\__init__.py", line 81, in Connect
    return Connection(*args, **kwargs)
  File "E:\Python27\lib\site-packages\MySQLdb\connections.py", line 193, in __init__
    super(Connection, self).__init__(*args, **kwargs2)
OperationalError: (2003, "Can't connect to MySQL server on 'localhost' (10061)")
#���Ӹ�ʽ
>>> con= MySQLdb.Connect(host="127.0.0.1", port=3306, user="python", passwd="123456", db="test")

>>> cursor=con.cursor ()
>>> cursor.execute('select version()')
1L
#��ȡ�汾��Ϣ
>>> data=cursor.fetchone()
>>> print 'database version:%s'%data
database version:5.7.15

#������employee
>>> cursor.execute ('drop table if exists employee')

Warning (from warnings module):
  File "__main__", line 1
Warning: Unknown table 'test.employee'
0L

>>> cursor.execute('select * from YourClass')
2L
>>> sql="""create table employee(
		first_name char(20) not null,
		last_name char(20),
		age int,
		sex char(1),
		income float)"""
>>> cursor.execute(sql)
0L
>>> con.close()
>>> db= MySQLdb.Connect(host="127.0.0.1", port=3306, user="python", passwd="123456", db="test")
>>> cursor=db.cursor ()

>>> sql="""insert into employee(first_name,
		last_name,
		age,
		sex,
		income)
	values('Mac','Mohan',20,'m',2000)"""

>>> try:
   # ִ��sql���
   cursor.execute(sql)
   # �ύ�����ݿ�ִ��
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

   
1L
>>> 

'''
mysql> use test;
Database changed
mysql> select * from employee;
+------------+-----------+------+------+--------+
| first_name | last_name | age  | sex  | income |
+------------+-----------+------+------+--------+
| Mac        | Mohan     |   20 | m    |   2000 |
+------------+-----------+------+------+--------+
1 row in set (0.00 sec)

mysql>
'''



>>> sql="""insert into employee(first_name,
		last_name,
		age,
		sex,
		income)
	values('Lina','Gu',20,'w',3000)"""
>>> try:
   # ִ��sql���
	   cursor.execute(sql)
   # �ύ�����ݿ�ִ��
	   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

   
1L
'''
mysql> select * from employee;
+------------+-----------+------+------+--------+
| first_name | last_name | age  | sex  | income |
+------------+-----------+------+------+--------+
| Mac        | Mohan     |   20 | m    |   2000 |
| Lina       | Gu        |   20 | w    |   3000 |
+------------+-----------+------+------+--------+
2 rows in set (0.00 sec)

mysql>
'''
>>> sql="select * from employee where income >'%d'"%(1000)
>>> try:
	cursor.execute(sql)
	results=cursor.fetchall()
	for row in results:
		fname=row[0]
		lname=row[1]
		age=row[2]
		sex=row[3]
		income=row[4]
		print "fname=%s,lname=%s,age=%d,sex=%s,income=%d"%\
		      (fname,lname,age,sex,income)
except:
	print "Error:unable to fecth data"

	
2L
fname=Mac,lname=Mohan,age=20,sex=m,income=2000
fname=Lina,lname=Gu,age=20,sex=w,income=3000
>>> 

>>> sql="update employee set age=age+1 where sex='%c'"%('m')
>>> try:
   # ִ��SQL���
	   cursor.execute(sql)
   # �ύ�����ݿ�ִ��
	   db.commit()
except:
   # ��������ʱ�ع�
   db.rollback()

   
1L
>>> db.close()
'''
mysql> select * from employee;
+------------+-----------+------+------+--------+
| first_name | last_name | age  | sex  | income |
+------------+-----------+------+------+--------+
| Mac        | Mohan     |   21 | m    |   2000 |
| Lina       | Gu        |   20 | w    |   3000 |
+------------+-----------+------+------+--------+
2 rows in set (0.00 sec)

mysql>
'''
