def name():
    print("Dibash")
name()

def add(a , b):
    return a + b
result = add(1,2)
print(result)

def check(a):
    if a % 2 == 0:
        print(f"{a} is Even number")
    else:
        print(f"{a} is Odd number")
a = int(input("enter a number: "))
check(a)