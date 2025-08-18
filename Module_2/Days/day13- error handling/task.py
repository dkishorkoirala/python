def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Denominator cannot be zero.")
    return a / b

try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = divide(a, b)
except ValueError:
    print("Both inputs must be valid integers.")
except ZeroDivisionError as e:
    print(f"Error: {e}")
else:
    print(f"Result = {result}")
finally:
    print("Operation complete.")
