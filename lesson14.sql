create database if not exists lesson14;
use lesson14;
show tables;


create table Users
(
    id int unsigned primary key auto_increment, -- Уникальный идентификатор
	username varchar(64) not null,
	password varchar(64) not null,
	email varchar(50) unique not null
);


create table seller
(
    id int unsigned primary key auto_increment, -- Уникальный идентификатор
    company varchar(64) not null,
    phone varchar(20) not null
);


create table products
(
    id int unsigned primary key auto_increment, -- Уникальный идентификатор
    name varchar(64) not null,
    cost int unsigned not null,
    count int unsigned not null,
    seller_id int unsigned not null, -- Для уникального ключа seller
    foreign key (seller_id) references seller (id) /* Создан внешний ключ, поле seller_id
    из этой таблицы ссылается на поле id из таблицы seller */
);


create table orders
(
    id int unsigned primary key auto_increment, -- Уникальный идентификатор
    user_id int unsigned not null, -- Для уникального ключа Users
    product_id int unsigned not null, -- Для уникального ключа products
    count int unsigned not null,
    foreign key (user_id) references Users (id), /* Создан внешний ключ,
    поле user_id из этой таблицы ссылается на поле id из таблицы Users */
    foreign key (product_id) references products (id) /* Создан внешний ключ,
    поле product_id из этой таблицы ссылается на поле id из таблицы products */
);


select * from Users;
select * from seller;
select * from products;
select * from orders;
show tables;
alter table seller add unique (company);

insert Users(username, password, email) values('Artur', 'w12345', 'arturred@gmail.com');
insert Users(username, password, email) values('Alex', 'qwe123456789', 'alex1996@gmail.com');
insert Users(username, password, email) values('Max', 'qwerty000', 'maxon@gmail.com');
insert Users(username, password, email) values('Kate', '123456789', 'kate11121991@yandex.ru');
insert seller(company, phone) values('Prostore', '+375294561268');
insert seller(company, phone) values('Amifruit', '+375336541269');
insert seller(company, phone) values('Delovoy', '+375442587932');
insert products(name, cost, count, seller_id) values('wine', 25, 2000, 1);
insert products(name, cost, count, seller_id) values('tomatoes', 10, 5000, 2);
insert products(name, cost, count, seller_id) values('A4 paper', 40, 250, 3);
insert orders(user_id, product_id, count) values(3, 2, 5);
insert orders(user_id, product_id, count) values(2, 1, 125);
insert orders(user_id, product_id, count) values(1, 3, 48);

select * from Users;
select * from seller;
select * from products;
select * from orders;
select * from products
order by cost;
select min(cost), max(cost) from products;
select sum(count) from products;
select sum(count * cost) from products;
update products set cost = 30, count = 2100 where id = 1;
select * from products