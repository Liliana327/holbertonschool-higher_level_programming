-- creates the database hbtn_0d_usa and the table states
CREATE DATABASE if not exists hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE if not exists states (id INT not NULL primary key auto_generated, name VARCHAR(256) not NULL);
