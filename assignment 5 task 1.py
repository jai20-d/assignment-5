import re

students = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78
}

name = input("Enter the student's name: ")

pattern = re.compile(name, re.IGNORECASE)

found = False
for student in students:
    if re.fullmatch(pattern, student):
        print(f"{student}'s marks: {students[student]}")
        found = True
        break

if not found:
    print("Student not found.")
