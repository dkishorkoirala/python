print("-----Task1-----")
student = {
    "name" : "Krishna",
    "age" : 20,
    "grade" : "A"
}

print(student)

print("\n-----task2-----")

print(student["grade"])

print("\n-----task3-----")
student["grade"] = "A+"
print(student["grade"])

print("\n-----task4-----")
student["school"] = "XYZ School"
print(student)

print("\n-----task5-----")
del student["age"]
print(student)

print("\n-----task6-----")
for key in student:
    print(key)

print("\n-----task7-----")
for key in student:
    print(student[key])

print("\n-----task8-----")
friends = []

for key in range(3):
    name = input("enter friend's name: ")
    color = input("enter Favourite color: ")
    friend ={
        "name": name,
        "color": color
    }
    friends.append(friend)

print(friends)

print("\n-----task9-----")
print(friend.get("age", "Not found!!!"))

print("\n-----task10-----")
stus = []

for key in range (2):
    sname = input("enter student name: ")
    score = int(input("enter student's subject score:"))
    stu={
        "name": sname,
        "score": score
    }
    stus.append(stu)

print(stus)

print("\n-----Challenge Project-----")
students = {}

for i in range(3):
    name = input(f"enter student's name {i+1}:")
    age = int(input(f"Enter {name} age:"))
    score = int(input(f"Enter {name} score:"))
    students[name] = {
        "age" : age,
        "score" : score
    }
    

print(students)

for name, info in students.items():
    print(f"{name} scored {info['score']} points.")

print("----challenge2------")
items = {}
t_price = 0
for i in range(3):
    name = input(f"Enter {i+1} item name: ")
    price = int(input(f"Enter {name} price: "))

    t_price += price
    items[name] = price

print(items)

for name, price in items.items():
    print(f"{name} costs {price} dollars.")

print("Total price is :",t_price)
print(f"The average price is: {t_price/3:.2f}")