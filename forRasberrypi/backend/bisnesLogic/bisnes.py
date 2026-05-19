from bd.models import Users, Pictures
from bd.models import SessionLocal, Base
from sqlalchemy import select
from sqlalchemy.orm import joinedload

from minio import Minio
import os
import io 

class minioConn():
    def __init__(self):
        self.testConnect = False
    def connect(self, imageFileName_f,imagesBite,):
        client = Minio(
            "localhost:9000",
            access_key="rootadmin",
            secret_key="supersecretpassword123",
            secure=False
        )
        raw_bytes = imagesBite.read()
        length = len(raw_bytes)

        self.testConnect = True
        bucket = "photos"
        if not client.bucket_exists(bucket):
            client.make_bucket(bucket)
        try: 
            client.put_object(
                bucket_name=bucket,
                object_name=imageFileName_f,
                data=io.BytesIO(raw_bytes),
                length=length,
                content_type=imagesBite.content_type
            )
        except Exception as e:
            print(f"error 2, check connect in minio -    {e}")


class Analization():
    def __init__(self):
        self.initializationTest = False
    
    def initialization(self, user_f,about_f,imageFileName_f):
        with SessionLocal() as session:
            user_name = Users(name=user_f, about=about_f)
            
            session.add_all([user_name])
            session.flush()
            imageFileName = Pictures(picture_patch=imageFileName_f, fk_users=user_name.id)
            session.add_all([imageFileName])
            session.commit()
            self.initializationTest = True
        
    
    def workForSave(self, imagesBite, imageFileName_f):
        if self.initializationTest == False:
            print("error 1, dont have initialization")
            return 1
        
        minioConnect = minioConn()
        minioConnect.connect(imageFileName_f, imagesBite)

class Return_data():
    def __init__(self):
        self.work_OR_not = False
    @staticmethod
    def retData():
        with SessionLocal() as session:
            query = select(Users).options(joinedload(Users.pictures)) 
            result = session.execute(query)
            users = result.scalars().unique().all()
        bucket = "photos"

        users_list = []
        for user in users:
            users_list.append({
            "id": user.id,
            "name": user.name,
            "about": user.about,
            "images": [pic.picture_patch for pic in user.pictures]
        })
        #print(users_list) 
        
        client = Minio(
            "localhost:9000",
            access_key="rootadmin",
            secret_key="supersecretpassword123",
            secure=False
            )
        full_data = []
        for user in users_list:
            print(user['name'])
            for filename in user['images']:
                patch = f"{bucket}_{filename}"
                print(patch)
                response = client.get_object(bucket, filename)
                file_bytes = response.read()
                full_data.append({
                    'username': user['name'],
                    'file': file_bytes,
                    'about': user['about']
                })
        
        print(full_data[0]['about'])



#create table users(
#id serial primary key,
#name varchar(255),
#about text
#)

#create table pictures(
#id serial primary key,
#fk_users integer,
#picture_patch varchar(255)
#)

#alter table pictures
#add constraint fk_pictures_users
#foreign key(fk_users) references users(id);

#drop table users 
#drop table pictures


#select*
#from users 

#select*
#from pictures
