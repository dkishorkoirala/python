import numpy as np

# task 1
arr = np.array([0, np.pi / 6, np.pi / 4, np.pi / 3, np.pi / 2])
print("sin:", np.sin(arr))
print("cos:", np.cos(arr))
print("tan:", np.tan(arr))
print()

# task 2
arr = np.arange(1, 11)
print(np.cumprod(arr))

# task 3
a = np.array([1, 2, 3, 44])
b = np.array([10, 2, 30, 40])

print("Greater:", np.greater(a, b))
print("Equal:", np.equal(a, b))

# task 4
arr = np.array([3.14, 7.89, -4.56])
frac, whole = np.modf(arr)
print("Fractional parts:", frac)
print("Whole parts:", whole)
