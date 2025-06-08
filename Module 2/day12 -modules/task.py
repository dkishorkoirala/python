import random
import math

numbers = random.sample(range(1, 20),3)
print(numbers)

for number in numbers:
    print(f"The square root of {number} numbers is:",math.sqrt(number))

    print(f"The floor of random number {number} is :", math.floor(number))
    print(f"The ceil of random numbers {number} is:",math.ceil(number))
    if number <= 10:
        print(f"Its factorial of {number} is :", math.factorial(number))