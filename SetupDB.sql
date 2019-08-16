CREATE DATABASE wpdb;
CREATE USER 'store'@'localhost' IDENTIFIED BY 'store';
GRANT ALL PRIVILEGES ON store.* TO 'store'@'localhost';
FLUSH PRIVILEGES;

CREATE TABLE IF NOT EXISTS customers (
id int AUTO_INCREMENT,
name varchar(30),
address varchar(30),
email varchar(50),
age int,
phone varchar(15)
);

INSERT INTO `customers` (name,address,email,age,phone)
values
('customer1','address1','customer1@store',25,'01234567890'),
('customer2','address2','customer2@store',25,'01234567890'),
('customer3','address3','customer3@store',25,'01234567890'),
('customer4','address4','customer4@store',25,'01234567890'),
('customer5','address5','customer5@store',25,'01234567890'),
('customer6','address6','customer5@store',25,'01234567890');

CREATE TABLE IF NOT EXISTS users (
id int AUTO_INCREMENT ,
username varchar(25),
email varchar(50),
password varchar(25),
PRIMARY KEY (id)
);

INSERT INTO `users`  (username ,email,password)
values 
('admin','admin@stores','adminpassword1'),
('user1','user1@stores','userpassword1'),
('user2','user2@stores','userpassword2'),
('user3','user3@stores','userpassword3'),
('user4','user4@stores','userpassword4'),
('user5','user5@stores','userpassword5');
