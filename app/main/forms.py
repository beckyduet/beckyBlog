from flask_wtf import FlaskForm
from wtforms.fields import *
from wtforms.validators import DataRequired


class newsletterForm(FlaskForm):
    name = StringField('订阅newsletter：', validators=[DataRequired()])
    submit = SubmitField('提交')


class PostForm(FlaskForm):
    title = StringField("标题", validators=[DataRequired()])
    body = TextAreaField("正文",validators=[DataRequired()])
    description = StringField("描述", validators=[DataRequired()])
    img_url = StringField("封面图", validators=[DataRequired()])
    category = RadioField(choices=[('大数据', '大数据'), ('Python', 'Python'), ('数据结构', '数据结构'), ('读书分享', '读书分享')], validators=[DataRequired()])
    submit = SubmitField('Submit')
