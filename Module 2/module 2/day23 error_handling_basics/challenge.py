def calculator(a,b,op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b 
    elif op == "/":
       return a /b
    else:
        return "sorry something went wrong"

try:   
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Enter the operation to perform(+,-,*,/): ")

    result = calculator(num1,num2,op)
    print("Result:",result )
except ValueError:
    print("numbers must be numbers and operation must be selected within the included")
except ZeroDivisionError:
    print("Cannot be divided by zero")
except:
    print("something went wrong...")
