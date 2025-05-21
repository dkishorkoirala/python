#10 mini projects 

#1. even or odd  checker
a = int (input("Enter a number to check whether it's odd or even: "))
if a % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")


# 2. Max of two numbers.
a = int(input("\nEnter the first number to compare: "))
b = int(input("Enter the second number to compare: "))

if a > b :
    print(f"In these two number {a} and {b}, the larger number is {a}")
elif b > a :
    print(f"In these two number {a} and {b}, the larger number is {b}")

else:
    print(f"In these two number {a} and {b}, the numbers are equal")

#3. simple Grading System
marks = int(input("\nEnter your marks: "))
if marks >= 90:
    print("Grade: A")
elif 80 <= marks <= 89:
    print("Grade: B")
elif 70 <= marks <= 79:
    print("Grade: C")
else:
    print("Grade: D")

#4. Simple calculator
num1 = int(input("\nEnter the first number for calculations: "))
num2 = int(input("Enter the second number for calculations: "))

print(f"Sum: {num1 + num2}")
print(f"Difference: {num1 - num2}")
print(f"Product: {num1 * num2}")
print(f"Quotient: {num1 / num2}")
print(f"Remainder: {num1 % num2}")
print(f"Power: {num1 ** num2}")

#5. Eligibility Checker
age = int(input("\nEnter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not Eligible")

#6. salary bonus calculator
salary = int(input("\nEnter your salary: "))

if salary < 50000:
    bonus = salary * 0.1
    print(f"Total salary is {salary + bonus:.2f}")

else:
    bonus = salary * 0.05
    print(f"Total salary is {salary + bonus:.2f}")

#7. age group classifier:
uage = int(input("\nEnter your age: "))

if uage < 13:
    print("Child")
elif 13 <= uage <= 19:
    print("Teen")
elif 20 <= uage <= 59:
    print("Adult")
else :
    print("Senior")

#8. Bill split calculator
bill = float(input("\nEnter the Total bill amount: "))
num_people = int(input("Enter the number of people: "))

print(f"Amount each person pays {bill / num_people :.2f}")

#9. Temperature Judge
t = float(input("\nEnter the temperature: "))

if t < 0 :
    print("Freezing")
elif 0 <= t <= 20: 
    print("Cold")
elif 21 <= t <= 30:
    print("Moderate")
else: 
    print("Hot")

#10. Logic Gate simulator:
a = int(input("\nEnter the value of A( 0 or 1): "))
b = int(input("\nEnter the value of B(0 or 1): "))

print(f" The result of A and B is {a and b}")
print(f"The result of A or B is {a or b}")
print(f"The result of not A is {not a}")