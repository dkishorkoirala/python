print("task 1")
def greet(name):
    def inner():
        print(f"Hello from inside: {name}")
    inner()
greet("Dibash")

print("\ntask 2")
def make_multiplier(n):
    def inner(x):
        return n * x
    return inner  

times3 = make_multiplier(3)
print(times3(5)) 


print("\ntask 3")
def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    inner()
    inner()
    inner()
    print("The final value is", count)

outer()

print("\ntask 4")
def msg():
    message = "Hello"
    def inner():
        nonlocal message 
        message = input("Enter any message: ")
        print("The message from inside:", message)
    inner()
    
    print("The message from outeside:", message)
msg()

print("\ntask 5")
def outer(string):
    def inner():
        return string.upper()      
    result = inner()
    print(result)
outer("AbcDEfGhIj")

print("\nchallenge 1")
def power(base):
    def inner(expo):
        return base ** expo
    return inner

power_of_2 = power(2)
print(power_of_2(3))


print("\nchallenge 2")
def counter_maker():
    counter = 0
    def maker():
        nonlocal counter
        counter += 1
        return counter
    return maker

count = counter_maker()
print(count())  
print(count())  
print(count())

print("\nchallenge 3")
def nested_calculator(a, b):

    def add():
        return a + b
    def sub(): return a - b 
    def mul(): return a * b 
    def div():
        if b ==0 :
            return f"Not divisible by zero"
        return a /b 
    print(f"Addition is {add()}\nSubtraction is {sub()}\n Multiplication is {mul()} and\nDivision is {div()}\nFor the given numbers")
nested_calculator(10, 2)

print("\nchallenge 4")
def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner
counter = outer()
print(counter())  
print(counter())  
print(counter())