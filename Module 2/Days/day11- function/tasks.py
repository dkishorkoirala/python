print("task 1 print v/s return")

def double_number_print(n):
    print(n *n )

def double_number_return(x):
    return x * x

print("of Return")
result_return = double_number_return(5)
print(result_return)
print(double_number_return(10))
print(double_number_return(21))
print("\nOF PRINT")
result_print = double_number_print(10)
print(result_print)
print(double_number_print(5))
print(double_number_print(21))

print("\n\ntask 2 lambda function practice")

add10 = lambda x : x + 10
print(add10(int(input("Enter the number to add 10: "))))

multiply= lambda a,b: a *b 
a = int(input("Enter the first number to multiply: "))
b = int(input("Enter the second number to multiply: "))
print(multiply(a ,b))

greater_than_50= lambda x : x > 50
print(greater_than_50(int(input("Enter the number: "))))

print("task 3 smart lambda calculator")
operation= {
    'add' : lambda a, b: a+b,
    'sub' : lambda a, b: a-b,
    'mul' : lambda a,b : a*b,
    'div' : lambda a, b: a/b if b != 0 else "Error"
}
op = input("Enter operation (add/sub/mul/div): ").lower()
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if op in operation:
    print("result: ", operation[op](a, b))
else:
    print("Invalid operation")

print("scope checker")
count = 0
def increment():
    global count
    count += 1
    print(count)
increment()
increment()
increment()
print(count)
def smart_calc(op, a, b):
    operations = {
        'add': lambda a, b: a + b,
        'sub': lambda a, b: a - b,
        'mul': lambda a, b: a * b,
        'div': lambda a, b: a / b if b != 0 else "Error: Division by zero"
    }
    return operations[op](a, b) if op in operations else "Invalid operation"

op = input("Enter operation (add/sub/mul/div): ").lower()
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
result = smart_calc(op, a, b)
print("Final Answer:", result)

