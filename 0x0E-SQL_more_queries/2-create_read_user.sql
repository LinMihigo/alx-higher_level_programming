-- creates a db hbtn_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANTS SELECT ON *.* TO 'user_0d_1'@'localhost';
