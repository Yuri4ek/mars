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


if __name__ == '__main__':
    app.run(debug=True, port=8080, host='127.0.0.1')
