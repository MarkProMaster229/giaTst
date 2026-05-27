create table users(
    id serial primary key,
    user_name varchar(255),
    id_generate_base36_4 varchar(4),--для генерации решено взять алгоритм base36 с 4 символами при регистрации делаем запрос проверим коллизию 
    user_password varchar(255),--без хеша похуй пока так
    user_about varchar(255),
    data timestamptz not null default now()
);
create table chat(
    id serial primary key,
    id_for_chat64 bigint,-- генерация под 64 символа
    fk_user_1 integer not null,-- тут хардкодится связь меж юзерами
    fk_user_2 integer not null,-- тут хардкодится связь меж юзерами
    fk_image integer -- ну это обьект minio
);
--под форум принято сделать отдельную таблицу, для разделения ответственности(на самом деле мне ума не хватает придумать что то лучше)
create table forum(
    id serial primary key,
    fk_only_user integer,
    fk_message integer-- конечно было бы круто сделать так - если приватно то ебашит ошибку никакой записи, ибо private в message в строке flag означает что то пошло не так
);
create table image(
    id serial primary key,
    about text,-- я предполагаю что фото можно описать юзером, но можно и не описывать
    link_for_minio text--ссылка на объект в minio
);
create table message(
    id serial primary key,
    message text,
    fk_chat integer,
    data timestamptz not null default now(),
    flag boolean not null default false -- если сообщение приватно - false если публично public
);


alter table chat
add constraint fk_user_1
foreign key(fk_user_1) references users(id),
add constraint fk_user_2
foreign key(fk_user_2)references users(id),
add constraint fk_image
foreign key (fk_image)references image(id);

alter table forum
add constraint fk_only_user
foreign key(fk_only_user)references users(id),
add constraint fk_message
foreign key(fk_message)references message(id);

alter table image 
add constraint fk_chat
foreign key(fk_chat)references chat(id)

