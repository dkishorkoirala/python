#personalized Greeting App
uname = input("Enter your name: ")
uage = int(input("Enter your age: "))

print (f"Hello, {uname}! You are {uage} years old!")

#simple calculator
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(f"The sum of {a} and {b} is {a + b}")
print(f"The difference of {a} and {b} is {a - b}")
print(f"The product of {a} and {b} is {a * b}")
print(f"The quotient of {a} and {b} is {a / b}")

#future age predictor
age = int(input("Enter your current age: "))

print(f"Your current is {age} years,\nAfter 5 years you will be {age + 5} years,\nAfter 10 years you will be {age + 10} years, and \nafter 20 years you will be {age + 20} years.")

#area of rectangle
l = int(input("Enter length of rectangle: "))
b = int(input("Enter breadth of Width: "))

print(f"The area of rectangle is {l * b} square units")

#temperature converter
c = int(input("Enter temperature in Celsius: "))

print(f"The temperature in Fahrenheit is {c * 9 / 5 + 32} degrees")

#name reverse
name = input("Enter your name: ")
print(f"Your name in reverse is {name[::-1]}")

#simple interest calculator
p = int(input("Enter principal amount: "))
r = int(input("Enter rate of interest: "))
t = int(input("Enter time period: "))
print(f"The simple interest is {p * r * t / 100}")

#shopping cart total
item1 = int(input("Enter price of item 1: "))
item2 = int(input("Enter price of item 2: "))
item3 = int(input("Enter price of item 3: "))

print (f"The total cost of items is {item1 + item2 + item3}")

#word repeater
word = input("Enter a word: ")
num = int(input("Enter a number"))

print((" " + word) * num)

#biocard generator
cname= input("Enter your name : ")
cage = int(input("Enter your age: "))
chobby = input("Enter your hobby: ")
ccolor= input("Enter your favourite color: ")

print(f"Name: {cname}\nAge: {cage}\nHobby: {chobby}\nFavourite Colour: {ccolor}")
