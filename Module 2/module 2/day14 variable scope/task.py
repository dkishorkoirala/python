print("mini-task 1")
x = 10 
def my_fun():
    x = 5
    print("Inside function:", x)
my_fun()
print("outside function: ", x)

print("\nmini-task 2")

count = 0

def increment():
    global count
    count += 1
    print("Inside:", count)
increment()
print("outside: ",count)

print("\nchallenge 1")
lists = [1, 2,3,4,5]

def fun():
    global lists
    lists.append(6)
    print(lists)
fun()

print("\nchallenge 2")
value = 4

def func():
    global value
    new = value *2
    return new

print(func())
print(value)

print("\nchallenge 3")
x =10
def func1():
    x = 5
    return x

def func2():
    global x
    return x

print("Local variable: ",func1())
print("Global variable:", func2())

print("\nmini task 3")
def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        print("From inner: ",count)
    inner()
    inner()
    print("From outer:",count)
outer()

print("\nchallenge 4")
def f_p(msg):
    x = msg
    def inner():
        nonlocal x
        x = x +" world"
        print("Inner message",x)
    inner()
    print ("The outer message",x)

msg = "Hello"

f_p(msg)

print("\nbonus challenge 1")
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        print("count :", count)
    counter()
    counter()
    counter()

make_counter()

print("\nbonus challenge 2")

def taskes():
    msg = input("Enter a message: ")
    def edit():
        nonlocal msg
        print(msg)
        msg = input("Enter new message the modified one: ")
    edit()
    edit()
    print("the final message is ", msg)
taskes()