-- creates the database hbtn_0d_2 and the user user_0d_2
CREATE DATABASE if not exists hbtn_0d_2;
GRANT SELECT ON hbtn_0d_2.* to user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
