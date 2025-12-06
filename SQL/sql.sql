create table pro(
id int,
name varchar(20),
price int,
add_data datetime
)//

create procedure greet_user(in name varchar(20))
begin
select concat('Hello',name,'how are you');
end//

create procedure add_item(in id int, in name varchar(10),in price int)
begin
insert into pro (id,name,price,add_date) values (id,name,price,sysdate());
select 'item add successfully';
select * from pro;
end//

create table product(
product_id int,
name varchar(20),
stock int
)//

create table order(
product_id int,
orders_date date,
qty int
)//

insert into product values(1,'redmi',10)///

create trigger stocks
after insert
on orders
for each row
begin
	update product
	set stock = stock - new.qty
    where product_id = new.product_id;
end//