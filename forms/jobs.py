from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class JobsForm(FlaskForm):
    job = StringField('Заголовок', validators=[DataRequired()])
    work_size = IntegerField("Время работы")
    is_private = BooleanField("Личное")
    is_finished = SubmitField('Готово?')
    submit = SubmitField('Применить')