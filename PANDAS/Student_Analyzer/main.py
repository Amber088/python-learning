from operations import *

while True:

    print("\n" + "=" * 50)
    print("      STUDENT PERFORMANCE ANALYZER")
    print("=" * 50)

    print("""
1. Show Complete Dataset
2. Show Dataset Shape
3. Show Column Names
4. Show First 5 Students
5. Show Last 5 Students
6. Dataset Information
7. Statistical Summary

--------------- ANALYSIS ----------------

8. Calculate Total Marks
9. Calculate Average Marks
10. Assign Grades
11. Show Topper
12. Show Lowest Scorer
13. Show Students Above 80%
14. Sort by Average Marks
15. Save Updated CSV

16. Exit
""")

    choice = input("Enter Your Choice : ")

    if choice == "1":
        show_dataset()

    elif choice == "2":
        show_shape()

    elif choice == "3":
        show_columns()

    elif choice == "4":
        show_first_five()

    elif choice == "5":
        show_last_five()

    elif choice == "6":
        show_info()

    elif choice == "7":
        show_statistics()

    elif choice == "8":
        calculate_total()

    elif choice == "9":
        calculate_average()

    elif choice == "10":
        assign_grade()

    elif choice == "11":
        show_topper()

    elif choice == "12":
        show_lowest()

    elif choice == "13":
        above_80()

    elif choice == "14":
        sort_average()

    elif choice == "15":
        save_csv()

    elif choice == "16":
        print("\nThank You for using Student Performance Analyzer ❤️")
        break

    else:
        print("\n❌ Invalid Choice! Please Try Again.")
        