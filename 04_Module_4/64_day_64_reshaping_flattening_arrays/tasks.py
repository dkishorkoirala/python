import numpy as np

"""Task 1"""
arr = np.arange(1, 17)
print(arr)
reshaped = arr.reshape(4, -1)
print(reshaped)

"""task2"""
arr2 = np.arange(1, 21).reshape(5, -1)
print(arr2)

"""Task 3"""
mat = np.arange(1, 10).reshape(3, 3)
print(mat)

flat1 = mat.flatten()
print(flat1)

flat2 = mat.ravel()
print(flat2)
