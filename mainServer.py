from flask import Flask, request, render_template, redirect, abort
from flask_login import LoginManager, login_user, login_required, logout_user, \
    current_user
from data import db_session
from data.users import User
from data.jobs import Jobs
from data.departments import Department
from forms.login import LoginForm
from forms.register import RegisterForm
from forms.jobs import JobsForm
from forms.departaments import DepartamentsForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/departamentsDisplay', methods=['GET', 'POST'])
@login_required
def display_departaments():
    db_sess = db_session.create_session()
    if current_user.is_authenticated:
        departaments = db_sess.query(Department).all()
    else:
        departaments = []
    return render_template('departamentsDisplay.html', title='Департаменты',
                           departaments=departaments
                           )


@app.route('/departaments', methods=['GET', 'POST'])
@login_required
def add_departaments():
    form = DepartamentsForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        departaments = Department()
        departaments.title = form.title.data
        departaments.chief = form.chief.data
        departaments.members = form.members.data
        departaments.email = form.email.data
        db_sess.add(departaments)
        db_sess.merge(current_user)
        db_sess.commit()
        return redirect('/departamentsDisplay')
    return render_template('departaments.html', title='Добавление департамента',
                           form=form
                           )


@app.route('/departaments/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_departaments(id):
    form = DepartamentsForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        departaments = db_sess.query(DepartamentsForm).filter(
            Department.id == id,
            (Department.user == current_user) |
            (current_user.id == 1)
        ).first()
        if departaments:
            departaments.title = form.title.data
            departaments.chief = form.chief.data
            departaments.members = form.members.data
            departaments.email = form.email.data
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        departaments = db_sess.query(Department).filter(
            Department.id == id,
            (Department.user == current_user) |
            (current_user.id == 1)
        ).first()
        if departaments:
            departaments.title = form.title.data
            departaments.chief = form.chief.data
            departaments.members = form.members.data
            departaments.email = form.email.data
            db_sess.commit()
            return redirect('/departamentsDisplay')
        else:
            abort(404)
    return render_template('departaments.html',
                           title='Редактирование департамента',
                           form=form
                           )


@app.route('/departaments_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def departaments_delete(id):
    db_sess = db_session.create_session()
    departaments = db_sess.query(Department).filter(Department.id == id,
                                                    (
                                                            Department.user == current_user) |
                                                    (current_user.id == 1)
                                                    ).first()
    if departaments:
        db_sess.delete(departaments)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/departamentsDisplay')


@app.route('/jobs', methods=['GET', 'POST'])
@login_required
def add_jobs():
    form = JobsForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        jobs = Jobs()
        jobs.job = form.job.data
        jobs.team_leader = form.team_leader.data
        jobs.collaborators = form.collaborators.data
        jobs.work_size = form.work_size.data
        jobs.is_finished = form.is_finished.data
        db_sess.add(jobs)
        db_sess.merge(current_user)
        db_sess.commit()
        return redirect('/')
    return render_template('jobs.html', title='Добавление работы',
                           form=form
                           )


@app.route('/jobs/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_jobs(id):
    form = JobsForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).filter(Jobs.id == id,
                                          (Jobs.user == current_user) |
                                          (current_user.id == 1)
                                          ).first()
        if jobs:
            jobs.job = form.job.data
            jobs.team_leader = form.team_leader.data
            jobs.collaborators = form.collaborators.data
            jobs.work_size = form.work_size.data
            jobs.is_finished = form.is_finished.data
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).filter(Jobs.id == id,
                                          (Jobs.user == current_user) |
                                          (current_user.id == 1)
                                          ).first()
        if jobs:
            jobs.job = form.job.data
            jobs.team_leader = form.team_leader.data
            jobs.collaborators = form.collaborators.data
            jobs.work_size = form.work_size.data
            jobs.is_finished = form.is_finished.data
            db_sess.commit()
            return redirect('/')
        else:
            abort(404)
    return render_template('jobs.html',
                           title='Редактирование работы',
                           form=form
                           )


@app.route('/jobs_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def jobs_delete(id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).filter(Jobs.id == id,
                                      (Jobs.user == current_user) |
                                      (current_user.id == 1)
                                      ).first()
    if jobs:
        db_sess.delete(jobs)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/')


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
        user = db_sess.query(User).filter(
            User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


def main():
    db_session.global_init("db/blogs.db")
    app.run(debug=True, port=8080, host='127.0.0.1')


@app.route("/")
def index():
    db_sess = db_session.create_session()
    if current_user.is_authenticated:
        jobs = db_sess.query(Jobs).all()
    else:
        jobs = []
    return render_template("index.html", jobs=jobs)


if __name__ == '__main__':
    main()
