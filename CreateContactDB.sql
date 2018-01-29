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

INSERT INTO users (userName,password) VALUES ('user','password');
GRANT ALL PRIVILEGES ON `contactDB`.* TO 'user'@'localhost';