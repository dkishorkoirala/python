import json

try:
    with open("students.json", "r") as f:
        students = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    students = []

while True:
    print("\nMenu")
    print("1. Add New Student\n2. View all students\n3. Search Student by Name\n4. Exit")

    try:
        choice = int(input("Enter Your choice(1-4): "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    if choice == 1:
        id = input("enter student id: ")
        name = input("Enter Student name: ")
        age = input("Enter student age: ")
        grade = input("Enter student Grade: ")

        students.append({
            "id": id,
            "name": name,
            "age" : age,
            "grade" : grade 
        })

        with open("students.json", "w") as wf:
            json.dump(students, wf)
        print("\nStudent added successfully!!!")

    elif choice == 2:
        if not students:
            print("\nNo student record found.")
        else: 
            print("\nAll Student Records:")
            for student in students:
                print(f"ID: {student['id']} \nName: {student['name']}\nAge: {student['age']}\nGrade: {student['grade']}\n")

    elif choice == 3:
        search_name = input("\nEnter student name to search: ")
        found = False
        for student in students:
            if student['name'].lower() == search_name.lower():
                print(f"\nStudent Found: \nID: {student['id']} \nName: {student['name']}\nAge: {student['age']}\nGrade: {student['grade']}\n")
                found = True
                break
        if not found:
            print(f"\nNo Student found with that name {search_name}")
            break
    elif choice == 4: 
        print("\nThank you for using the student management system...")
        break
    else:
        print("Invalid choice! Please Try again")