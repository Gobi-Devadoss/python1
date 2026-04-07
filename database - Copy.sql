CREATE DATABASE expense_management_system;

USE expense_management_system;

CREATE TABLE users(
user_id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(50)
);

CREATE TABLE expense(
exp_id INT PRIMARY KEY AUTO_INCREMENT,
user_id int,
amount FLOAT,
category VARCHAR(50),
description VARCHAR(100),
date DATE,
FOREIGN KEY(user_id) REFERENCES users(user_id)
);