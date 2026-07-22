import sqlite3
import os
 
DB_NAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "expenses.db")
 
 
def get_connection():
    """Return a connection to the SQLite database."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # lets us access columns by name
    return conn
 
 
def initialize_database():
    """Create the expenses table if it doesn't already exist."""
    conn = get_connection()
    cursor = conn.cursor()
 
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            expense_id   INTEGER PRIMARY KEY AUTOINCREMENT,
            amount       REAL NOT NULL,
            category     TEXT NOT NULL,
            description  TEXT,
            date         TEXT NOT NULL,
            created_at   TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)
 
    conn.commit()
    conn.close()
 
