
from database import test_connection
from todo import (
    add_supply,
    view_supplies,
    update_supply,
    delete_supply,
    search_supply,
    view_low_stock,
    view_total_value,
)


def main():
    print("=" * 40)
    print("   HOME SUPPLIES MONITORING SYSTEM")
    print("=" * 40)

    if not test_connection():
        print("Please fix the database connection before continuing.")
        return

    while True:
        print("\n========== MAIN MENU ==========")
        print("1. Add Home Supply")
        print("2. View All Supplies")
        print("3. Update Home Supply")
        print("4. Delete Home Supply")
        print("5. Search Home Supply")
        print("6. View Low-Stock Items")
        print("7. View Total Inventory Value")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            add_supply()
        elif choice == "2":
            view_supplies()
        elif choice == "3":
            update_supply()
        elif choice == "4":
            delete_supply()
        elif choice == "5":
            search_supply()
        elif choice == "6":
            view_low_stock()
        elif choice == "7":
            view_total_value()
        elif choice == "8":
            print("Thank you for using Home Supplies Monitoring System!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")


if __name__ == "__main__":
    main()
