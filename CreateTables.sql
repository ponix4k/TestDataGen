CREATE TABLE Users (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    UserName VARCHAR(50) NOT NULL,
    Password VARCHAR(50) NOT NULL,
    EmailAddress VARCHAR(50) NOT NULL
);

CREATE TABLE `store`.`Customers` (
     `Name` VARCHAR(50) NOT NULL DEFAULT '\'\'' ,
      `Address` VARCHAR(50) NOT NULL DEFAULT '\'\'' ,
       `Email` VARCHAR(50) NOT NULL DEFAULT '\'\'' ,
        `Age` INT NOT NULL DEFAULT '0' ,
         `Phone` VARCHAR NOT NULL DEFAULT '0' )