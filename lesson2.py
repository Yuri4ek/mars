from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return "Миссия Колонизация Марса"


@app.route('/')
@app.route('/index/<title>')
def index(title):
    user = "Ученик Яндекс.Лицея"
    return render_template('base.html',
                           title=title)


if __name__ == '__main__':
    app.run(debug=True, port=8080, host='127.0.0.1')
