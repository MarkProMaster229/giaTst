from my_bd_connect.engine import SessionLocal, Base
from my_bd_connect.my_models import Users, Order_my, Full_products


class changeClient():

    def delete(self):
        client_id = input("give me ID for user")
        
        with SessionLocal() as session:
            client = session.query(Users).filter(Users.id == client_id).first()
            session.delete(client)
            session.commit()
            print("delete")


    def create(self):
        print("\nCREATE USER!")
        u_type_input = input("ul or ip? 1-ul, 0-ip: ")
        u_type = True if u_type_input == '1' else False
        
        name = input("name: ")
        
        def to_int(val):
            return int(val) if val and val.strip().isdigit() else None

        inn_val = to_int(input("inn: "))
        kpp_val = to_int(input("kpp: "))
        ogrn_val = to_int(input("ogrn: "))
        
        addr = input("adress: ")
        cont = input("contact: ")

        with SessionLocal() as session:
            new_user = Users(
                type_ul_ip=u_type,
                user_name=name,
                inn=inn_val,
                kpp=kpp_val,
                ogrn=ogrn_val,
                ur_adress=addr,
                contact=cont
            )
            
            try:
                session.add(new_user)
                session.commit()
                session.refresh(new_user)
                print(f"user done! ID: {new_user.id}")
            except Exception as e:
                session.rollback()
                print(f"error! {e}")

    def create_order(self):
        print("\nCREATE ORDER!")
        client_id = input("give me ID for user, for make order")
        
        delivery_days = input("days: ")
        status = "create"

    def create_order(self):
        print("\nCREATE ORDER!")
        client_id = input("give me ID for user, for make order: ") # Не забудь : для красоты
        
        delivery_days = input("days: ")
        status = "create"

        with SessionLocal() as session:
            # 1. Сначала создаем заказ
            new_order = Order_my(
                data_delivery=int(delivery_days) if delivery_days.isdigit() else 0,
                stat=status,
                fk_users=int(client_id)
            )
            
            session.add(new_order)
            session.flush()
            
            print(f"order draft created. Now add products.")

            while True:
                add_prod = input("add product to this order? 1-yes, 0-no: ")
                if add_prod != "1":
                    break
                    
                prod_name = input("name product: ")
                prod_price = input("price product: ")
                    
                new_product = Full_products(
                    product=prod_name,
                    price=int(prod_price) if prod_price.isdigit() else 0,
                    fk_users=new_order.id
                )
                session.add(new_product)
                print("product added to list...")

            session.commit()
            print(f"DONE! Order №{new_order.id} with all products saved.")

    def show_order_total(self, order_id):
        with SessionLocal() as session:
            products = session.query(Full_products).filter(Full_products.fk_users == order_id).all()
            
            total_sum = 0
            print(f"\nORDER №{order_id} DETAILS:")
            print("-" * 30)
            delivery = 0
            for item in products:
                print(f"{item.product:<15} | Price: {item.price}")
                total_sum += item.price
            if total_sum < 50000:
                delivery = 1000
            elif total_sum >= 50000:
                delivery = total_sum * 0.05
            print(f"TOTAL SUM: {total_sum} delivery - {delivery}")
            print("discounts")
            if total_sum > 100000:
                print(f"your discount - {total_sum * 0.05}")
            elif total_sum > 500000:
                print(f"your discount - {total_sum * 0.10}")