CREATE USER 'store'@'localhost' IDENTIFIED BY 'store';
create database store;
use store;
GRANT ALL PRIVILEGES ON store. * TO 'store'@'localhost';