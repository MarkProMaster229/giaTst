from flask import Flask, jsonify, render_template, request, redirect, url_for, session, flash
from flask_cors import CORS
from bisnesLogic.tool import Registration, Autorization

app = Flask(__name__)
CORS(app, origins=['http://localhost:5173'])
#первый роут регистрационный
@app.route('/dataRegORAutoriz',methods = ['POST'])
def registration():
    data = request.get_json()
    if not data:
            return jsonify({"doneRegOrAutoreg": False, "error": "Данные не пришли"}), 400
    user = data.get('login')
    password = data.get('password')
    mode = data.get('regORautoriz')
    #а нахуя мне два класса 
    registrationOBJ = Registration()
    autorizationOBJ = Autorization()
    #если false как я говорил - регистрация
    if mode is False or mode == "false":
        try:
            registrationOBJ.login_or_password_registration(user,password)
            return jsonify({
                "doneRegOrAutoreg": True
            })
        except Exception as e:
            print("регистрации пизда")
            return jsonify({
                "doneRegOrAutoreg": False
            })
    #если true то авторизация
    if mode is True or mode == 'true':
        try:
            if autorizationOBJ.autorization(user, password) == 200:
                #ну типо если все успешно надо че то вернуть
                return jsonify({
                    "doneRegOrAutoreg": True
                })
        except Exception as e:
            print("авторизации пизда")
            return jsonify({
                "doneRegOrAutoreg": False
            })

        
    

    


if __name__ == '__main__':
    app.run(debug=True)