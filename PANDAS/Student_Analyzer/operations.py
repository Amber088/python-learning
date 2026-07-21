import pandas as pd

# Read CSV
students = pd.read_csv("/Users/amberjain/Desktop/Python/PANDAS/Student_Analyzer/Students.csv")


# ---------------- PART 1 ---------------- #

def show_dataset():
    print("\n===== COMPLETE DATASET =====")
    print(students)


def show_shape():
    print("\n===== DATASET SHAPE =====")
    print("Rows :", students.shape[0])
    print("Columns :", students.shape[1])


def show_columns():
    print("\n===== COLUMN NAMES =====")
    for column in students.columns:
        print(column)


def show_first_five():
    print("\n===== FIRST FIVE STUDENTS =====")
    print(students.head())


def show_last_five():
    print("\n===== LAST FIVE STUDENTS =====")
    print(students.tail())


def show_info():
    print("\n===== DATASET INFO =====")
    students.info()


def show_statistics():
    print("\n===== STATISTICS =====")
    print(students.describe())


# ---------------- PART 2 ---------------- #

def calculate_total():

    students["Total"] = (
        students["Maths"] +
        students["Physics"] +
        students["Chemistry"]
    )

    print("\n===== TOTAL MARKS =====")
    print(students[["Name", "Total"]])


def calculate_average():

    if "Total" not in students.columns:
        calculate_total()

    students["Average"] = students["Total"] / 3

    print("\n===== AVERAGE MARKS =====")
    print(students[["Name", "Average"]])


def assign_grade():

    if "Average" not in students.columns:
        calculate_average()

    def grade(avg):

        if avg >= 90:
            return "A"

        elif avg >= 80:
            return "B"

        elif avg >= 70:
            return "C"

        elif avg >= 60:
            return "D"

        else:
            return "F"

    students["Grade"] = students["Average"].apply(grade)

    print("\n===== STUDENT GRADES =====")
    print(students[["Name", "Average", "Grade"]])


def show_topper():

    if "Average" not in students.columns:
        calculate_average()

    topper = students.sort_values("Average", ascending=False).iloc[0]

    print("\n===== TOPPER =====")
    print("Name :", topper["Name"])
    print("Average :", topper["Average"])


def show_lowest():

    if "Average" not in students.columns:
        calculate_average()

    lowest = students.sort_values("Average").iloc[0]

    print("\n===== LOWEST SCORER =====")
    print("Name :", lowest["Name"])
    print("Average :", lowest["Average"])


def above_80():

    if "Average" not in students.columns:
        calculate_average()

    print("\n===== STUDENTS ABOVE 80% =====")
    print(students[students["Average"] >= 80][["Name", "Average"]])


def sort_average():

    if "Average" not in students.columns:
        calculate_average()

    print("\n===== SORTED BY AVERAGE =====")
    print(
        students.sort_values(
            by="Average",
            ascending=False
        )[["Name", "Average"]]
    )


def save_csv():

    students.to_csv("updated_students.csv", index=False)

    print("\n✅ updated_students.csv saved successfully.")