# WARNING:
# THIS SCRIPT WILL DELETE AN EXISTING DATABASE.
# BACKUP ANY DATA YOU MAY WANT TO PRESERVE.
#
# This script should be run by a user with database creation privileges.

DROP DATABASE IF EXISTS `contactDB`;
CREATE DATABASE `contactDB`;
USE `contactDB`;

CREATE TABLE `users` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `userName` VARCHAR(20) NOT NULL DEFAULT '' ,
  `password` VARCHAR(64) NOT NULL DEFAULT '' ,
  PRIMARY KEY (`ID`));

CREATE TABLE `contacts` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `name` VARCHAR(20) NOT NULL DEFAULT '' ,
  `phone` VARCHAR(50) NOT NULL DEFAULT '' ,
  `email` VARCHAR(20) NOT NULL DEFAULT '' ,
  `userID` INT NOT NULL DEFAULT '0' ,
  PRIMARY KEY (`ID`));

INSERT INTO users (userName,password) VALUES ('user','password');
GRANT ALL PRIVILEGES ON `contactDB`.* TO 'user'@'localhost';

# Testing insert
INSERT INTO contacts (name) VALUES ('Blue');