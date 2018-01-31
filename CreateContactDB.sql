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
username VARCHAR(30) UNIQUE,
password VARCHAR(64));

CREATE TABLE contact ( firstname VARCHAR(30),
lastname VARCHAR(30),
phone VARCHAR(30),
email VARCHAR(30),
userid INT);

# Modify userid to have foreign key.
ALTER TABLE contact
ADD CONSTRAINT FK_contact
FOREIGN KEY (userid) REFERENCES user(id)
ON UPDATE CASCADE
ON DELETE CASCADE;

# Insert base users and data
INSERT INTO user (username,password) VALUES ('user','password');
INSERT INTO user (username, password) VALUES ('gabe', '9ed1515819dec61fd361d5fdabb57f41ecce1a5fe1fe263b98c0d6943b9b232e');
INSERT INTO user (username, password) VALUES ('cole','7842275f98964d3914268cc7b66e35b8b614663978b64a1e9ecb3c5499427ed9');

 INSERT INTO contact VALUES ('Cole','Sil','407555555','cole@gmail.com',2);
 INSERT INTO contact VALUES ('James', 'Joyce', '5553456789','jimmy@dublin.com',2);
 INSERT INTO contact VALUES ('Scott', 'Fitzgerald', '5553456789', 'ScottyBoy@gmail.com', 2);
 INSERT INTO contact VALUES ('The', 'Rock', '5553425678', 'peoplesElbow@gmail.com', 3);
 INSERT INTO contact VALUES ('Cole', 'Silvernail', '5555555555', 'cole@gmail.com', 1);
 INSERT INTO contact VALUES ('Lebron', 'James', '3215555555','lbj@lemail.com',3);
 INSERT INTO contact VALUES ('Crocodile','Dundee','5558494756','isthataknife@CrocLuvr.com',2);
