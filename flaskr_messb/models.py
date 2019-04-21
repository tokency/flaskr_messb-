from datetime import datetime
from flaskr_messb import db

#定义数据库字段模型

class Message(db.Model):
	
	id = db.Column(db.Integer,primary_key=True)
	body = db.Column(db.String(500))
	name = db.Column(db.String(20))
	timestamp =  db.Column(db.DateTime,default=datetime.utcnow,index=True)