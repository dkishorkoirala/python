print("Library book tracker")
books = []

for i in range(3):
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    status = input("Enter available/borrowed: ").lower()

    book = {
        "title": title,
        "author": author,
        "status": status
    }
    books.append(book)


for book in books:
    if book["status"] == "available":
        print(f"Book: {book['title']} by {book['author']} is available")
    elif book["status"] == "borrowed":
        print(f"Book: {book['title']} by {book['author']} is borrowed")
    else:
        print("Invalid status")

print("Classroom attendance system")
students = []
for i in range(3):
    name = input("Enter student name: ").lower()

    students.append(name)

student = input("Enter student name to check attendance: ").lower()
if student in students:
    print(f"{student} is present")
else:
    print(f"{student} is absent")

print("Simple shopping cart")
items = []
total = 0

for i in range(3):
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    item = {
        "name": name,
        "price": price
    }
    items.append(item)
    total += price

print(items)
print(f"Total: ${total:.2f}")

print("Student search tool")
students = []
for i in range(3):
    name = input("Enter student name: ").lower()
    grade = input("Enter student grade: ")
    students.append({
        "name": name,
        "grade": grade
        })
name = input("Enter student name to search: ").lower()
found = False
for student in students:
    if student["name"] == name:
        print(f"Student: {student['name']} has grade: {student['grade']}")
        found = True
        break
if not found:
    print(f"Student: {name} not found")

print("Unique character counter")
char= input("Enter a string: ")
unique_chars = set(char.lower().replace(" ", ""))
print(f"Unique characters: {len(unique_chars)}")

print("Student score analyzer")
students= {}
for i in range(3):
    name = input("Enter student name: ").lower()
    subject = {}

    for j in ["math", "science", "english"]:
        score = int(input("enter the score of " + j + ":"))
        subject[j] = score
    students[name] = subject
print(students)

topper = ""
top_avg = 0

for name , score in students.items():
    avg = sum(score.values()) /len (score)
    print(f"{name}'s average score is {avg:.2f}")

    if avg > top_avg:
        top_avg = avg
        topper = name
print(f"\nTopper: {topper} with average score of {top_avg:.2f}")

print("\nAge classification + voting eligibility")
age = int(input("Enter age: "))
citizen = input("Do you have citizenship? ").lower()
if age < 12:
    print("You are a kid")
elif 13 <= age <= 19:
    print("You are teen")
else:
    print("You are adult")

if citizen == "yes" and age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

print("Loop-based tasks")
counter = 10
while counter > 0:
    print(counter)
    counter -= 1

a = 0
b = int(input("enter any number: "))
for i in range(b+1):
    a += i
print("Sum till you entered number is: ", a)

for i in range(1, 6):
    for j in range(1, 11):
        print(f"{i} * {j} = {i*j}", end="\t")

for i in range(10):
    if i % 2 == 0:
        continue
    print(f"odd numbers are :{i}")

password = "1234"
for i in range(3):
    passw = input("enter a password: ")
    if passw == password:
        print("Access granted")
        break
else: 
    print("Access Denied")