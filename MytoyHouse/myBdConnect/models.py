from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from myBdConnect.endine import Base
from datetime import datetime
from sqlalchemy import Integer, DateTime

class Users(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer,primary_key=True)
    name: Mapped[str] = mapped_column(String(255))

class Original_os(Base):
    __tablename__ = "original_os"
    id: Mapped[int] = mapped_column(Integer,primary_key=True)
    about: Mapped[str] = mapped_column(String(255))
    fk_users: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"))

class Comment(Base):
    __tablename__ = "comments"
    id: Mapped[int] = mapped_column(Integer,primary_key=True)
    comments: Mapped[str] = mapped_column(String(255))
    fk_users: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"))

class Likes(Base):
    __tablename__ = "likes"
    id: Mapped[int] = mapped_column(Integer,primary_key=True)
    fk_original_character: Mapped[int] = mapped_column(Integer, ForeignKey("original_os.id"))
    fk_users: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"))

