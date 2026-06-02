from typing import Optional
import datetime

from sqlalchemy import Boolean, DateTime, ForeignKeyConstraint, Integer, PrimaryKeyConstraint, String, Text, text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

databaseConn = os.environ.get("DATABASE_URL", "postgresql://postgres:1@localhost:5432/full_social")

engine = create_engine(
    databaseConn,
    pool_size = 5,
    max_overflow = 10,
    echo = True
)

SessionLocal = sessionmaker(
    bind=engine,
    expire_on_commit=False
)



class Base(DeclarativeBase):
    pass


class Chat(Base):
    __tablename__ = 'chat'
    __table_args__ = (
        ForeignKeyConstraint(['fk_image'], ['image.id'], name='fk_image'),
        ForeignKeyConstraint(['fk_user_1'], ['users.id'], name='fk_user_1'),
        ForeignKeyConstraint(['fk_user_2'], ['users.id'], name='fk_user_2'),
        PrimaryKeyConstraint('id', name='chat_pkey')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fk_user_1: Mapped[int] = mapped_column(Integer, nullable=False)
    fk_user_2: Mapped[int] = mapped_column(Integer, nullable=False)
    id_for_chat64: Mapped[Optional[str]] = mapped_column(Text)
    fk_image: Mapped[Optional[int]] = mapped_column(Integer)

    image: Mapped[Optional['Image']] = relationship('Image', foreign_keys=[fk_image], back_populates='chat_fk_image')
    users: Mapped['Users'] = relationship('Users', foreign_keys=[fk_user_1], back_populates='chat_fk_user_1')
    users_: Mapped['Users'] = relationship('Users', foreign_keys=[fk_user_2], back_populates='chat_fk_user_2')
    image_fk_chat: Mapped[list['Image']] = relationship('Image', foreign_keys='[Image.fk_chat]', back_populates='chat')


class Image(Base):
    __tablename__ = 'image'
    __table_args__ = (
        ForeignKeyConstraint(['fk_chat'], ['chat.id'], name='fk_chat'),
        PrimaryKeyConstraint('id', name='image_pkey')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fk_chat: Mapped[Optional[int]] = mapped_column(Integer)
    about: Mapped[Optional[str]] = mapped_column(Text)
    link_for_minio: Mapped[Optional[str]] = mapped_column(Text)

    chat_fk_image: Mapped[list['Chat']] = relationship('Chat', foreign_keys='[Chat.fk_image]', back_populates='image')
    chat: Mapped[Optional['Chat']] = relationship('Chat', foreign_keys=[fk_chat], back_populates='image_fk_chat')


class Message(Base):
    __tablename__ = 'message'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='message_pkey'),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    data: Mapped[datetime.datetime] = mapped_column(DateTime(True), nullable=False, server_default=text('now()'))
    flag: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=text('false'))
    message: Mapped[Optional[str]] = mapped_column(Text)
    fk_chat: Mapped[Optional[int]] = mapped_column(Integer)

    forum: Mapped[list['Forum']] = relationship('Forum', back_populates='message')


class Users(Base):
    __tablename__ = 'users'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='users_pkey'),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    data: Mapped[datetime.datetime] = mapped_column(DateTime(True), nullable=False, server_default=text('now()'))
    user_name: Mapped[Optional[str]] = mapped_column(String(255))
    id_generate_base36_4: Mapped[Optional[str]] = mapped_column(String(4))
    user_password: Mapped[Optional[str]] = mapped_column(String(255))
    user_about: Mapped[Optional[str]] = mapped_column(String(255))

    chat_fk_user_1: Mapped[list['Chat']] = relationship('Chat', foreign_keys='[Chat.fk_user_1]', back_populates='users')
    chat_fk_user_2: Mapped[list['Chat']] = relationship('Chat', foreign_keys='[Chat.fk_user_2]', back_populates='users_')
    forum: Mapped[list['Forum']] = relationship('Forum', back_populates='users')


class Forum(Base):
    __tablename__ = 'forum'
    __table_args__ = (
        ForeignKeyConstraint(['fk_message'], ['message.id'], name='fk_message'),
        ForeignKeyConstraint(['fk_only_user'], ['users.id'], name='fk_only_user'),
        PrimaryKeyConstraint('id', name='forum_pkey')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fk_only_user: Mapped[Optional[int]] = mapped_column(Integer)
    fk_message: Mapped[Optional[int]] = mapped_column(Integer)

    message: Mapped[Optional['Message']] = relationship('Message', back_populates='forum')
    users: Mapped[Optional['Users']] = relationship('Users', back_populates='forum')
