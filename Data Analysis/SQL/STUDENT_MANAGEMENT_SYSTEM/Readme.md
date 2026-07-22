Student Management System (Python + SQLite3)

A command-line mini project for managing students, attendance, and grades.

Features


Student CRUD: add, view, update, delete, search students
Attendance: mark present/absent per date, view history, get attendance %
Grades: record marks per subject/exam, view records, get average + letter grade
Reports: full student profile, class-wide performance ranking


Project Structure

student_management_system/
├── database.py     # DB connection + table schema (students, attendance, grades)
├── operations.py   # All CRUD / business logic functions
├── main.py         # CLI menu — run this file
└── school.db       # Created automatically on first run

How to Run

Requires only Python 3 (sqlite3 is built into the standard library — no installs needed).

bashpython3 main.py

You'll see a menu:

1. Student Management
2. Attendance Management
3. Grade Management
4. Reports
5. Exit

Database Schema


students: student_id, name, roll_no (unique), class_name, email, phone
attendance: attendance_id, student_id (FK), date, status (Present/Absent)
grades: grade_id, student_id (FK), subject, exam_type, marks, max_marks


Foreign keys cascade on delete — removing a student also removes their attendance
and grade records.

Possible Extensions (if you want to level this up further)


Export reports to CSV/PDF
Add a teachers table with subject assignments
Switch the CLI to a Flask web UI (same operations.py and database.py would work almost unchanged)
Add login/authentication for admin vs. viewer roles