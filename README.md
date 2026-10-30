
# Home Supplies Monitoring System

## Project Description

The Home Supplies Monitoring System is a Python and MySQL console-based application designed to help households manage and monitor their everyday supplies.

It allows users to add, view, update, delete, and search household supplies. It also provides a low-stock warning and calculates the total inventory value.

## Features

1. Add Home Supply
2. View All Supplies
3. Update Home Supply
4. Delete Home Supply
5. Search Home Supply
6. View Low-Stock Items
7. View Total Inventory Value

## Technologies Used

- Python
- MySQL
- XAMPP
- phpMyAdmin
- MySQL Connector

## Database Information

Database Name: home_supplies_db

Table Name: home_supplies

### Table Columns

- id
- item_name
- category
- quantity
- price

## Installation and Setup

1. Install Python.
2. Install XAMPP.
3. Start Apache and MySQL.
4. Open phpMyAdmin.
5. Import the schema.sql file.
6. Install MySQL Connector using:

   py -m pip install mysql-connector-python

7. Run the application using:

   py main.py

## Project Files

- main.py - Main menu of the application.
- database.py - MySQL connection.
- todo.py - CRUD operations and other functions.
- schema.sql - Database and table creation.
- README.md - Project documentation.

## Developer

Created as a Python and MySQL performance task project.
