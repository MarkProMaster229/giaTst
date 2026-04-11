from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


DatabaseConnect = "postgresql://postgres:1@localhost:5432/my_office"


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



#create table users(
#id serial primary key,
#type_ul_ip boolean,--if true юридическое лицо if false индивидуальный предприниматель
#user_name varchar(255),
#inn bigint,
#kpp bigint,
#ogrn bigint,
#ur_adress text,
#contact text

#)

#create table order_my(
#id serial primary key,
#data_order TIMESTAMPTZ DEFAULT NOW(),
#data_delivery integer,
#stat varchar(50),
#fk_users integer
#)




#create table full_products(
#id serial primary key,
#product varchar,
#price integer,
#fk_order_my integer
#)


#alter table order_my
#add constraint fr_order_users
#foreign key (fk_users) references users(id)

#alter table full_products
#add constraint fr_fullprod_order
#foreign key(fk_order_my) references order_my(id)
