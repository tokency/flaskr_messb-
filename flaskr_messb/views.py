from flask import flash,redirect,url_for,render_template

from flaskr_messb import app,db
from flaskr_messb.models import Message
from flaskr_messb.forms import HelloForm

@app.route('/',methods=['POST','GET'])
def index():
	#数据库操作  加载所有记录
	messages = Message.query.order_by(Message.timestamp.desc()).all()
	form = HelloForm()
	if form.validate_on_submit():
		name = form.name.data
		body = form.body.data
		message = Message(body=body,name=name) #实例化模型类，创建记录
		db.session.add(message) #添加记录到数据库会话
		db.session.commit() #提交会话
		flash('你的留言已经成功发布！')
		return redirect(url_for('index'))  #重定向到index视图
	return render_template('index.html',form=form,messages=messages)