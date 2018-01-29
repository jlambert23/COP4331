#=========================================================================#
# WARNING:                                                                #
# THIS SCRIPT WILL DELETE AN EXISTING DATABASE.                           #
# BACKUP ANY DATA YOU MAY WANT TO PRESERVE.                               #
#                                                                         #
# This script should be run by a user with database creation privileges.  #
# To run this script:                                                     #
#                     sudo mysql < setup.sql;                             #
#                                                                         #
#=========================================================================#

# Create database.
DROP DATABASE IF EXISTS `contactDB`;
CREATE DATABASE `contactDB`;
USE `contactDB`;

# Setup database user.
CREATE USER IF NOT EXISTS 'db-sys'@'localhost';
GRANT ALL PRIVILEGES ON `contactDB`.* TO `db-sys`@`localhost`;


CREATE TABLE user (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, 
userName VARCHAR(30),
password VARCHAR(64));




CREATE TABLE contact ( firstname VARCHAR(30),
lastname VARCHAR(30),
phone VARCHAR(30),
email VARCHAR(30),
userID INT);


ALTER TABLE contact
ADD CONSTRAINT FK_contact
FOREIGN KEY (userID) REFERENCES user(id)
ON UPDATE CASCADE
ON DELETE CASCADE;

INSERT INTO user (userName,password) VALUES ('user','password');
GRANT ALL PRIVILEGES ON `contactDB`.* TO 'user'@'localhost';

INSERT INTO user (userName, password) VALUES ('gabe', '9ed1515819dec61fd361d5fdabb57f41ecce1a5fe1fe263b98c0d6943b9b232e');

 INSERT INTO contact VALUES ('Cole','Sil','407555555','cole@gmail.com',2);
 INSERT INTO contact VALUES ('James', 'Joyce', '5553456789','jimmy@dublin.com',2);
 INSERT INTO contact VALUES ('Scott', 'Fitzgerald', '5553456789', 'ScottyBoy@gmail.com', 2);
 INSERT INTO contact VALUES ('The', 'Rock', '5553425678', 'peoplesElbow@gmail.com', 2);
 INSERT INTO contact VALUES ('Cole', 'Silvernail', '5555555555', 'cole@gmail.com', 1);