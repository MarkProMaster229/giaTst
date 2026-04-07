from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from myBD.endineBd import Base


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    log: Mapped[str] = mapped_column(String(100))

class personaos(Base):
    __tablename__ = "personaos"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    aboutperson: Mapped[str] = mapped_column(String(255))
    userid: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))#this foreign key

class commentss(Base):
    __tablename__ = "commentss"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    userid: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))#this foreign key
    textcomment: Mapped[str] = mapped_column(String(255))

class likesusers(Base):
    __tablename__ = "likesusers"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    userid: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))#this foreign key
    personaid: Mapped[int] = mapped_column(Integer,ForeignKey("personas.id"))#this foreign key
