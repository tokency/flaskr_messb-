import os

from flaskr_messb import app

dev_db = 'sqlite:////' + os.path.join(os.path.dirname(app.root_path),'data.db') #split URI的格式就是sqlite:/// (内存格式固定为3个/)；配置文件被放置文件夹内，要获取根目录的数据库文件 故用os.path.dirname(app.root_path)

SECRET_KEY = os.getenv('SECRET_KEY','secret string') #设置密钥 为secret string
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI',dev_db)