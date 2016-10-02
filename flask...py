# -*- coding: cp936 -*-
from flask import Flask
from flask import request

app=Flask(__name__)

@app.route('/',methods=['Get','Post'])#/Ĭ��Ϊ127.0.0.1/,����
def home():
    return '<h1>Home</h1>'

@app.route('/signin',methods=['Get'])#url��127.0.0.1/signin��get����
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</p>
              </form>'''

@app.route('/signin',methods=['Post'])#url��127.0.0.1/signin��post����
def signin():
    #��Ҫ��request�����ȡ������ݣ�
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello,admin!</h3>'
    return '<h3>Bad username or password.</h3>'

if __name__=='__main__':
    app.run()

    
