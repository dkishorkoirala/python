from temp_converter import to_celsius, to_farhenheit
from math_utils import power, divide, is_prime

print("Temperature Conversion:")
print("100 Degree Farhenheit to Celsius:", to_celsius(100))
print("0 Degree Celsius to Fahrenheit:", to_farhenheit(0))

print("\nPower Calculator:")
base = int(input("Enter power: "))
exponent = int(input("Enter base number:  "))
power_func = power(base)
print(f"{exponent} raised to {base} is:", power_func(exponent))

print("\nDivision:")
a = int(input("Enter numerator: "))
b = int(input("Enter denominator: "))
print("Result:", divide(a, b))

print("\nPrime Check:")
n = int(input("Enter a number to check if it's prime: "))
print(is_prime(n))
