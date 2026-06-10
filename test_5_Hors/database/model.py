from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
import os

from typing import Optional

from sqlalchemy import ForeignKeyConstraint, Integer, PrimaryKeyConstraint, REAL, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

databaseConn = os.environ.get("DATABASE_URL", "postgresql://postgres:1@localhost:5432/my_shop")

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


class Categories(Base):
    __tablename__ = 'categories'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='categories_pkey'),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(50))

    products: Mapped[list['Products']] = relationship('Products', back_populates='category')


class Customers(Base):
    __tablename__ = 'customers'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='customers_pkey'),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(50))
    email: Mapped[Optional[str]] = mapped_column(String(50))
    city: Mapped[Optional[str]] = mapped_column(String(50))

    orders: Mapped[list['Orders']] = relationship('Orders', back_populates='customer')


class Orders(Base):
    __tablename__ = 'orders'
    __table_args__ = (
        ForeignKeyConstraint(['customer_id'], ['customers.id'], name='fk_orders_customers'),
        PrimaryKeyConstraint('id', name='orders_pkey')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    order_date: Mapped[Optional[str]] = mapped_column(String(50))
    customer_id: Mapped[Optional[int]] = mapped_column(Integer)
    status: Mapped[Optional[str]] = mapped_column(String(50))

    customer: Mapped[Optional['Customers']] = relationship('Customers', back_populates='orders')
    order_items: Mapped[list['OrderItems']] = relationship('OrderItems', back_populates='order')
    payments: Mapped[list['Payments']] = relationship('Payments', back_populates='order')


class Products(Base):
    __tablename__ = 'products'
    __table_args__ = (
        ForeignKeyConstraint(['category_id'], ['categories.id'], name='fk_product_category'),
        PrimaryKeyConstraint('id', name='products_pkey')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(50))
    category_id: Mapped[Optional[int]] = mapped_column(Integer)
    price: Mapped[Optional[float]] = mapped_column(REAL)

    category: Mapped[Optional['Categories']] = relationship('Categories', back_populates='products')
    order_items: Mapped[list['OrderItems']] = relationship('OrderItems', back_populates='product')


class OrderItems(Base):
    __tablename__ = 'order_items'
    __table_args__ = (
        ForeignKeyConstraint(['order_id'], ['orders.id'], name='fk_order_item_orders'),
        ForeignKeyConstraint(['product_id'], ['products.id'], name='fk_order_items_product'),
        PrimaryKeyConstraint('id', name='order_items_pkey')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    order_id: Mapped[Optional[int]] = mapped_column(Integer)
    product_id: Mapped[Optional[int]] = mapped_column(Integer)
    quantity: Mapped[Optional[int]] = mapped_column(Integer)
    unit_price: Mapped[Optional[float]] = mapped_column(REAL)

    order: Mapped[Optional['Orders']] = relationship('Orders', back_populates='order_items')
    product: Mapped[Optional['Products']] = relationship('Products', back_populates='order_items')


class Payments(Base):
    __tablename__ = 'payments'
    __table_args__ = (
        ForeignKeyConstraint(['order_id'], ['orders.id'], name='fk_payments_order'),
        PrimaryKeyConstraint('id', name='payments_pkey')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    order_id: Mapped[Optional[int]] = mapped_column(Integer)
    amount: Mapped[Optional[float]] = mapped_column(REAL)
    payment_date: Mapped[Optional[str]] = mapped_column(String(50))

    order: Mapped[Optional['Orders']] = relationship('Orders', back_populates='payments')
