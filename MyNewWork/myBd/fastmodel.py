from typing import Optional
import datetime
#sqlacodegen postgresql://postgres:1@localhost:5432/my_test_bd_for_me > fastmodel.py
from sqlalchemy import Boolean, DateTime, ForeignKeyConstraint, Integer, PrimaryKeyConstraint, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from myBd.engine import Base

class Fine(Base):
    __tablename__ = 'fine'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='fine_pkey'),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    about_fine: Mapped[Optional[str]] = mapped_column(String(255))
    fk_users: Mapped[Optional[int]] = mapped_column(Integer)


class Users(Base):
    __tablename__ = 'users'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='users_pkey'),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(255))
    volunteer: Mapped[Optional[bool]] = mapped_column(Boolean)

    event: Mapped[list['Event']] = relationship('Event', back_populates='users')
    firsona: Mapped[list['Firsona']] = relationship('Firsona', back_populates='users')
    event_users: Mapped[list['EventUsers']] = relationship('EventUsers', back_populates='users')


class Event(Base):
    __tablename__ = 'event'
    __table_args__ = (
        ForeignKeyConstraint(['fk_leading'], ['users.id'], name='fk_event'),
        PrimaryKeyConstraint('id', name='event_pkey')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fk_leading: Mapped[int] = mapped_column(Integer, nullable=False)
    about_event: Mapped[Optional[str]] = mapped_column(String(255))
    time: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)

    users: Mapped['Users'] = relationship('Users', back_populates='event')
    event_users: Mapped[list['EventUsers']] = relationship('EventUsers', back_populates='event')


class Firsona(Base):
    __tablename__ = 'firsona'
    __table_args__ = (
        ForeignKeyConstraint(['fk_users'], ['users.id'], name='fk_firsona'),
        PrimaryKeyConstraint('id', name='firsona_pkey')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    about_me: Mapped[Optional[str]] = mapped_column(String(255))
    fk_users: Mapped[Optional[int]] = mapped_column(Integer)

    users: Mapped[Optional['Users']] = relationship('Users', back_populates='firsona')


class EventUsers(Base):
    __tablename__ = 'event_users'
    __table_args__ = (
        ForeignKeyConstraint(['fk_event'], ['event.id'], name='user_event_event'),
        ForeignKeyConstraint(['fk_user'], ['users.id'], name='user_event_users'),
        PrimaryKeyConstraint('id', name='event_users_pkey')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fk_user: Mapped[Optional[int]] = mapped_column(Integer)
    fk_event: Mapped[Optional[int]] = mapped_column(Integer)
    about: Mapped[Optional[str]] = mapped_column(String)

    event: Mapped[Optional['Event']] = relationship('Event', back_populates='event_users')
    users: Mapped[Optional['Users']] = relationship('Users', back_populates='event_users')
