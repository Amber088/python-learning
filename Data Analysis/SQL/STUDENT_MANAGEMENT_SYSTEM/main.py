from database import initialize_database
import operations as ops


def print_header(title):
    print("\n" + "=" * 45)
    print(title.center(45))
    print("=" * 45)


def main_menu():
    print_header("STUDENT MANAGEMENT SYSTEM")
    print("1. Student Management")
    print("2. Attendance Management")
    print("3. Grade Management")
    print("4. Reports")
    print("5. Exit")
    return input("Select an option: ").strip()


def student_menu():
    print_header("STUDENT MANAGEMENT")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Search Students")
    print("6. Back to Main Menu")
    choice = input("Select an option: ").strip()

    if choice == "1":
        name = input("Name: ").strip()
        roll_no = input("Roll No: ").strip()
        class_name = input("Class: ").strip()
        email = input("Email (optional): ").strip()
        phone = input("Phone (optional): ").strip()
        ops.add_student(name, roll_no, class_name, email, phone)

    elif choice == "2":
        ops.view_all_students()

    elif choice == "3":
        student_id = input("Student ID to update: ").strip()
        field = input("Field to update (name/roll_no/class_name/email/phone): ").strip()
        new_value = input("New value: ").strip()
        ops.update_student(student_id, field, new_value)

    elif choice == "4":
        student_id = input("Student ID to delete: ").strip()
        confirm = input(f"Are you sure you want to delete student {student_id}? (y/n): ").strip().lower()
        if confirm == "y":
            ops.delete_student(student_id)
        else:
            print("Cancelled.")

    elif choice == "5":
        keyword = input("Search by name/roll no/class: ").strip()
        ops.search_students(keyword)

    elif choice == "6":
        return
    else:
        print("❌ Invalid option.")


def attendance_menu():
    print_header("ATTENDANCE MANAGEMENT")
    print("1. Mark Attendance")
    print("2. View Attendance for a Student")
    print("3. Attendance Report (Percentage)")
    print("4. Back to Main Menu")
    choice = input("Select an option: ").strip()

    if choice == "1":
        student_id = input("Student ID: ").strip()
        date = input("Date (YYYY-MM-DD): ").strip()
        status = input("Status (Present/Absent): ").strip()
        ops.mark_attendance(student_id, date, status)

    elif choice == "2":
        student_id = input("Student ID: ").strip()
        ops.view_attendance(student_id)

    elif choice == "3":
        student_id = input("Student ID: ").strip()
        ops.attendance_report(student_id)

    elif choice == "4":
        return
    else:
        print("❌ Invalid option.")


def grade_menu():
    print_header("GRADE MANAGEMENT")
    print("1. Add Grade")
    print("2. View Grades for a Student")
    print("3. Grade Report (Average & Letter Grade)")
    print("4. Back to Main Menu")
    choice = input("Select an option: ").strip()

    if choice == "1":
        student_id = input("Student ID: ").strip()
        subject = input("Subject: ").strip()
        exam_type = input("Exam Type (e.g. Midterm/Final): ").strip()
        marks = float(input("Marks obtained: ").strip())
        max_marks_input = input("Max marks (default 100): ").strip()
        max_marks = float(max_marks_input) if max_marks_input else 100
        ops.add_grade(student_id, subject, exam_type, marks, max_marks)

    elif choice == "2":
        student_id = input("Student ID: ").strip()
        ops.view_grades(student_id)

    elif choice == "3":
        student_id = input("Student ID: ").strip()
        ops.grade_report(student_id)

    elif choice == "4":
        return
    else:
        print("❌ Invalid option.")


def reports_menu():
    print_header("REPORTS")
    print("1. Full Student Profile (Attendance + Grades)")
    print("2. Class-wide Performance Report")
    print("3. Back to Main Menu")
    choice = input("Select an option: ").strip()

    if choice == "1":
        student_id = input("Student ID: ").strip()
        student = ops.get_student_by_id(student_id)
        if not student:
            print("❌ No student found with that ID.")
            return
        print_header(f"PROFILE: {student['name']} ({student['roll_no']})")
        print(f"Class: {student['class_name']}")
        print(f"Email: {student['email'] or '-'}   Phone: {student['phone'] or '-'}")
        print("\n--- Attendance ---")
        ops.attendance_report(student_id)
        print("\n--- Grades ---")
        ops.view_grades(student_id)
        ops.grade_report(student_id)

    elif choice == "2":
        class_name = input("Class name: ").strip()
        ops.class_average_report(class_name)

    elif choice == "3":
        return
    else:
        print("❌ Invalid option.")


def run():
    initialize_database()
    while True:
        choice = main_menu()
        if choice == "1":
            student_menu()
        elif choice == "2":
            attendance_menu()
        elif choice == "3":
            grade_menu()
        elif choice == "4":
            reports_menu()
        elif choice == "5":
            print("\nGoodbye! 👋")
            break
        else:
            print("❌ Invalid option. Please choose 1-5.")


if __name__ == "__main__":
    run()

