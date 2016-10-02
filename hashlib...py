# -*- coding: utf-8 -*-
#hashlib 摘要算法，含MD5，SHA1等
#它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。
#用于保存用户密码等
>>> import hashlib
>>> md5=hashlib.md5()
>>> md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
>>> print(md5.hexdigest())
d26a53750bc40b38b65a520292f69306
>>> print(md5.digest())
ÒjSuÄ8ﾶZRﾒöﾓ
>>> 'd26a53750bc40b38b65a520292f69306'.decode('hex')
'\xd2jSu\x0b\xc4\x0b8\xb6ZR\x02\x92\xf6\x93\x06'


##account and password
import hashlib
def __calc_md5__(password):
    md5=hashlib.md5()
    md5.update(password)
    return md5.hexdigest()

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def login(user, password):
    if db[user]==__calc_md5__(password):
        return True
    else:
        return False

    
'''
>>> ================================ RESTART ================================
>>> 
>>> login('bob','abc999')
True
>>> login('alice','sakjd')
False
>>> 
'''
name    | password
--------+----------
michael | 123456
bob     | abc999
alice   | alice2008



##inhance the password with username and the-Salt
import hashlib
def __calc_md5__(password):
    md5=hashlib.md5()
    md5.update(password)
    return md5.hexdigest()

db ={}

def register(username,password):
    db[username] = __calc_md5__(password + username + 'iamsalt')


def login(username, password):
    if db[username]==__calc_md5__(password + username + 'iamsalt'):
        return True
    else:
        return False

'''   
>>> ================================ RESTART ================================
>>> 
>>> register('alice','alice2008')
>>> register('lice','alice2008')
>>> db
{'alice': 'a338492f301152667c072942c5fd41d9', 'lice': 'ae40285e187ab09e454ad02f79e4627a'}
>>> login('lice','alice2008')
True
>>> login('alice','alic2008')
False
'''

    
