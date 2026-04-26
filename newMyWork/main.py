from myBD.endineBd import SessionLocal, Base
from myBD.models import User, personaos, commentss, likesusers


with SessionLocal() as session:
    user = User(name="admin",log="admin")
    session.add(user)
    session.commit()
    print("this worked!")