print("mini task 1")
try:
    num = int(input("Enter any number to divide to 100: "))
    print(100/num)
except ZeroDivisionError:
    print("Number cannot be zero")

print("\nmini task 2")
try:
    num2 = int(input("Enter a number: "))
    print("You typed",num2)
except ValueError:
    print("It must be number...")

print("\nmini task 3")
try:
    num = int(input("Enter any number: "))
    print("Your calculation:",50/num)
except ZeroDivisionError:
    print("Number cannot be zero")
except ValueError:
    print("Number must be number not alphabet")