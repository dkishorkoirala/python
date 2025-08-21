# challenge 1:student filter(list of dictionaries)
students = []

for i in range(3):
    name = input("Enter student name: ")
    score = int(input("Enter score:"))
    student={
        "name": name,
        "score": score
    }
    students.append(student)
print(students)

for score in students:
    if score["score"] > 80:
        print(f"{score['name']} has a score of {score['score']}")

#challenge2: Unique words (using set)
sentence = input("Enter a sentence: ")
words = set(sentence.split())
print(words)
print("There are",len(words), "unique words")

# Challenge 3: product billing system(using dictionary)
product= {}
total=0
for i in range(3):
    name = input("Enter product name: ")
    price = int(input("Enter price: "))
    product[name] = price
    total += price
print(product)
print("The total price of provided products is:",total)
print("The average price of provided products is:",total/len(product))

# challenge 4: Tulple slicing

numbers = (10, 20, 30, 40, 50, 60)
print(numbers[0:3])
print(numbers[4:6])
print(numbers[2:4])

# challenge 5: Dictionary search
student_db= []

for i in range(3):
    name = input("Enter student name: ")
    score = int(input("Enter score:"))
    student={
        "name": name,
        "score": score
    }
    student_db.append(student)

sname = input("Enter student name to search: ")
found = False

for student in student_db:
    if student["name"].lower() == sname.lower():
        print(f"{student['name']}'s grade is {student['score']}")
        found = True
        break
    else:
        print(f"Student {sname} not found")