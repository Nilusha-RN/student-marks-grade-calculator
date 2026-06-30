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

print("\nStudent Name:", name)
print("Total Marks:", total)
print("Average:", average)
print("Grade:", grade)