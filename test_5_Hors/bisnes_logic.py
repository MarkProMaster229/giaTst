from database.model import SessionLocal, Base
from database.model import Categories, Customers, Orders, Products, OrderItems, Payments
from sqlalchemy import select
from sqlalchemy.orm import joinedload

#утилитарный класс вне!
class Util:
    def __init__(self):
        self.flag = True



#получение списка товаров с возможностью фильтрации по категориям
class Product():
    def __init__(self):#под объекты
        self.correct_work = True#флаг был создан с целью того что он может пригодится в отладке
    

    def get_categor(self, get, categories):# если 1 то вывести все. если 2 то фильтрация по категории
        # в свою очередь categories отвечает за категорию их пока 5
        print("вывести все")
        if get == 1:
            try:
                with SessionLocal()as session:
                    query = select(Products.name)
                    result = session.execute(query)
                    name = result.scalars().all()#тута массив со всем 
                    for i in range(len(name)):
                        print(name[i])

                    #for product in name:
                    #    print(product)
                print(name)
            except Exception as e:
                print("не удалось подключится к базе данных и вывести все")
        else:
            try:
                with SessionLocal() as session:
                    #строго по категорям сортировка!
                    query = (
                        #где id категориии равен конкретному числу where(Categories.id == categories)
                        select(Products.name).join(Categories).where(Categories.id == categories)
                    )
                    result = session.execute(query)
                    # тут все по категорям что выбрал юзер
                    name = result.scalars().all()
                    for i in range(len(name)):
                        print(name[i])

                    print(name)
                

            except Exception as e:
                    print(f"не удалось подключится к базе данных и вывести по категориям {e}")
#получение заказов клиента 
#мне прям ооочень тяжело с базой работать и запросы писать вот это вообще мое очень слабое место! очень опасно 2 часа потрачено на запросы!!!! 
class Order():
    def order_client(self):
        try:
            with SessionLocal() as session:
                query = (
                    select(Customers.name).join(Orders, Customers.id == Orders.customer_id)
                )
                result = session.execute(query)
                name = result.scalars().all()
            for i in range(len(name)):
                print(name[i])


        except Exception as e:
            print(f"не удалось подключится к базе данных и получить заказы клиентов{e}")



obj_test_product = Product()
obj_test_product.get_categor(2,3)

obj_test_Order = Order()
obj_test_Order.order_client()