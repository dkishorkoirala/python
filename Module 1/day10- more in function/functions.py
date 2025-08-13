def multiply(a, b):
    return a * b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
result = multiply(a, b)
print("Result: ", result)

print("\ntask second")

check = lambda x: x % 3 == 0
print(check(int(input("Enter the number to check whether it can be divisible by 3 or not: ")))) 

print("\nThird Task")
def calc_total(scores):
    total = 0
    for score in scores:
        total += score
    return total

def average(scores):

    return calc_total(scores) / len(scores) 

scores = []

n = int(input("Enter the no of list you wanna create: "))
for i in range(n):
    scores.append(int(input("Enter the score: ")))

print("Average: ", average(scores)) 
print("total: ", calc_total(scores))

print("\nFinal assessment")


def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    else:
        return a / b

def choose(operation, a , b):
    if operation == 1:
        return add(a, b)
    elif operation == 2:
        return sub(a, b)
    elif operation == 3:
        return mul(a, b)
    elif operation == 4:
        return div(a, b)
    else:
        return "Invalid operation"
    
while True:
    print("\nChoose your operation")
    print("1. ADD")
    print("2. SUBTRACT")
    print("3. MULTIPLY")
    print("4. DIVIDE")
    print("5. EXIT")
    operation= int(input("Enter your choice: "))

    if operation == 5:
        print("Exiting the Program")
        break
    

    a = int(input("Enter the first number: "))
    b = int(input("Enter second number for operation: "))
    print(choose(operation, a, b))
