from myBd.engine import SessionLocal, Base
from myBd.fastmodel import Fine, Users, Event, Firsona, EventUsers
from sqlalchemy import select
class GetInfo:
    def full_info(self):
        print("вся информация по посетителям")
        with SessionLocal() as session:
            result = session.execute(select(Users))
            user = result.scalars().all()
            for user in users:
                print(users.name)


g = GetInfo()
g.full_info()