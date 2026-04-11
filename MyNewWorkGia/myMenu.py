from my_bd_connect.engine import SessionLocal, Base
from my_bd_connect.my_models import Users, Order_my, Full_products


class MyMenu:
    def show_clients(self):
        print("все клиенты")
        with SessionLocal() as session:
            result = session.query(
                Users.id, Users.type_ul_ip, Users.user_name,
                Users.inn, Users.kpp, Users.ogrn,
                Users.ur_adress, Users.contact
            ).all()
            print(f"{'ID':<4} | {'Тип':<20} | {'Имя':<15} | {'ИНН':<12} | {'КПП':<10} | {'ОГРН':<13}")
            print("-" * 115)
            for user in result:
                u_type = 'Юридическое лицо' if user.type_ul_ip else 'ИП'

                u_name = (user.user_name or "-")[:15]
                u_inn = str(user.inn or "-")
                inn_str = str(user.inn or "")
                
                if len(inn_str) not in [10, 12]:
                    u_inn = "error"
                else:
                    u_inn = inn_str

                u_kpp = str(user.kpp or "-")
                u_ogrn = str(user.ogrn or "-")
                u_cont = user.contact or "-"
                u_adr = user.ur_adress or "-"
                print(f"{user.id:<4} | {u_type:<20} | {u_name:<15} | {u_inn:<12} | {u_kpp:<10} | {u_ogrn:<13}")
