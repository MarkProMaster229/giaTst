from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


DatabaseConnect = "postgresql://postgres:1@localhost:5432/mytoyhouse"

engine = create_engine(
    DatabaseConnect,
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

