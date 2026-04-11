from backend import Manager
from my_bd_connect.engine import SessionLocal, Base
from my_bd_connect.my_models import Users, Order_my, Full_products
from myMenu import MyMenu
from changeClient import changeClient


createSelf = Manager()
createSelf.mainManager() 