from database import get_connection
 
 
# ---------------------------------------------------------------------------
# ADD / DELETE
# ---------------------------------------------------------------------------
 
def add_expense(amount, category, date, description=""):
    try:
        amount = float(amount)
    except ValueError:
        print("❌ Amount must be a number.")
        return
 
    conn = get_connection()
    conn.execute(
        "INSERT INTO expenses (amount, category, description, date) "
        "VALUES (?, ?, ?, ?)",
        (amount, category.strip(), description.strip(), date.strip()),
    )
    conn.commit()
    conn.close()
    print(f"✅ Expense added: ₹{amount:.2f} on {date} [{category}]")
 
 
def delete_expense(expense_id):
    conn = get_connection()
    cursor = conn.execute("DELETE FROM expenses WHERE expense_id = ?", (expense_id,))
    conn.commit()
    conn.close()
    if cursor.rowcount == 0:
        print("❌ No expense found with that ID.")
    else:
        print("✅ Expense deleted.")
 
 
# ---------------------------------------------------------------------------
# VIEW / FILTER
# ---------------------------------------------------------------------------
 
def _print_expenses(rows):
    if not rows:
        print("No expenses found.")
        return
 
    print(f"\n{'ID':<5}{'Date':<12}{'Category':<15}{'Amount':<12}{'Description':<25}")
    print("-" * 69)
    for r in rows:
        print(f"{r['expense_id']:<5}{r['date']:<12}{r['category']:<15}"
              f"₹{r['amount']:<11.2f}{(r['description'] or ''):<25}")
 
    total = sum(r["amount"] for r in rows)
    print("-" * 69)
    print(f"Total: ₹{total:.2f}  ({len(rows)} expense(s))")
 
 
def show_all_expenses():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM expenses ORDER BY date DESC").fetchall()
    conn.close()
    _print_expenses(rows)
 
 
def filter_by_month(year_month):
    """year_month should be in 'YYYY-MM' format, e.g. '2026-07'."""
    conn = get_connection()
    rows = conn.execute(
        "SELECT * FROM expenses WHERE strftime('%Y-%m', date) = ? ORDER BY date",
        (year_month,),
    ).fetchall()
    conn.close()
    _print_expenses(rows)
 
 
def filter_by_category(category):
    conn = get_connection()
    rows = conn.execute(
        "SELECT * FROM expenses WHERE category LIKE ? ORDER BY date",
        (f"%{category}%",),
    ).fetchall()
    conn.close()
    _print_expenses(rows)
 
 
# ---------------------------------------------------------------------------
# REPORTS
# ---------------------------------------------------------------------------
 
def total_spent():
    conn = get_connection()
    row = conn.execute("SELECT SUM(amount) AS total FROM expenses").fetchone()
    conn.close()
    total = row["total"] or 0
    print(f"Total spent: ₹{total:.2f}")
 
 
def average_expense():
    conn = get_connection()
    row = conn.execute("SELECT AVG(amount) AS avg_amt, COUNT(*) AS c FROM expenses").fetchone()
    conn.close()
    if not row["c"]:
        print("No expenses recorded yet.")
        return
    print(f"Average expense: ₹{row['avg_amt']:.2f}  (across {row['c']} entries)")
 
 
def highest_expenses(limit=5):
    conn = get_connection()
    rows = conn.execute(
        "SELECT * FROM expenses ORDER BY amount DESC LIMIT ?", (limit,)
    ).fetchall()
    conn.close()
 
    if not rows:
        print("No expenses recorded yet.")
        return
 
    print(f"\nTop {len(rows)} Highest Expenses")
    print(f"{'ID':<5}{'Date':<12}{'Category':<15}{'Amount':<12}{'Description':<25}")
    print("-" * 69)
    for r in rows:
        print(f"{r['expense_id']:<5}{r['date']:<12}{r['category']:<15}"
              f"₹{r['amount']:<11.2f}{(r['description'] or ''):<25}")
 
 
def category_wise_report():
    conn = get_connection()
    rows = conn.execute(
        """
        SELECT category, SUM(amount) AS total, COUNT(*) AS c, AVG(amount) AS avg_amt
        FROM expenses
        GROUP BY category
        ORDER BY total DESC
        """
    ).fetchall()
    conn.close()
 
    if not rows:
        print("No expenses recorded yet.")
        return
 
    grand_total = sum(r["total"] for r in rows)
 
    print(f"\n{'Category':<15}{'Total':<12}{'Count':<8}{'Avg':<12}{'% of Total':<10}")
    print("-" * 57)
    for r in rows:
        pct = (r["total"] / grand_total) * 100 if grand_total else 0
        print(f"{r['category']:<15}₹{r['total']:<11.2f}{r['c']:<8}"
              f"₹{r['avg_amt']:<11.2f}{pct:<10.1f}")
    print("-" * 57)
    print(f"Grand Total: ₹{grand_total:.2f}")
 
