from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from my_bd_connect.engine import Base
from datetime import datetime
from sqlalchemy import Integer, DateTime, BigInteger, Boolean, Text 

class Users(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)  
    type_ul_ip: Mapped[bool] = mapped_column(Boolean, default=False)
    user_name: Mapped[str] = mapped_column(String(255))
    inn: Mapped[int] = mapped_column(BigInteger)
    kpp: Mapped[int] = mapped_column(BigInteger)
    ogrn: Mapped[int] = mapped_column(BigInteger)
    ur_adress: Mapped[str] = mapped_column(Text)
    contact: Mapped[str] = mapped_column(Text)


class Order_my(Base):
    __tablename__ = "order_my"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    data_order: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow
    )
    data_delivery: Mapped[int] = mapped_column(Integer)
    stat: Mapped[str] = mapped_column(String(255))
    fk_users: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))


class Full_products(Base):
    __tablename__ = "full_products"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    product: Mapped[str] = mapped_column(String(255))
    price: Mapped[int] = mapped_column(Integer)
    fk_users: Mapped[int] = mapped_column(Integer, ForeignKey("order_my.id"))
