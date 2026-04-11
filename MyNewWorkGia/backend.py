from my_bd_connect.engine import SessionLocal, Base
from my_bd_connect.my_models import Users, Order_my, Full_products
from myMenu import MyMenu
from changeClient import changeClient

class Manager():
    def mainManager(self):
        createMenu = MyMenu()
        changeUserController = changeClient()
        createMenu.show_clients()
        name = input("delete users? 1-yes 2-no ")
        if name == "1":
            changeUserController.delete()
        name = input("create User? 1-yes 2-no ")
        if name == "1":
            changeUserController.create()
        name = input("createOrder? 1-yes 2-no ")
        if name == "1":
            new_id = changeUserController.create_order() 
        name = input("check order total? 1-yes 2-no ")
        if name == "1":
            id_for_total = input("give me order ID: ")
            changeUserController.show_order_total(id_for_total)