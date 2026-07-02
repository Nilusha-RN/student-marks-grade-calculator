while True:
    print("\n=== Student Marks Calculator ===")
    print("1. Calculate Student Result")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")

        python_mark = int(input("Enter Python mark: "))
        database_mark = int(input("Enter Database mark: "))
        web_mark = int(input("Enter Web Development mark: "))

        total = python_mark + database_mark + web_mark
        average = total / 3

        if average >= 75:
            grade = "A"
        elif average >= 65:
            grade = "B"
        elif average >= 55:
            grade = "C"
        elif average >= 40:
            grade = "S"
        else:
            grade = "F"

        if python_mark < 40 or database_mark < 40 or web_mark < 40:
            result = "Fail"
        else:
            result = "Pass"

        print("\n--- Student Result ---")
        print("Name:", name)
        print("Total:", total)
        print("Average:", average)
        print("Grade:", grade)
        print("Result:", result)

    elif choice == "2":
        print("Program closed.")
        break

    else:
        print("Invalid choice.")