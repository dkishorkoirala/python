#Task 1: Arithmetic Practice

a = int (input("Enter First number: "))
b = int (input("Enter Second number: "))

print(f"The sum of two number is {a+b},")
print(f"The difference of two number is {a-b},")
print(f"The product of two number is {a*b},")
print(f"The remainder of two number is {a % b},")
print(f"The power of two number is {a **b},")

#task 2: Comparison Tester
c = int(input("\nEnter first number: "))
d = int(input("Enter second number: "))

if c > d :
    print(f"Number : {c} is greater than, Number {d}")
elif c == d:
    print(f"Number : {c} is equal to, Number {d}")
else :
    print(f"Number : {c} is smaller than, Number {d}")

#task 3: Logic tester
uage = int(input("\nEnter your age: "))

if uage >= 18  and uage <= 59:
    print(f"Eligible Adult")
else:
    print(f"Minor or a senior.")

#mini project
#1. even or odd checker
num = int(input("\nEnter a number: "))

if num % 2 == 0:
    print(f"Number {num} is even")

else:
    print(f"Number {num} is odd")

#2. Grading system
marks = int(input("\nEnter your marks: "))

if marks >= 90:
    print(f"Grade A")

elif marks >= 80 and marks <= 89:
    print(f"Grade B")

elif marks >= 70 and marks <= 79:
    print(f"Grade C")

else :
    print(f"Grade D")

#3. salary and bonus calculator
salary = int(input("\nEnter your basic salary: "))

if salary < 50000:
    bonus = salary * 0.1
    print(f"Bonus amount is {bonus:.2f} and Updated salary is {salary + bonus:.2f}")

else:
    bonus = salary * 0.05
    print(f"Bonus amount is {bonus:.2f} and Updated salary is {salary + bonus:.2f}")

#challenge of the day: Simple logic gate simulator

x = int(input ("\nEnter first binary number(o or 1): "))
y = int(input("Enter second binary number(o or 1): "))

if x in [0, 1] and y in [0, 1]:
    print(f"AND: {x and y}")
    print(f"OR: {x or y}")
    print(f"NOT (first): {not x}")
else:
    print("Please enter valid binary values (0 or 1)")
