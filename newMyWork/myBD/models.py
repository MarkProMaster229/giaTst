from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from myBD.endineBd import Base
from datetime import datetime
from sqlalchemy import Integer, DateTime

class Users(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)  
    nickname:Mapped[str] = mapped_column(String(50))
    about: Mapped[str] = mapped_column(String(255))

class forumMessage(Base):
    __tablename__ = "forummessage"
    message: Mapped[str] = mapped_column(String(485))
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    massadedata: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow
    )
    fk_users: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))