# leave.py

from sqlite3 import Error

def add_leave(connection):
    cursor = connection.cursor()
    employee_id = input("Employee ID: ")
    employee_name = input("Employee Name: ")
    leave_type = input("Leave Type (e.g., Annual, Sick): ")
    start_date = input("Start Date (YYYY-MM-DD): ")
    end_date = input("End Date (YYYY-MM-DD): ")
    reason = input("Reason: ")

    query = """
    INSERT INTO leaves (employee_id, employee_name, leave_type, start_date, end_date, reason)
    VALUES (?, ?, ?, ?, ?, ?)
    """
    values = (employee_id, employee_name, leave_type, start_date, end_date, reason)
    try:
        cursor.execute(query, values)
        connection.commit()
        print("Leave record added successfully!")
    except Error as e:
        print(f"Error: {e}")
        connection.rollback()

def view_leaves(connection):
    cursor = connection.cursor()
    query = "SELECT * FROM leaves"
    try:
        cursor.execute(query)
        records = cursor.fetchall()
        if records:
            print("\nAll Leave Records:")
            print("{:<10} {:<15} {:<20} {:<15} {:<12} {:<12} {:<30}".format(
                "Leave ID", "Employee ID", "Employee Name", "Leave Type", "Start Date", "End Date", "Reason"
            ))
            print("-" * 120)
            for row in records:
                print("{:<10} {:<15} {:<20} {:<15} {:<12} {:<12} {:<30}".format(*row))
        else:
            print("No leave records found.")
    except Error as e:
        print(f"Error: {e}")

def search_leave(connection):
    cursor = connection.cursor()
    search_term = input("Enter Employee ID or Name to search: ")
    query = """
    SELECT * FROM leaves
    WHERE employee_id LIKE ? OR employee_name LIKE ?
    """
    try:
        cursor.execute(query, ('%' + search_term + '%', '%' + search_term + '%'))
        records = cursor.fetchall()
        if records:
            print("\nSearch Results:")
            print("{:<10} {:<15} {:<20} {:<15} {:<12} {:<12} {:<30}".format(
                "Leave ID", "Employee ID", "Employee Name", "Leave Type", "Start Date", "End Date", "Reason"
            ))
            print("-" * 120)
            for row in records:
                print("{:<10} {:<15} {:<20} {:<15} {:<12} {:<12} {:<30}".format(*row))
        else:
            print("No matching leave records found.")
    except Error as e:
        print(f"Error: {e}")

def update_leave(connection):
    cursor = connection.cursor()
    leave_id = input("Enter Leave ID to update: ")
    query = "SELECT * FROM leaves WHERE leave_id = ?"
    try:
        cursor.execute(query, (leave_id,))
        record = cursor.fetchone()
        if record:
            print("\nCurrent Leave Details:")
            print("{:<10} {:<15} {:<20} {:<15} {:<12} {:<12} {:<30}".format(
                "Leave ID", "Employee ID", "Employee Name", "Leave Type", "Start Date", "End Date", "Reason"
            ))
            print("-" * 120)
            print("{:<10} {:<15} {:<20} {:<15} {:<12} {:<12} {:<30}".format(*record))
            print("\nEnter new details (leave blank to keep current value):")
            employee_id = input(f"Employee ID [{record[1]}]: ") or record[1]
            employee_name = input(f"Employee Name [{record[2]}]: ") or record[2]
            leave_type = input(f"Leave Type [{record[3]}]: ") or record[3]
            start_date = input(f"Start Date [{record[4]}]: ") or record[4]
            end_date = input(f"End Date [{record[5]}]: ") or record[5]
            reason = input(f"Reason [{record[6]}]: ") or record[6]

            update_query = """
            UPDATE leaves SET employee_id = ?, employee_name = ?, leave_type = ?, start_date = ?,
            end_date = ?, reason = ? WHERE leave_id = ?
            """
            values = (employee_id, employee_name, leave_type, start_date, end_date, reason, leave_id)
            cursor.execute(update_query, values)
            connection.commit()
            print("Leave record updated successfully!")
        else:
            print("Leave record not found.")
    except Error as e:
        print(f"Error: {e}")
        connection.rollback()

def delete_leave(connection):
    cursor = connection.cursor()
    leave_id = input("Enter Leave ID to delete: ")
    query = "DELETE FROM leaves WHERE leave_id = ?"
    try:
        cursor.execute(query, (leave_id,))
        connection.commit()
        if cursor.rowcount:
            print("Leave record deleted successfully!")
        else:
            print("Leave record not found.")
    except Error as e:
        print(f"Error: {e}")
        connection.rollback()
