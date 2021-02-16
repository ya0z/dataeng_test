-- Car inventory
create table car(
id SERIAL PRIMARY KEY, 
manufacturer varchar(255), 
model varchar(100), 
variant varchar(100), 
serial_no varchar(50), 
weight float, 
engine_cc float, 
price float);
-- Salesperson
create table salesperson(
id SERIAL PRIMARY KEY,
name VARCHAR(255)
);
-- Sales transaction
create table sales(
id SERIAL PRIMARY KEY,
cust_name VARCHAR(255),
cust_phone INTEGER,
salesperson_id INTEGER REFERENCES salesperson(id),
car_id INTEGER REFERENCES car(id)
);