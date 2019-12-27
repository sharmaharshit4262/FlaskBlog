from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class NewPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=3, max=150)])
    content = TextAreaField('Content', validators=[DataRequired(), Length(max=1500)])
    submit = SubmitField('Post')
