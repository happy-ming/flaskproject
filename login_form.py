# -*- coding:utf-8 -*-
# 个人项目
# 开发时间：2022/6/13 15:25
import wtforms
from wtforms.validators import length,email

class Login(wtforms.Form):
    '''
    label（第一个参数）：Field的label的文本。
    validators：验证器。
    id：Field的id属性，默认不写为该属性名。
    default：默认值。
    widget：指定的html控件
    '''
    email = wtforms.StringField(validators=[length(min=5,max=20),email()])
    password = wtforms.StringField(validators=[length(min=6,max=10)])
'''
验证器validators：
    Email：验证上传的数据是否为邮箱。
    EqualTo：验证上传的数据是否和另外一个字段相等，常用的就是密码和确认密码两个字段是否相等。
    InputRequired：原始数据的需要验证。如果不是特殊情况，应该使用InputRequired。
    Length：长度限制，有min和max两个值进行限制。
    NumberRange：数字的区间，有min和max两个值限制，如果处在这两个数字之间则满足。
    Regexp：自定义正则表达式。
    URL：必须要是URL的形式。
    UUID：验证UUID。`
'''