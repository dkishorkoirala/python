#report card generator:
def calculate_grade(avg):
    if avg >= 90:
        return "Excellent"
    elif avg >= 75:
        return "Good"
    else:
        return "Needs Improvement"

def report_card(student):
    print(f"\nStudent: {student['name']}")
    total = 0
    for subject, mark in student["marks"].items():
        print(f"{subject}: {mark}")
        total += mark
    avg = total / len(student["marks"])
    grade = calculate_grade(avg)
    print(f"Average: {avg:.2f}")
    print(f"Grade: {grade}")


students =[]

n = int(input("Enter the number of students: "))
for i in range(n):
    name = input("Enter student name: ")

    subjects = ["Math", "Nepali", "English"]

    marks= {}

    for subject in subjects:
        score = int(input("Enter marks of {subject}: "))
        marks[subject] = score
    students.append({"name": name, "marks": marks})

for student in students:
    report_card(student)