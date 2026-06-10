select *
from categories 

select *
from products 

alter table categories add primary key (id);
alter table orders add primary key (id);
alter table order_items add primary key(id);
alter table payments add primary key(id);
alter table products add primary key(id);
alter table customers add primary key (id);


alter table products 
add constraint fk_product_category
foreign key (category_id) references categories(id);

alter table orders
add constraint fk_orders_customers
foreign key (customer_id) references customers(id);

alter table order_items
add constraint fk_order_item_orders
foreign key (order_id) references  orders(id);

alter table order_items 
add constraint fk_order_items_product
foreign key (product_id) references products(id);

alter table payments 
add constraint fk_payments_order
foreign key (order_id) references orders (id);