from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import DataRequired


class NewChatForm(FlaskForm):
    question = TextAreaField('What can I help with?', render_kw={"placeholder": "Message ChatBot"}, validators=[DataRequired()])
    submit = SubmitField('Send')


class MessageForm(FlaskForm):
    text = TextAreaField('Text', render_kw={"placeholder": "Message ChatBot"}, validators=[DataRequired()])
    submit = SubmitField('Send')
