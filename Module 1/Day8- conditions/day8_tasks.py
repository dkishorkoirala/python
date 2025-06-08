print("Task 1")
age = int(input("Enter your age: "))

if age < 13:
    print("Child")
elif age <20:
    print("Teenager")
else:
    print("Adult")

print("Task 2")
age = int(input("Enter your age to vote: "))
citizen = input("Are you a citizen? (yes/no): ").lower()

if age >= 18 and citizen == "yes":
    print("You can vote")
else:
    print(f"Sorry not eligible")

print("Task 3")
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
operator = input("Enter what to perform(+, - , * , /): ")

if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second)
elif operator == "*":
    print(first * second)
elif operator == "/":
    print(first / second)
else: 
    print("Invalid operator")
    
print("Student Grader Challenge")
name = input("Enter student's name: ")
marks = int(input("Enter student's marks: "))

if marks >= 90:
    print(f"{name.capitalize()} got A grade")
elif marks >= 80:
    print(f"{name.capitalize()} got B grade")
elif marks >= 70:
    print(f"{name.capitalize()} got C grade")
else :
    print(f"{name.capitalize()} got F grade")

if marks == 100:
    print(f"{name.capitalize()} is Topper.")