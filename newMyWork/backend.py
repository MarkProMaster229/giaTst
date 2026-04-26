from myBD.endineBd import SessionLocal, Base
from myBD.models import Users, forumMessage
from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app, origins=['http://localhost:5173'])
#npm create vite@latest frontend --template react
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

@app.route('/NickName',methods=['POST'])
def Myrequest():
    data = request.get_json()
    print(f"input {data}")
    print("Имя:", data.get('nickname'))
    with SessionLocal() as session:
        newNickname = Users(nickname = data.get('nickname'))
        session.add(newNickname)
        session.commit()
    return jsonify({'status': 'ok'})

@app.route('/message', methods=['POST'])
def MyMessage():
    data = request.get_json()
    print(data.get("messageJso"))
    print("Имя:", data.get('nameUsers'))
    if data.get('nameUsers') == None:
        return jsonify({'status': 'NoNickname'}) 
    with SessionLocal() as session:
        nickname = data.get('nameUsers')
        users = session.query(Users).filter(Users.nickname == nickname).first()
        if not users:
            users = Users(nickname = data.get('nameUsers'))
            session.add(users)
            session.flush()#id
        newMessage = forumMessage(message = data.get('messageJso'),fk_users = users.id)
        users = Users(nickname=data.get('nameUsers'), about="")
        session.add(newMessage)
        session.commit()
    return jsonify({'status': 'ok'})

@app.route('/returnMessage',methods = ['GET'])
def returnRes():
    with SessionLocal() as session:
        results = session.query(
            forumMessage.id,
            forumMessage.message,
            forumMessage.massadedata,
            Users.nickname
            ).join(Users, forumMessage.fk_users == Users.id).order_by(forumMessage.massadedata.desc()).all()
        result = [
            {
                'id': row.id,
                'message': row.message,
                'date': row.massadedata.strftime("%Y-%m-%d %H:%M:%S") if row.massadedata else None,
                'nickname': row.nickname
                }
                for row in results
                ]
    return jsonify(result)

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000, debug=True)




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