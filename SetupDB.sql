CREATE DATABASE wpdb;
CREATE USER 'store'@'localhost' IDENTIFIED BY 'store';
GRANT ALL PRIVILEGES ON store.* TO 'store'@'localhost';
FLUSH PRIVILEGES;
