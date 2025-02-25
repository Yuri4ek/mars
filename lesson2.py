from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return "Миссия Колонизация Марса"


@app.route('/')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html',
                           title=title)


@app.route('/')
@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html',
                           title=prof)


@app.route('/')
@app.route('/list_prof/<key>')
def list_prof(key):
    list_prof = ['цветоед', 'инженер', 'строитель', 'врач', 'магистр']
    return render_template('list_prof.html',
                           title=key, list_prof=list_prof)


@app.route('/')
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


if __name__ == '__main__':
    app.run(debug=True, port=8080, host='127.0.0.1')
