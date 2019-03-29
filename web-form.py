from flask import Flask, request
from flask import url_for
from db import DB
import sqlite3

app = Flask(__name__)

 
@app.route('/')
@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'POST':
        #nm = DB(db.get_connection())
        #nm.insert(username, info, about, whatelse, sphere)
        return "Oтправленo. С Вами свяжутся в ближайшее время!"
    elif request.method == 'GET':
        return '''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport"
                            content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
                            integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm"
                            crossorigin="anonymous">
                            <title>Активист</title>
                          </head>
                          <body>
                            <h1>Анкета активиста</h1>
                            <form method="post">
                                <input type="username" class="form-control" id="username" placeholder="Введите ФИО" name="username">
                                <div class="form-group">
                                    <label for="classSelect">Откуда вы узнали о нашей организации?</label>
                                    <select class="form-control" id="classSelect" name="info">
                                      <option>Интернет</option>
                                      <option>ВКонтакте</option>
                                      <option>Друзья и знакомые</option>
                                      <option>Случайно забрел(-а)</option>
                                    </select>
                                 </div>
                                <div class="form-group">
                                    <label for="about">Расскажите немного о себе</label>
                                    <textarea class="form-control" maxlength="100" id="about" rows="1" name="about"></textarea>
                                </div>
                                <div class="form-group">
                                    <label for="whatelse">Что бы вы хотели реализовать в организации?</label>
                                    <textarea class="form-control" id="whatelse" rows="1" name="whatelse"></textarea>
                                </div>
                                <div class="form-group">
                                    <label for="form-check">Укажите желаемую сферу деятельности</label>
                                    <div class="form-check">
                                      <input class="form-check-input" type="radio" name="sphere" id="internet" value="internet" checked>
                                      <label class="form-check-label" for="internet">
                                        Интернет-сфера
                                      </label>
                                    </div>
                                    <div class="form-check">
                                      <input class="form-check-input" type="radio" name="sphere" id="volonteer" value="volonteer">
                                      <label class="form-check-label" for="volonteer">
                                        Активное волонтерство
                                      </label>
                                    </div>
                                    <div class="form-check">
                                      <input class="form-check-input" type="radio" name="sphere" id="organise" value="organise" checked>
                                      <label class="form-check-label" for="organise">
                                        Организация мероприятий
                                      </label>
                                    </div>
                                    <div class="form-check">
                                      <input class="form-check-input" type="radio" name="sphere" id="donate" value="donate" checked>
                                      <label class="form-check-label" for="onate">
                                        Благотворительность
                                      </label>
                                    </div>
                                </div>
                                <button type="submit" class="btn btn-primary">Отправить!</button>
                            </form>
                          </body>
                        </html>'''
    

    
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
    
