import sqlite3
conn = sqlite3.connect("Student.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE Students(
    id INTEGER PRIMARY KEY
    Name TEXT
    age INTEGER
    )
""")
cursor.commit()
conn.commit()
