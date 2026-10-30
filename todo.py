
from database import get_connection
from mysql.connector import Error


def add_supply():
    """Add a new household supply."""
    connection = None
    cursor = None

    try:
        item_name = input("Enter item name: ").strip()
        category = input("Enter category (Cleaning/Bathroom/Laundry): ").strip()
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price per item: "))

        if not item_name or not category:
            print("Item name and category cannot be empty.")
            return

        if quantity < 0 or price < 0:
            print("Quantity and price cannot be negative.")
            return

        connection = get_connection()
        cursor = connection.cursor()

        sql = """
            INSERT INTO home_supplies
            (item_name, category, quantity, price)
            VALUES (%s, %s, %s, %s)
        """

        values = (item_name, category, quantity, price)

        cursor.execute(sql, values)
        connection.commit()

        print("Supply added successfully!")

    except ValueError:
        print("Please enter a valid number for quantity and price.")
    except Error as error:
        print(f"Database error: {error}")

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()


def view_supplies():
    """Display all household supplies."""
    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM home_supplies")
        supplies = cursor.fetchall()

        if not supplies:
            print("No supplies found.")
            return

        print("\n========== HOME SUPPLIES ==========")

        for supply in supplies:
            print(f"\nID: {supply[0]}")
            print(f"Item: {supply[1]}")
            print(f"Category: {supply[2]}")
            print(f"Quantity: {supply[3]}")
            print(f"Price: PHP {supply[4]:.2f}")
            print("----------------------------------")

    except Error as error:
        print(f"Database error: {error}")

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()


def update_supply():
    """Update an existing household supply."""
    connection = None
    cursor = None

    try:
        view_supplies()

        supply_id = int(input("\nEnter the ID to update: "))

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM home_supplies WHERE id = %s",
            (supply_id,)
        )
        supply = cursor.fetchone()

        if not supply:
            print("Supply ID not found.")
            return

        print("Press Enter to keep the current value.")

        item_name = input(f"Item name [{supply[1]}]: ").strip()
        category = input(f"Category [{supply[2]}]: ").strip()
        quantity_input = input(f"Quantity [{supply[3]}]: ").strip()
        price_input = input(f"Price [{supply[4]}]: ").strip()

        if not item_name:
            item_name = supply[1]

        if not category:
            category = supply[2]

        quantity = int(quantity_input) if quantity_input else supply[3]
        price = float(price_input) if price_input else float(supply[4])

        if quantity < 0 or price < 0:
            print("Quantity and price cannot be negative.")
            return

        sql = """
            UPDATE home_supplies
            SET item_name = %s,
                category = %s,
                quantity = %s,
                price = %s
            WHERE id = %s
        """

        values = (item_name, category, quantity, price, supply_id)

        cursor.execute(sql, values)
        connection.commit()

        print("Supply updated successfully!")

    except ValueError:
        print("Please enter a valid ID, quantity, or price.")
    except Error as error:
        print(f"Database error: {error}")

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()


def delete_supply():
    """Delete a household supply."""
    connection = None
    cursor = None

    try:
        view_supplies()

        supply_id = int(input("\nEnter the ID to delete: "))

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT item_name FROM home_supplies WHERE id = %s",
            (supply_id,)
        )
        supply = cursor.fetchone()

        if not supply:
            print("Supply ID not found.")
            return

        confirm = input(
            f"Delete {supply[0]}? Type YES to confirm: "
        ).strip()

        if confirm == "YES":
            cursor.execute(
                "DELETE FROM home_supplies WHERE id = %s",
                (supply_id,)
            )
            connection.commit()
            print("Supply deleted successfully!")
        else:
            print("Deletion cancelled.")

    except ValueError:
        print("Please enter a valid ID.")
    except Error as error:
        print(f"Database error: {error}")

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()


def search_supply():
    """Search for a supply by name."""
    connection = None
    cursor = None

    try:
        keyword = input("Enter item name to search: ").strip()

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM home_supplies WHERE item_name LIKE %s",
            (f"%{keyword}%",)
        )

        supplies = cursor.fetchall()

        if not supplies:
            print("No matching supplies found.")
            return

        print("\n========== SEARCH RESULTS ==========")

        for supply in supplies:
            print(
                f"ID: {supply[0]} | "
                f"Item: {supply[1]} | "
                f"Category: {supply[2]} | "
                f"Quantity: {supply[3]} | "
                f"Price: PHP {supply[4]:.2f}"
            )

    except Error as error:
        print(f"Database error: {error}")

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()


def view_low_stock():
    """Display supplies with a quantity of 2 or less."""
    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM home_supplies WHERE quantity <= 2"
        )

        supplies = cursor.fetchall()

        print("\n========== LOW-STOCK SUPPLIES ==========")

        if not supplies:
            print("No low-stock supplies.")
            return

        for supply in supplies:
            print(
                f"{supply[1]} - Quantity: {supply[3]} "
                f"({supply[2]})"
            )

    except Error as error:
        print(f"Database error: {error}")

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()


def view_total_value():
    """Calculate the total value of all household supplies."""
    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT SUM(quantity * price) FROM home_supplies"
        )

        result = cursor.fetchone()
        total = result[0] if result[0] is not None else 0

        print(f"\nTotal Inventory Value: PHP {total:.2f}")

    except Error as error:
        print(f"Database error: {error}")

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
