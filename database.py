
import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "",
    "database": "home_supplies_db",
}


def get_connection():
    """Connect to the home supplies database."""
    return mysql.connector.connect(**DB_CONFIG)


def test_connection():
    """Test the MySQL connection."""
    connection = None

    try:
        connection = get_connection()

        if connection.is_connected():
            print("Connected to MySQL successfully!")
            return True

    except Error as error:
        print(f"Could not connect to MySQL: {error}")
        print("Check if MySQL is running and the database exists.")
        return False

    finally:
        if connection is not None and connection.is_connected():
            connection.close()
