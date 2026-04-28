from myBd.engine import SessionLocal, Base
from myBd.fastmodel import Fine, Users, Event, Firsona, EventUsers
from sqlalchemy import select
class GetInfo:
    def full_info(self):
        print("вся информация по посетителям")

        #users
        with SessionLocal() as session:
            result = session.execute(select(Users))
            users = result.scalars().all()
            for users in users:
                print(users.name)
        #event
        with SessionLocal() as session:
            result = session.execute(select(Event))
            event = result.scalars().all()
            for event1 in event:
                print(event1.about_event)
        #Firsona
        with SessionLocal() as session:
            result = session.execute(select(Firsona))
            firsona = result.scalars().all()
            for firsona1 in firsona:
                print(firsona1.about_me)
        #Fine
        with SessionLocal() as session:
            result = session.execute(select(Fine))
            fine = result.scalars().all()
            for fine1 in fine:
                print(fine1.about_fine)
        #EventUsers
        with SessionLocal() as session:
            result = session.execute(select(EventUsers))
            eventUsers = result.scalars().all()
            for eventUsers1 in eventUsers:
                print(eventUsers1.about)
        

        
g = GetInfo()
g.full_info()