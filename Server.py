from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def main():
    return "Миссия Колонизация Марса"


@app.route('/')
@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/')
@app.route('/promotion')
def promotion():
    return ("Человечество вырастает из детства.</br>Человечеству мала одна "
            "планета.</br>Мы сделаем обитаемыми безжизненные пока планеты.</br>И "
            "начнем с Марса!</br>Присоединяйся!")


@app.route('/')
@app.route('/promotion_image')
def image():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.png')}">
                    <div class="alert alert-primary" role="alert">
                      Человечеств овырастает из детства
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      Мы - будущее!
                    </div>
                    <div class="alert alert-warning" role="alert">
                      Тут был Юра
                    </div>
                    <div class="alert alert-danger" role="alert">
                      Марс - наше все
                    </div>
                    <div class="alert alert-primary" role="alert">
                      мой номер 8 800 555 35 35
                    </div>
                  </body>
                </html>'''


@app.route('/')
@app.route('/astronaut_selection', methods=['POST', 'GET'])
def select():
    if request.method == 'GET':
        return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                <title>Пример формы</title>
                              </head>
                              <body>
                                <h1>Форма для регистрации в суперсекретной системе</h1>
                                <div>
                                    <form class="login_form" method="post">
                                        <input type="lastname" 
                                        class="form-control" id="lastname"
                                        placeholder="Введите фамилию" 
                                        name="lastname">
                                        
                                        <input type="name" 
                                        class="form-control" id="name" 
                                        placeholder="Введите имя" 
                                        name="name">
                                        
                                        <input type="address" 
                                        class="form-control" id="address" 
                                        placeholder="Введите адрес почты" 
                                        name="address">
                                        
                                        <p>Какое у вас образование?</p>
                                        <div class="form-group">
                                            <label 
                                            for="classSelect">Выберите 
                                            образование</label>
                                            <select class="form-control" id="classSelect" name="class">
                                              <option>Начальное</option>
                                              <option>Среднее</option>
                                              <option>Высшеее</option>
                                            </select>
                                         </div>
                                         
                                        <div class="form-group">
                                            <label 
                                            for="form-check">Какие у вас 
                                            профессии?
                                            </label>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="prof" id="1" value="1">
                                              <label class="form-check-label" for="1">
                                                Программист
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="prof" id="2" value="2">
                                              <label class="form-check-label" for="2">
                                                Архитектор
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="prof" id="3" value="3">
                                              <label class="form-check-label" for="3">
                                                Врач
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="prof" id="3" value="3">
                                              <label class="form-check-label" for="3">
                                                Не врач
                                              </label>
                                            </div>
                                        </div> 
                                        
                                        <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male">
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    
                                    <div class="form-group">
                                            <label for="about">Почему вы 
                                            хотите принять участие в 
                                            эксперименте?
                                            </label>
                                            <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                        </div>
                                        
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                            <label class="form-check-label" 
                                            for="acceptRules">Готовы ли 
                                            вы остаться на марсе?</label>
                                        </div>
                                        <button type="submit" class="btn 
                                        btn-primary">Отправить</button>
                                    </form>
                                </div>
                              </body>
                            </html>'''
    elif request.method == 'POST':
        print(request.form['lastname'])
        print(request.form['name'])
        print(request.form['address'])
        print(request.form['class'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


@app.route('/')
@app.route('/load_photo', methods=['POST', 'GET'])
def load_image():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                             <link rel="stylesheet"
                             href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                             integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                             crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример загрузки файла</title>
                          </head>
                          <body>
                            <h1>Загрузим файл</h1>
                            <form method="post" enctype="multipart/form-data">
                               <div class="form-group">
                                    <label for="photo">Выберите файл</label>
                                    <input type="file" class="form-control-file" id="photo" name="file">
                                </div>
                                <button type="submit" class="btn btn-primary">Отправить</button>
                            </form>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        f = request.files['file']
        with open('static/img/person.png', mode='wb+') as file:
            file.write(f.read())
        return f'''<!doctype html>
                                <html lang="en">
                                  <head>
                                    <meta charset="utf-8">
                                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                     <link rel="stylesheet"
                                     href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                     integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                     crossorigin="anonymous">
                                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                    <title>Пример загрузки файла</title>
                                  </head>
                                  <body>
                                    <h1>Загрузим файл</h1>
                                    <form method="post" enctype="multipart/form-data">
                                       <div class="form-group">
                                            <label for="photo">Выберите файл</label>
                                            <input type="file" class="form-control-file" id="photo" name="file">
                                        </div>
                                        <img src="
{url_for('static', filename='img/person.png')}">
                                    </form>
                                  </body>
                                </html>'''


@app.route('/')
@app.route('/carousel')
def pepe():
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Пейзажи марса!!!!!!!!!</h1>
                        <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
                          <div class="carousel-inner">
                            <div class="carousel-item active">
                              <img src="
{url_for('static', filename='img/pepe1.png')}" class="d-block w-100" alt="...">
                            </div>
                            <div class="carousel-item active">
                              <img src="
{url_for('static', filename='img/pepe2.png')}" class="d-block w-100" alt="...">
                            </div>
                            <div class="carousel-item">
                              <img src="
{url_for('static', filename='img/pepe3.png')}" class="d-block w-100" alt="...">
                            </div>
                          </div>
                        </div>
                      </body>
                    </html>'''


@app.route('/')
@app.route('/choice/<planet_name>')
def planet_image(planet_name):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Мое предложение: {planet_name}</h1>
                    <div class="alert alert-primary" role="alert">
                      Человечеств овырастает из детства
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      Мы - будущее!
                    </div>
                    <div class="alert alert-warning" role="alert">
                      Тут был Юра
                    </div>
                    <div class="alert alert-danger" role="alert">
                      Марс - наше все
                    </div>
                    <div class="alert alert-primary" role="alert">
                      мой номер 8 800 555 35 35
                    </div>
                  </body>
                </html>'''


@app.route('/')
@app.route('/results/<nickname>/<int:level>/<float:rating>')
def selection_person(nickname, level, rating):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Результаты отбора:</h1>
                    <div class="alert alert-primary" role="alert">
                      Претендента на участие в миссии {nickname}:
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      Поздравляем! Ваш рейтинг после {level} этапа отбора
                    </div>
                    <div class="alert alert-warning" role="alert">
                      составляет {rating}!
                    </div>
                    <div class="alert alert-danger" role="alert">
                      Желаем удачи!!!
                    </div>
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(debug=True, port=8080, host='127.0.0.1')
