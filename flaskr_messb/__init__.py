from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_moment import Moment

#将config.py里面的参数传入道程序实例中来
app = Flask('flaskr_messb')
app.config.from_pyfile('config.py')

#去掉jinja2语句占据的空行 设置
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True
#数据库变量db
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

from flaskr_messb import views,errors,commands