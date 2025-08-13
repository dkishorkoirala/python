print("Challenge 1")
student= {
    "Name": "John",
    "Age": 20,
    "subject": "Math"
}
for key, value in student.items():
    print(f"{key} : {value}")

print("\nChallenge 2")
inventory={
    "pen" : 10,
    "notebook": 5,
    "pencil": 7
}
for item, quantity in inventory.items():
    print(f"{item}: {quantity}")

print("\nchallenge 3")
student = {
    "name": "Dibash",
    "marks" : [80, 90, 85]
}

for name, marks in student.items():
    if name == "marks":
        for mark in value:
            print(mark)

print("\nChallenge 4")


sentence = "AI is the future and AI is powerful"
words = sentence.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

for word, count in word_count.items():
    print(f"{word}: {count}")

print("\nChallenge 5")
students={
    "arya": {"math": 90, "science": 85},
    "jon": {"math": 75,"science": 95},
}

for name , subject in students.items():
    total = sum(subject.values())
    avg = total/ len(subject)
    print(f"{name}-> Average: {avg}")

print("\nChallenge 6")
menu = {
    "Burger": 120,
    "Pizza": 250,
    "Fries": 90
}

item = input("Enter the item you want to order: ").capitalize()
if item in menu:
    print(f"Price of {item}: {menu[item]}")
else:
    print(f"{item} is not available")