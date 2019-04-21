from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import DataRequired,Length


#创建留言表单  用的是flask中的wtforms
class HelloForm(FlaskForm):
	name = StringField('姓名：',validators=[DataRequired(),Length(1,30)])
	body = TextAreaField('留言 ',validators=[DataRequired(),Length(1,300)])
	submit = SubmitField()
