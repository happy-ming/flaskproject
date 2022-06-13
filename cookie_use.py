# -*- coding:utf-8 -*-
# 个人项目
# 开发时间：2022/6/13 14:45
'''
cookie作用：
    第一次登录后服务器返回一些数据（cookie）给浏览器，
    然后浏览器保存在本地，当该用户发送第二次请求的时候，
    就会自动的把上次请求存储的cookie数据自动的携带给服务器，
    服务器通过浏览器携带的数据就能判断当前用户是哪个了。

session出现：
    cookie是存储在本地浏览器，session是一个思路、一个概念、
    一个服务器存储授权信息的解决方案，不同的服务器，不同的框架，
    不同的语言有不同的实现。虽然实现不一样，但是他们的目的都是服务器为了方便存储数据的。
    session的出现，是为了解决cookie存储数据不安全的问题的。
'''
from flask import Flask,Response,request,session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abcdefg'

# 设置cookie
@app.route('/set_cookie')
def set_cookie():
    response = Response("cookie设置")
    response.set_cookie('user_id','xxx')
    return response

# 获取cookie
@app.route('/get_cookie')
def get_cookie():
    user_id = request.cookies.get('user_id')
    print('user_id:',user_id)
    return "获取cookie"

# 设置session
@app.route('/set_session')
def set_session():
    # 在flask中，session是先把数据经过加密，然后用session. id作为key,存放到cookie中
    # #因为session会经过加密再存储到cookie中，所以我们的敏感信息，会存放到session中
    session['username'] = '张三'
    return 'seesion设置成功'

# 获取session
@app.route('/get_session')
def get_session():
    username = session.get('username')
    return "用户名："+username

@app.route('/')
def hello_world():
    return 'hello world'

if __name__ == '__main__':
    app.run(debug=True)



