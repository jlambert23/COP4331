# WARNING:
# THIS SCRIPT WILL DELETE AN EXISTING DATABASE.
# BACKUP ANY DATA YOU MAY WANT TO PRESERVE.
#
# This script should be run by a user with database creation privileges.
# To run this script: sudo mysql source setup.sql;

# Create database.
DROP DATABASE IF EXISTS `contactDB`;
CREATE DATABASE `contactDB`;
USE `contactDB`;

# Setup database user.
CREATE USER IF NOT EXISTS 'db-sys'@'localhost';
GRANT ALL PRIVILEGES ON `contactDB`.* TO `db-sys`@`localhost`;

# Add and configure tables.
CREATE TABLE `users` (
  `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT ,
  `userName` VARCHAR(30) NOT NULL DEFAULT '' ,
  `password` VARCHAR(64) NOT NULL DEFAULT '' );

CREATE TABLE `contacts` (
  `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT ,
  `name` VARCHAR(30) NOT NULL DEFAULT '' ,
  `phone` VARCHAR(30) NOT NULL DEFAULT '' ,
  `email` VARCHAR(30) NOT NULL DEFAULT '' ,
  `userID` INT NOT NULL DEFAULT '0' );

ALTER TABLE contact
ADD CONSTRAINT FK_contact
FOREIGN KEY (userID) REFERENCES user(id)
ON UPDATE CASCADE
ON DELETE CASCADE;


# Testing insert
INSERT INTO users (userName,password) VALUES ('user','password');
INSERT INTO contacts (name) VALUES ('Blue');