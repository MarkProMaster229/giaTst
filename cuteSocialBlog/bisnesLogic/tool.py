from bdforApp.models import SessionLocal
from bdforApp.models import Chat, Image, Message, Users, Forum

class Registration():
    def __init__(self):
        we_have_this_name = False
        we_have_this_password = False

    
    class Tools():
        @staticmethod
        def error_password(self):
            breakPassword = ["123","123456789","qazwsx123", "987654321"]#and more
            return breakPassword
        @staticmethod
        def help_fun_for_make_mistakes(self):
            print("probably I fix you!")


    def login_or_password(self, login, password):
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

        if we_have_this_name and we_have_this_password == True:
            new_user = (
                what_read_user_login,
                what_read_user_password
            )
            session.add(new_user)
            session.commit()

        print("all work!")



