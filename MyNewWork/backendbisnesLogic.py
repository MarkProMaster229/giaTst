from myBd.engine import SessionLocal, Base
from myBd.fastmodel import Fine, Users, Event, Firsona, EventUsers
from sqlalchemy import select
class GetInfo:
    @staticmethod
    def full_info():
        print("вся информация по посетителям")

        #users
        with SessionLocal() as session:
            result = session.execute(select(Users))
            users_full = result.scalars().all()
            user_mass = []
            for users in users_full:
                user_mass.append(users.name)
                print(users.name)
        #event
        with SessionLocal() as session:
            result = session.execute(select(Event))
            event_full = result.scalars().all()
            event_mass = []
            for event in event_full:
                event_mass.append(event.about_event)
        #Firsona
        with SessionLocal() as session:
            result = session.execute(select(Firsona))
            fursona_full = result.scalars().all()
            fursona_mass = []
            for fursona in fursona_full:
                fursona_mass.append(fursona.about_me)

        #Fine
        with SessionLocal() as session:
            result = session.execute(select(Fine))
            fine_full = result.scalars().all()
            fine_mass = []
            for fine in fine_full:
                fine_mass.append(fine.about_fine)
        #EventUsers
        with SessionLocal() as session:
            result = session.execute(select(EventUsers))
            eventUsers_full = result.scalars().all()
            event_user_mass = []
            for even_user in eventUsers_full:
                event_user_mass.append(even_user.id)
        
        
        return {
            "users" : user_mass,
            "event" : event_mass,
            "fursona" : fursona_mass,
            "fine" : fine_mass,
            "event_user" : event_user_mass
        }
        

        