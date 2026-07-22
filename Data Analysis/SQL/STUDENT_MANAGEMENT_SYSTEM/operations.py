import sqlite3
from database import get_connection
 
 
# ---------------------------------------------------------------------------
# STUDENT CRUD
# ---------------------------------------------------------------------------
 
def add_student(name, roll_no, class_name, email="", phone=""):
    conn = get_connection()
    try:
        conn.execute(
            "INSERT INTO students (name, roll_no, class_name, email, phone) "
            "VALUES (?, ?, ?, ?, ?)",
            (name, roll_no, class_name, email, phone),
        )
        conn.commit()
        print(f"✅ Student '{name}' added successfully.")
    except sqlite3.IntegrityError:
        print(f"❌ Error: Roll number '{roll_no}' already exists.")
    finally:
        conn.close()
 
 
def view_all_students():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM students ORDER BY class_name, roll_no").fetchall()
    conn.close()
 
    if not rows:
        print("No students found.")
        return
 
    print(f"\n{'ID':<5}{'Name':<20}{'Roll No':<10}{'Class':<10}{'Email':<25}{'Phone':<15}")
    print("-" * 85)
    for r in rows:
        print(f"{r['student_id']:<5}{r['name']:<20}{r['roll_no']:<10}"
              f"{r['class_name']:<10}{(r['email'] or ''):<25}{(r['phone'] or ''):<15}")
 
 
def get_student_by_id(student_id):
    conn = get_connection()
    row = conn.execute(
        "SELECT * FROM students WHERE student_id = ?", (student_id,)
    ).fetchone()
    conn.close()
    return row
 
 
def update_student(student_id, field, new_value):
    valid_fields = {"name", "roll_no", "class_name", "email", "phone"}
    if field not in valid_fields:
        print(f"❌ Invalid field. Choose from: {', '.join(valid_fields)}")
        return
 
    conn = get_connection()
    try:
        conn.execute(
            f"UPDATE students SET {field} = ? WHERE student_id = ?",
            (new_value, student_id),
        )
        if conn.total_changes == 0:
            print("❌ No student found with that ID.")
        else:
            conn.commit()
            print("✅ Student record updated.")
    except sqlite3.IntegrityError:
        print(f"❌ Error: '{new_value}' conflicts with an existing record (e.g. duplicate roll no).")
    finally:
        conn.close()
 
 
def delete_student(student_id):
    conn = get_connection()
    cursor = conn.execute("DELETE FROM students WHERE student_id = ?", (student_id,))
    conn.commit()
    conn.close()
    if cursor.rowcount == 0:
        print("❌ No student found with that ID.")
    else:
        print("✅ Student (and their attendance/grades) deleted.")
 
 
def search_students(keyword):
    conn = get_connection()
    like = f"%{keyword}%"
    rows = conn.execute(
        "SELECT * FROM students WHERE name LIKE ? OR roll_no LIKE ? OR class_name LIKE ?",
        (like, like, like),
    ).fetchall()
    conn.close()
 
    if not rows:
        print("No matching students found.")
        return
 
    print(f"\n{'ID':<5}{'Name':<20}{'Roll No':<10}{'Class':<10}")
    print("-" * 45)
    for r in rows:
        print(f"{r['student_id']:<5}{r['name']:<20}{r['roll_no']:<10}{r['class_name']:<10}")
 
 
# ---------------------------------------------------------------------------
# ATTENDANCE
# ---------------------------------------------------------------------------
 
def mark_attendance(student_id, date, status):
    status = status.strip().capitalize()
    if status not in ("Present", "Absent"):
        print("❌ Status must be 'Present' or 'Absent'.")
        return
 
    conn = get_connection()
    try:
        conn.execute(
            "INSERT INTO attendance (student_id, date, status) VALUES (?, ?, ?) "
            "ON CONFLICT(student_id, date) DO UPDATE SET status = excluded.status",
            (student_id, date, status),
        )
        conn.commit()
        print(f"✅ Attendance marked: {status} on {date}.")
    except sqlite3.IntegrityError as e:
        print(f"❌ Error: {e}")
    finally:
        conn.close()
 
 
def view_attendance(student_id):
    conn = get_connection()
    rows = conn.execute(
        "SELECT date, status FROM attendance WHERE student_id = ? ORDER BY date",
        (student_id,),
    ).fetchall()
    conn.close()
 
    if not rows:
        print("No attendance records found.")
        return
 
    print(f"\n{'Date':<15}{'Status':<10}")
    print("-" * 25)
    for r in rows:
        print(f"{r['date']:<15}{r['status']:<10}")
 
 
def attendance_report(student_id):
    conn = get_connection()
    total = conn.execute(
        "SELECT COUNT(*) AS c FROM attendance WHERE student_id = ?", (student_id,)
    ).fetchone()["c"]
    present = conn.execute(
        "SELECT COUNT(*) AS c FROM attendance WHERE student_id = ? AND status = 'Present'",
        (student_id,),
    ).fetchone()["c"]
    conn.close()
 
    if total == 0:
        print("No attendance records found.")
        return
 
    percentage = (present / total) * 100
    print(f"Total days recorded: {total}")
    print(f"Present: {present}  |  Absent: {total - present}")
    print(f"Attendance percentage: {percentage:.2f}%")
 
 
# ---------------------------------------------------------------------------
# GRADES
# ---------------------------------------------------------------------------
 
def add_grade(student_id, subject, exam_type, marks, max_marks=100):
    conn = get_connection()
    try:
        conn.execute(
            "INSERT INTO grades (student_id, subject, exam_type, marks, max_marks) "
            "VALUES (?, ?, ?, ?, ?)",
            (student_id, subject, exam_type, marks, max_marks),
        )
        conn.commit()
        print(f"✅ Grade recorded: {subject} ({exam_type}) - {marks}/{max_marks}")
    except sqlite3.IntegrityError:
        print(f"❌ Error: No student found with ID '{student_id}'. "
              f"Use 'View All Students' to check the correct ID first.")
    finally:
        conn.close()
 
 
def view_grades(student_id):
    conn = get_connection()
    rows = conn.execute(
        "SELECT subject, exam_type, marks, max_marks FROM grades WHERE student_id = ?",
        (student_id,),
    ).fetchall()
    conn.close()
 
    if not rows:
        print("No grade records found.")
        return
 
    print(f"\n{'Subject':<15}{'Exam':<12}{'Marks':<10}{'Max':<8}{'%':<8}")
    print("-" * 53)
    for r in rows:
        pct = (r["marks"] / r["max_marks"]) * 100
        print(f"{r['subject']:<15}{r['exam_type']:<12}{r['marks']:<10}{r['max_marks']:<8}{pct:<8.1f}")
 
 
def grade_report(student_id):
    conn = get_connection()
    rows = conn.execute(
        "SELECT marks, max_marks FROM grades WHERE student_id = ?", (student_id,)
    ).fetchall()
    conn.close()
 
    if not rows:
        print("No grade records found.")
        return
 
    total_marks = sum(r["marks"] for r in rows)
    total_max = sum(r["max_marks"] for r in rows)
    average_pct = (total_marks / total_max) * 100
 
    print(f"Subjects recorded: {len(rows)}")
    print(f"Total: {total_marks:.1f} / {total_max:.1f}")
    print(f"Overall average: {average_pct:.2f}%")
 
    if average_pct >= 90:
        grade_letter = "A+"
    elif average_pct >= 75:
        grade_letter = "A"
    elif average_pct >= 60:
        grade_letter = "B"
    elif average_pct >= 40:
        grade_letter = "C"
    else:
        grade_letter = "F"
    print(f"Grade: {grade_letter}")
 
 
# ---------------------------------------------------------------------------
# CLASS-WIDE REPORTS
# ---------------------------------------------------------------------------
 
def class_average_report(class_name):
    conn = get_connection()
    rows = conn.execute(
        """
        SELECT s.name, AVG(g.marks * 100.0 / g.max_marks) AS avg_pct
        FROM students s
        JOIN grades g ON g.student_id = s.student_id
        WHERE s.class_name = ?
        GROUP BY s.student_id
        ORDER BY avg_pct DESC
        """,
        (class_name,),
    ).fetchall()
    conn.close()
 
    if not rows:
        print(f"No grade data found for class '{class_name}'.")
        return
 
    print(f"\nClass Performance Report — {class_name}")
    print(f"{'Rank':<6}{'Name':<20}{'Average %':<10}")
    print("-" * 36)
    for i, r in enumerate(rows, start=1):
        print(f"{i:<6}{r['name']:<20}{r['avg_pct']:<10.2f}")
 
