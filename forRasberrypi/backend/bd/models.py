from typing import Optional
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from sqlalchemy import ForeignKeyConstraint, Integer, PrimaryKeyConstraint, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

import os

databaseConn = os.environ.get("DATABASE_URL", "postgresql://postgres:1@localhost:5432/photo_may")


engine = create_engine(
    databaseConn,
    pool_size=5,
    max_overflow=10,
    echo=True
)

SessionLocal = sessionmaker(
    bind=engine,
    expire_on_commit=False
)


class Base(DeclarativeBase):
    pass





class Users(Base):
    __tablename__ = 'users'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='users_pkey'),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(255))
    about: Mapped[Optional[str]] = mapped_column(Text)

    pictures: Mapped[list['Pictures']] = relationship('Pictures', back_populates='users')


class Pictures(Base):
    __tablename__ = 'pictures'
    __table_args__ = (
        ForeignKeyConstraint(['fk_users'], ['users.id'], name='fk_pictures_users'),
        PrimaryKeyConstraint('id', name='pictures_pkey')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fk_users: Mapped[Optional[int]] = mapped_column(Integer)
    picture_patch: Mapped[Optional[str]] = mapped_column(String(255))

    users: Mapped[Optional['Users']] = relationship('Users', back_populates='pictures')
