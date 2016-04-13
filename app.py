# -*- coding: utf-8 -*-

#
# @date 2016/04/12
# @auther me@fengyao.me
# @desc How to create a separate config file with flask
# @record 
#

import os

# set environment variable
os.environ["FLASK_SETTING"] = "./config_file.ext"


from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
# get config from ENVIRONMENT VARIABLE 
app.config.from_envvar("FLASK_SETTING")

print app.config['HELLO']
print app.config['TEST_ENVVAR']