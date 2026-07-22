import sqlite3
import os

DB_NAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "school.db")


def get_connection():
    """Return a connection to the SQLite database with foreign keys enabled."""
    conn = sqlite3.connect(DB_NAME)
    conn.execute("PRAGMA foreign_keys = ON")
    conn.row_factory = sqlite3.Row  # lets us access columns by name
    return conn


def initialize_database():
    """Create all tables if they don't already exist."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id   INTEGER PRIMARY KEY AUTOINCREMENT,
            name         TEXT NOT NULL,
            roll_no      TEXT NOT NULL UNIQUE,
            class_name   TEXT NOT NULL,
            email        TEXT,
            phone        TEXT,
            created_at   TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attendance (
            attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id    INTEGER NOT NULL,
            date          TEXT NOT NULL,
            status        TEXT NOT NULL CHECK (status IN ('Present', 'Absent')),
            FOREIGN KEY (student_id) REFERENCES students (student_id) ON DELETE CASCADE,
            UNIQUE (student_id, date)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS grades (
            grade_id    INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id  INTEGER NOT NULL,
            subject     TEXT NOT NULL,
            exam_type   TEXT NOT NULL,
            marks       REAL NOT NULL,
            max_marks   REAL NOT NULL DEFAULT 100,
            FOREIGN KEY (student_id) REFERENCES students (student_id) ON DELETE CASCADE
        )
    """)

    conn.commit()
    conn.close()

