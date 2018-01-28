DROP DATABASE IF EXISTS `contactDB`;
CREATE DATABASE `contactDB`;
USE `contactDB`;

CREATE TABLE user (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, 
userName VARCHAR(30),
password VARCHAR(64),
signup_date DATE);

ALTER TABLE user ADD signup_date DATE;


CREATE TABLE contact ( name VARCHAR(30),
phone VARCHAR(30),
email VARCHAR(30),
userID INT);


ALTER TABLE contact
ADD CONSTRAINT FK_contact
FOREIGN KEY (userID) REFERENCES user(id)
ON UPDATE CASCADE
ON DELETE CASCADE;

INSERT INTO users (userName,password) VALUES ('user','password');
GRANT ALL PRIVILEGES ON `contactDB`.* TO 'user'@'localhost';