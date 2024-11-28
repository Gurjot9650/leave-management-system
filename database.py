# database.py

import sqlite3
from sqlite3 import Error

def create_connection():
    """Create a database connection to the SQLite database."""
    try:
        connection = sqlite3.connect('leave_management.db')
        print("Connected to SQLite database")
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def initialize_database(connection):
    """Create the leaves table if it doesn't exist."""
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS leaves (
        leave_id INTEGER PRIMARY KEY AUTOINCREMENT,
        employee_id TEXT NOT NULL,
        employee_name TEXT NOT NULL,
        leave_type TEXT NOT NULL,
        start_date TEXT NOT NULL,
        end_date TEXT NOT NULL,
        reason TEXT
    );
    '''
    try:
        cursor = connection.cursor()
        cursor.execute(create_table_query)
        connection.commit()
        print("Database initialized successfully.")
    except Error as e:
        print(f"Error: {e}")
