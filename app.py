# -*- coding: utf-8 -*-

#
# @date 2016/04/12
# @auther me@fengyao.me
# @desc How to create a separate config file with flask
# @record 
#


from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('config.cfg')

print app.config['HELLO']