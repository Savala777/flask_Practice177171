from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def route():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotion():
    lines = ['Человечество вырастает из детства.',
             'Человечеству мала одна планета.',
             'Мы сделаем обитаемыми безжизненные пока планеты.',
             'И начнем с Марса!',
             'Присоединяйся!']
    return '<br>'.join(lines)


@app.route('/image_mars')
def image_mars():
    line2 = f'''<div><img src="{url_for('static', filename='img/MARS2.png')}"
            width="200" height="200"
           alt="здесь должна была быть картинка, но не нашлась"></div>\n'''
    line3 = '<div> Вот она какая, красная планета.</div>'
    line = f'''<!doctype html>
              <html lang="en">
              <head>
              <meta charset="utf8">
              <title> Привет, Марс!</title>
              <body>
                <h1>Жди нас, Марс!</h1>
              {line2} 
              {line3} 
              </body>
              '''
    return line


@app.route('/promotion_image')
def promotion_image():
    pass


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
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
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1 class="intro">Анкета претендента</h1>
                            <h1 class="intro">на участие в миссии</h1>
                            <div>
                                <form class="login_form" method="post">
                                    <div class="nameInput">
                                    <input type="text" class="form-control" id="se-name-input" 
                                    placeholder="Введите фамилию" name="se_name">
                                    <input type="text" class="form-control" id="name-input" 
                                    placeholder="Введите имя" name="name">
                                    </div>
                                    <input type="email" class="form-control" id="email-input"
                                    placeholder="Введите адрес почты" name="email">
                                    <div class="block">
                                        <label for="educationSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="educationSelect" name="education">
                                          <option>Начальное</option>
                                          <option>Основное общее</option>
                                          <option>Среднее общее</option>
                                          <option>Среднее профессиональное</option>
                                          <option>Высшее</option>
                                          <option>Без образования</option>
                                        </select>
                                     </div>
                                    <div class="block">
                                    <div>Какие у вас есть профессии?</div>
                                    <div><input type="checkbox" class="professionSelect" name="exp_engi">
                                    Инженер исследователь</div>
                                    <div><input type="checkbox" class="professionSelect" name="pilot">
                                    Пилот</div>
                                    <div><input type="checkbox" class="professionSelect" name="builder">
                                    Строитель</div>
                                    <div><input type="checkbox" class="professionSelect" name="exobio">
                                    Экзобиолог</div>
                                    <div><input type="checkbox" class="professionSelect" name="doctor">
                                    Врач</div>
                                    <div><input type="checkbox" class="professionSelect" name="terra_engi">
                                    Инженер по терраформированию</div>
                                    <div><input type="checkbox" class="professionSelect" name="climate">
                                    Климатолог</div>
                                    <div><input type="checkbox" class="professionSelect" name="radiation">
                                    Специалист по радиационной защите</div>
                                    <div><input type="checkbox" class="professionSelect" name="astrogeolog">
                                    Астрогеолог</div>
                                    <div><input type="checkbox" class="professionSelect" name="glaciolog">
                                    Гляциолог</div>
                                    <div><input type="checkbox" class="professionSelect" name="life_engi">
                                    инженер жизнеобеспечения</div>
                                    <div><input type="checkbox" class="professionSelect" name="meteorolog">
                                    Метеоролог</div>
                                    <div><input type="checkbox" class="professionSelect" name="operator">
                                    Оператор марсохода</div>
                                    <div><input type="checkbox" class="professionSelect" name="cyber_engi">
                                    Киберинженер</div>
                                    <div><input type="checkbox" class="professionSelect" name="shturman">
                                    Штурман</div>
                                    <div><input type="checkbox" class="professionSelect" name="drone_pilot">
                                    Пилот дронов</div>
                                    </div>
                                    <div class="block">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" 
                                          value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" 
                                          value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="block">
                                        <label for="about">Почему вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="block">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    
                                    <div class="block">
                                        <input type="checkbox" class="form-check-input" id="acceptMission" 
                                        name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы 
                                        остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
