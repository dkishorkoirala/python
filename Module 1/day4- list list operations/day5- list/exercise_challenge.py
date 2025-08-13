print("-----task1-----")

lists = [1,2,342,32234,234]
print("Max value is:", max(lists))
print("Min value is ", min(lists))
print("Total value is ", sum(lists))

print("-----task2-----")
students = [
    ["Ram", 20, 90, 23],
    ["Shyam", 21, 85, 23],
]

print("Second student score is", students[1][1], students[1][2], students[1][3])

print("-----task3-----")
fruits=["banana","Apple","apple","mango","orange"]
fruits.sort()
print("Sorted fruit list is:",fruits)

fruits.reverse()
print("Reversed fruit list is:", fruits)

print("-----task4-----")
colors = ["red", "green", "blue", "yellow", "black"]
b = colors.copy()
b.append("RGB")

print("Original list is:", colors)
print("Copied list is:", b)

print("-----task5-----")
evennum = [ x for x in range(1, 11) if x % 2 == 0]

print("Even numbers are:", evennum)

print("-----task6-----")
user = []
for a in range(3):
    uname= input("Enter your name: ")
    uage = int(input("Enter your age: "))
    ucity = input("Enter your city: ")
    user.append([uname, uage, ucity])

print("User details are:", user)

print("-----task7-----")
numbers= [1,2,3,4,5,6,7,8,9,10]
for number in numbers:
    if number % 2 != 0:
        number ** 2
        print("Square of odd numbers are:", number)

print("-----task8-----")
grocery = ["something", "anything", "nothing"]

grocery.sort()
grocery.reverse()
print("Sorted grocery in reverse form list is:", grocery)

print("-----task9-----")
temp = [23,35, 23,23,23]
print("The average of the list is:", sum(temp)/len(temp))

print("-----task10-----")
strings  = []
new_string = []
for i in range(5):
    s = input("Enter your string: ")
    strings.append(s)
    if len(s) >= 3:
        new_string.append(s)

print("The string with more than 3 character is:",new_string)

print("-----challenge-----")
items = []
prices = []
total = 0
for i in range(5):
    item = input("Enter your item: ")
    price = int(input("Enter your price: "))
    items.append(item)
    prices.append(price)
    total += price
for i in range(5):
    print(f"The items with is price is {items[i]}, Rs{prices[i]}")
    i += 1
print("The total price of all items is:", total)
          