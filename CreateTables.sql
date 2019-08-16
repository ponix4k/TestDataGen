CREATE TABLE Users (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    UserName VARCHAR(50) NOT NULL,
    Password VARCHAR(50) NOT NULL,
    EmailAddress VARCHAR(50) NOT NULL
);

CREATE TABLE customers (
    Name VARCHAR(50),
    Address VARCHAR(50),
    Email VARCHAR(50),
    Age INT,
    Phone VARCHAR
);
