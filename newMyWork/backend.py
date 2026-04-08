from myBD.endineBd import SessionLocal, Base
from myBD.models import User, personaos, commentss, likesusers
from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app, origins=['http://localhost:5173'])

@app.route('/spermoglot3000', methods=['POST'])
def receive_data():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No JSON received'}), 400
    print("Получил:", data)
    print("Заголовки запроса:", dict(request.headers))
    print("Получил от React:", data)
    print("Имя:", data.get('name'))
    print("Возраст:", data.get('age'))
    #вот так лучше не делать, тут лучше вызвать отдельную функцию 
    with SessionLocal() as session:
        new_user = User(name= data.get('name'), log = data.get('age'))
        session.add(new_user)
        session.commit()
        print("yes")
    return jsonify({'status': 'ok'})

@app.route('/Mydildo/pay', methods=['GET', 'POST'])
def pay_handler():
    # кинуть на фронтенд
    result = {
        'status': 'success',
        'message': 'Платеж прошел успешно',
        'amount': 100
    }
    return jsonify(result)
if __name__ == '__main__':
    app.run(port=5000)




#create table likesUsers(
#id serial primary key,
#UsersId integer,
#personaId integer
#)
#select *
#from likesUsers

#alter table likesUsers
#add constraint fk_like_users
#foreign key (UsersId) references Users(id);

#alter table likesUsers
#add constraint fk_like_person
#foreign key (personaId) references personos(id);


#select *
#from users 