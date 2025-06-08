def calculate_grade(avg):
    if avg >= 90:
        return "Excelent"
    elif avg >= 75:
        return "Good"
    else:
        return "Needs improvement"

def report_card(student):
    print(f"\nstudent: {student['name']}")
    total = 0
    for subject, mark in student["marks"].items():
        print(f"{subject.capitalize()}: {mark}")
        total += mark
    
    avg = total / len(student["marks"])
    grade = calculate_grade(avg)
    print(f"Average: {avg:.2f}")
    print(f"Grade: {grade}\n")

students = []
n = int (input("Enter the number of students: "))

for i in range(n):
    name = input("Enter the name of student: ")
    subjects = ["English", "Nepali", "Math","science"]
    marks = {}
    for subject in subjects:
        score = int(input(f"Enter the marks for {subject}: "))
        marks[subject] = score
    
    students.append({"name": name, "marks": marks})

print("\n-----------Generating Report-----------")
for student in students:
    report_card(student)