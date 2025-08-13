print("mini task 1")
def greet_user():
    def ask_name():
        username = input("Enter the username: ")
        return username
    
    print("hello, ", ask_name())
greet_user()

print("\nmini challenge :calculator")

def calculator():
    x = int(input("Enter first number (greater than second number to prevent from error): "))
    y = int(input("Enter second number: "))

    def add():
        return x + y
    def multiply():
        return x * y
    def sub():
        return x - y
    def div():
        if y == 0:
            return f"the second number cannot be zero"
        else:
            return x / y
    print("The addition of numbers are: ", add())
    print("The multiplication of numbers are : ", multiply())
    print("The substraction of numbers are: " ,sub())
    print("The division of numbers are: ", div())
calculator()

print("\nmini task 1: counter with nested function")
def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        print("Current value of count:", count)
    increment()
    increment()
    increment()
    print("the final value of count is :", count)
make_counter()

print("\ntask 2: nested function with parameter")
def greet(name):
    def get_message():
        msg= input(f"Enter the message: ")
        print(f"Hey {name}\nyour message: {msg}")
    get_message()
greet("Ram")