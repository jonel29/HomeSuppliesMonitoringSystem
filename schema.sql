
CREATE DATABASE IF NOT EXISTS home_supplies_db;

USE home_supplies_db;

CREATE TABLE IF NOT EXISTS home_supplies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);
