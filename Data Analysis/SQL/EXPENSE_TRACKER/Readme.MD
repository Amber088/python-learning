
Readme · MD
Expense Tracker (Python + SQLite3)
A command-line mini project for tracking personal expenses.

Features
Add expense (amount, category, date, description)
Show all expenses
Filter by month
Filter by category
Total spent
Average expense
Highest expenses (top N)
Category-wise report (total, count, average, % of total)
Delete expense
Project Structure
expense_tracker/
├── database.py     # DB connection + expenses table schema
├── operations.py   # All logic: add/filter/delete/reports
├── main.py         # CLI menu — run this file
└── expenses.db     # Created automatically on first run
How to Run
Requires only Python 3 (sqlite3 is built into the standard library).

bash
python3 main.py
Important: all three .py files (database.py, operations.py, main.py) must be in the same folder, with lowercase filenames exactly as shown above — Python's import system is case-sensitive.

Usage Notes
Date format: always use YYYY-MM-DD, e.g. 2026-07-17
Month filter format: use YYYY-MM, e.g. 2026-07
Expense ID: shown in the leftmost column when you view/filter expenses — use this exact number when deleting an expense
Database Schema
expenses: expense_id, amount, category, description, date, created_at
Possible Extensions
Export reports to CSV
Add a monthly budget limit with over-budget warnings
Add recurring expenses (rent, subscriptions)
Visualize category spending with a chart (e.g. matplotlib)

