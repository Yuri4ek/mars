from flask import Flask, url_for, request, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def main():
    return "Миссия Колонизация Марса"


@app.route('/')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html',
                           title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html',
                           title=prof)


@app.route('/list_prof/<key>')
def list_prof(key):
    list_prof = ['цветоед', 'инженер', 'строитель', 'врач', 'магистр']
    return render_template('list_prof.html',
                           title=key, list_prof=list_prof)


@app.route('/answer')
def answer():
    data = {'title': 'Анкета',
            'surname': 'Pedrov',
            'name': 'Mark',
            'education': 'Выше Высокого',
            'profession': 'Врач',
            'sex': 'male',
            'motivation': 'Захотел',
            'ready': 'Всегда'}
    return render_template('auto_answer.html',
                           data=data)


@app.route('/')
@app.route('/auto_answer')
def auto_answer():
    data = {'title': 'Анкета',
            'surname': 'Петров',
            'name': 'Маркс',
            'education': 'Выше среднего',
            'profession': 'Глав Врач',
            'sex': 'male',
            'motivation': 'Захотел и захотел',
            'ready': 'Всегда и никогда'}
    return render_template('auto_answer.html',
                           data=data)


class LoginForm(FlaskForm):
    aid = StringField('id астронавта', validators=[DataRequired()])
    apassword = PasswordField('Пароль астронавта', validators=[DataRequired()])
    kid = StringField('id капитана', validators=[DataRequired()])
    kpassword = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


if __name__ == '__main__':
    app.run(debug=True, port=8080, host='127.0.0.1')
