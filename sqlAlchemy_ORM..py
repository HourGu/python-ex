# -*- coding: utf-8 -*-
#ORM:object-Relational Mapping,把关系数据库的表结构映射到对象上
from sqlalchemy import Column,String,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()

class User(Base):
    __tablename__='student'


    id=Column(String(20),primary_key=True)
    name=Column(String(20))




db_config={
    'host':'127.0.0.1',
    'user':'python',
    'password':'123456',
    'db':'test',
    'charset':'utf8'}

engine=create_engine('mysql://%s:%s@%s/%s?charset=%s'%(db_config['user'],
                                                       db_config['password'],
                                                       db_config['host'],
                                                       db_config['db'],
                                                       db_config['charset']),echo=True)

DBSession=sessionmaker(bind=engine)
# 创建session对象:
session = DBSession()
# 创建新User对象:
#new_user = User(id='5', name='Bob')
# 添加到session:
#session.add(new_user)
# 提交即保存到数据库:
#session.commit()
'''
mysql> select * from student;
+----+------+
| ID | name |
+----+------+
|  1 | b    |
|  2 | c    |
|  5 | Bob  |
+----+------+
3 rows in set (0.00 sec)

mysql>
'''

# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id=='5').one()
# 打印类型和对象的name属性:
print 'type:', type(user)
print 'name:', user.name
# 关闭Session:
session.close()
