from flask import Flask, request, render_template, redirect
from flask_login import LoginManager, login_user, login_required, logout_user, \
    current_user
from data import db_session
from data.users import User
from data.jobs import Jobs
from forms.login import LoginForm
from forms.register import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            surname=form.surname.data,
            name=form.name.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data,
            email=form.email.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


def main():
    db_session.global_init("db/blogs.db")
    app.run()


@app.route("/")
def index():
    db_sess = db_session.create_session()
    if current_user.is_authenticated:
        jobs = db_sess.query(Jobs).all()
    else:
        jobs = []
    return render_template("index.html", jobs=jobs)


if True:
    @app.route('/distribution')
    def distribution():
        data = ['Mike', 'Юра Борисов', 'Jason Statham', 'Я']
        return render_template('distribution.html',
                               data=data)


    @app.route('/table/<sex>/<year>')
    def room(sex, year):
        year = int(year)
        return render_template('room.html',
                               sex=sex, year=year)


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

if __name__ == '__main__':
    main()
    app.run(debug=True, port=8080, host='127.0.0.1')
