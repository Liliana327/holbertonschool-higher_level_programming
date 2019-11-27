-- creates the database hbtn_0d_usa and the table cities
CREATE DATABASE if not exists hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE if not exists cities (id INT not NULL AUTO_INCREMENT, PRIMARY KEY, state_id INT not NULL, FOREIGN KEY(state_id) REFERENCES 
state_id(id), name VARCHAR(256) not NULL) ENGINE=INN0DB; 
