import psycopg2
from psycopg2 import sql



def createDatabaseIfNotExists(conn,database):
    
    try:   

        cursor = conn.cursor()
        cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(database)))
        conn.commit()
        print(f"База данных '{database}' успешно создана.")

    except Exception as e:
        print(f"Произошла ошибка: {e}")
        conn.rollback() 

class Material_data:
    def __init__(self, host, database, user, password,port):
        try:
            self.connect = psycopg2.connect(host=host, database=database, user=user, password=password,port=port)
        except psycopg2.errors.InvalidCatalogName:
            self.connect = psycopg2.connect(host=host,  user=user, password=password,port=port)
            
    
            createDatabaseIfNotExists(self.connect, database )
            
            self.connect = psycopg2.connect(host=host, database=database, user=user, password=password,port=port)
            
    def get_material_id(self,):
        try:
            with self.connect.cursor() as cur:
                cur.execute("SELECT id_materials FROM materials", (loginname,password))
                result = cur.fetchone()
                if result:
                    return {"user_id": result[0],"Loginname": result[1], "Password": result[2]}
                return None
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            self.connect.rollback() 
            
    def get_name_material(self,id):
        try:
            with self.connect.cursor() as cur:
                cur.execute("SELECT name_material FROM materials where id_materials = %d", (id))
                result = cur.fetchone()
                if result:
                    return {"name_material": result[0]}
                return None
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            self.connect.rollback() 
        
    
    def get_price_material_by_id(self):
        try:
            with self.connect.cursor() as cur:
                cur.execute("SELECT price_material FROM materials where id_materials = %d", (id))
                result = cur.fetchone()
                if result:
                    return {"price_material": result[0]}
                return None
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            self.connect.rollback() 
        pass
        
    def get_kolichestvo_na_sklade(self):
        try:
            with self.connect.cursor() as cur:
                cur.execute("SELECT kolichestvo_sklad FROM materials where id_materials = %d", (id))
                result = cur.fetchone()
                if result:
                    return {"kolichestvo_sklad": result[0]}
                return None
        except Exception as e:
            print(f"Произошла ошибка: {e}")
        pass
    def get_min_kolichestvo(self):
        try:
            with self.connect.cursor() as cur:
                cur.execute("SELECT min_kolichestvo FROM materials where id_materials = %d", (id))
                result = cur.fetchone()
                if result:
                    return {"min_kolichestvo": result[0]}
                return None
        except Exception as e:
            print(f"Произошла ошибка: {e}")
        pass
    def get_kolichestvo_upakovka(self):
        try:
            with self.connect.cursor() as cur:
                cur.execute("SELECT kolichestvo_v_upakovke FROM materials where id_materials = %d", (id))
                result = cur.fetchone()
                if result:
                    return {"kolichestvo_v_upakovke": result[0]}
                return None
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            
        pass
    def get_edinica_izmerenia(self,id):
        try:
            with self.connect.cursor() as cur:
                cur.execute("SELECT edinica_izmerenia FROM materials where id_materials = %s", (id))
                result = cur.fetchone()
                if result:
                    return {"edinica_izmerenia": result}
                return None
        except Exception as e:
            print(f"Произошла ошибка: {e}")
        pass
    def type_material(self):
        try:
            with self.connect.cursor() as cur:
                cur.execute("SELECT name_material FROM materials where id_materials = %d", (id))
                result = cur.fetchone()
                if result:
                    return {"name_material": result[0]}
                return None
        except Exception as e:
            print(f"Произошла ошибка: {e}")
        pass
    
    
class Supplier_data:
    def __init__(self, host, database, user, password,port):
        try:
            self.connect = psycopg2.connect(host=host, database=database, user=user, password=password,port=port)
        except psycopg2.errors.InvalidCatalogName:
            self.connect = psycopg2.connect(host=host,  user=user, password=password,port=port)
            
    
            createDatabaseIfNotExists(self.connect, database )
            
            self.connect = psycopg2.connect(host=host, database=database, user=user, password=password,port=port)
            
    #def getname_supplier
    
    
    #def get_type_supplier
    #def get_inn
    #def rating_suppliers
    #def date_begin_with_suppliers
    
    
    