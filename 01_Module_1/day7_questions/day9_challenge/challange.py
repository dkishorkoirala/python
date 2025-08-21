#project 1: library book Tracker
books = []

for i in range(3):
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    status = input("Enter book status(borrowed/available): ")
    book = {
        "title": title,
        "author": author,
        "status": status
    }
    books.append(book)
print(books)
for book in books:
    if book["status"].lower() == "available":
        print(f"The {book['title']} by {book['author']} is available.")
    else : 
        print("Sorry book is borrowed")

#project 2: Classroom Attendance System.
students = set()

for i in range(5):
    name = input("Enter student name who attended the class: ").lower()
    student = (name)
    students.add(student)

print(students)

uname = input("Enter name for attendance: ").lower()
if uname in students:
    print(f"{uname.capitalize()} is present")
else:
    print(f"{uname.capitalize()} is absent")

#project 3: simple shopping cart
items = []
total = 0
for i in range(3):
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    item = {
        "name": name,
        "price": price
    }
    total += price
    items.append(item)
print(items)
print(f"The Total price of items is: ${total:.2f}")

#Project 4: student search tool
students = []
found = False
for i in range(3):
    name = input("Enter student name: ").lower()
    grade = input("Enter student grade: ").upper()
    student = {
        "name": name,
        "Grade": grade
    }
    students.append(student)

print(students)

search = input("enter name to search: ").lower()
for student in students:
    if student["name"] == search:
        print(f"Name: {student['name'].capitalize()}, Grade: {student['Grade']}.")
        found = True
        break
    else:
        print(f"{search.capitalize()} Not Found.")
        break

#Project 5: Unique Character counter
sen = input("Enter a sentence: ")
unique_chars = set(sen.lower())
print(f"Number of unique characters: {len(unique_chars)}")