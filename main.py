# main.py

from database import create_connection, initialize_database
from leave import add_leave, view_leaves, search_leave, update_leave, delete_leave

def main_menu():
    print("\n=== Leave Management System ===")
    print("1. Add New Leave Record")
    print("2. View All Leave Records")
    print("3. Search for a Leave Record")
    print("4. Update Leave Record")
    print("5. Delete a Leave Record")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")
    return choice

def main():
    connection = create_connection()
    if connection:
        initialize_database(connection)
        while True:
            choice = main_menu()
            if choice == '1':
                add_leave(connection)
            elif choice == '2':
                view_leaves(connection)
            elif choice == '3':
                search_leave(connection)
            elif choice == '4':
                update_leave(connection)
            elif choice == '5':
                delete_leave(connection)
            elif choice == '6':
                connection.close()
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a number between 1 and 6.")
    else:
        print("Failed to connect to the database.")

if __name__ == "__main__":
    main()
