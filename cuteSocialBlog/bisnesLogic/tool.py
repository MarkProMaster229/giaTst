from bdforApp.models import SessionLocal
from bdforApp.models import Chat, Image, Message, Users, Forum

class Tools():
    @staticmethod
    def error_password():
        breakPassword = ["123","123456789","qazwsx123", "987654321"]#and more
        return breakPassword

class Registration():
    def __init__(self):
        self.we_have_this_name = False
        self.we_have_this_password = False


    def login_or_password_registration(self, what_read_user_login, what_read_user_password):
        self.we_have_this_name = False
        self.we_have_this_password = False
        full_login = []

        with SessionLocal() as session:
            result = session.query(Users.user_name).all()#вот эта хуета вернет картежи ибо до некий еблан решил что так надо. ПОШЕЛ НАХУЙ СУКА!
            for row in result:
                full_login.append(row[0])#СИДИ ЕБИСЬ СУКА

            for name in full_login:
                if what_read_user_login == name:#жду фронтенд реализации
                    self.we_have_this_name = True
                    break

            for mistake_pass in Tools.error_password():#без создания объекта что бы память не расходовать я не знаю утилитарный класс в питон как делать но по написанию этот работает так же ведь да ?
                if what_read_user_password == mistake_pass:
                    self.we_have_this_password = True
                    break

            if self.we_have_this_name == True:
                print("pls chek name, this name have database")
                return 1
            if self.we_have_this_password == True:
                print("pls chek this password, because your password very simple!")
                return 2
            print(self.we_have_this_name)
            print(self.we_have_this_password)
            #вот с этим условием проблема
            if not self.we_have_this_name and not self.we_have_this_password:
                try:
                    new_user = Users(
                        user_name=what_read_user_login,
                        user_password=what_read_user_password
                    )
                    session.add(new_user)
                    session.commit()

                    print("all work!")
                except Exception as e:
                    print("упала база в моменте регистрации")
class Autorization():
    def __init__(self):
        self.correct_password = False
        self.correct_name = True
    
    def autorization(self, what_read_user_login, what_read_user_password):
        #конкретно по логинам - 
        all_username = []
        all_password = []
        try:
            with SessionLocal() as session:
                result = session.query(Users.user_name).all()#требует рефакторинг
                for name in result:
                    all_username.append(name[0])
        except Exception as e:
            print("я падаю в поменте открытия сессии и чтения юзеров")

        for include_name in all_username:
            if what_read_user_login == include_name:
                print("will done")
                #доступ разрешен
                #логика разрешения доступа
            else:
                correct_name = False
                print("name is not correct")
                return 1
        #конкретно по паролям
        try:
            with SessionLocal() as session:
                result = session.query(Users.user_password).all()
                for iteration in result:
                    all_password.append(iteration[0])
                
                for i in all_password:
                    if i == what_read_user_password:
                        self.correct_password = True
                        break
            if self.correct_password == False:
                    print("как уже ранее было сказано - пароль не найден")
        except Exception as e:
            print("я падаю в момент открытия сессии и чтения паролей")

        print(correct_name)
        print(correct_password)
        #выходит раз два флага так и остались true мы гарантируем что и логин и пароль есть в базе 
        if correct_name and correct_password:
            print("everything good!")
            return 200
        
