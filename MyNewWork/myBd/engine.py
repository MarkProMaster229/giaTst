from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

databaseConn = "postgresql://postgres:1@localhost:5432/my_test_bd_for_me"


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

