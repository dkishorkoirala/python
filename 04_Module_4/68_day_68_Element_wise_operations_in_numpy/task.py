import numpy as np

# task 1

arr1 = np.array([2, 4, 6, 8])
arr2 = np.array([1, 3, 5, 7])

print("Addition:", arr1 + arr2)
print("Subtraction:", arr1 - arr2)
print("Multiplication:", arr1 * arr2)
print("Division:", arr1 / arr2)
print("Modulus:", arr1 % arr2)
print("Power:", arr1**arr2)

# task 2
print("Greater than:", arr1 > arr2)
print("Less than:", arr1 < arr2)
print("Equal to:", arr1 == arr2)
print("Not equal", arr1 != arr2)


# task 3
mat = np.array([[1, 2, 3], [4, 5, 6]])
vec = np.array([1, 1, 1])

print("Broadcasting subtraction:", mat - vec)

# task 4
arr = np.array([1, 2, 3])
print(arr * 5)
