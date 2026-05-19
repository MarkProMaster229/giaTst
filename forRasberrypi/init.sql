create table users(
id serial primary key,
name varchar(255),
about text
);

create table pictures(
id serial primary key,
fk_users integer,
picture_patch varchar(255)
);

alter table pictures
add constraint fk_pictures_users
foreign key(fk_users) references users(id);