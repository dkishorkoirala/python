import numpy as np

arr = np.array([1, 2, 3, 4, 5])

add = np.add(arr, 100)
square_root = np.sqrt(add)
power = np.power(square_root, 3)
sine_values = np.sin(power)

print("Original array:", arr)
print("Array after adding 100:", add)
print("Array after taking square root of added one:", square_root)
print("Array after raising to power 3 to square rooted array:", power)
print("Array after taking sine of powered array:", sine_values)

# task 2

print(np.exp(arr))
print(np.log(arr))

# task 3
result = np.where(arr % 2 == 0, arr, -1)
print(result)
