import numpy as np

arr = np.array([[2, 7, 3], [5, 1, 9], [8, 6, 4]])

print("Original array:\n", arr)

print("Row-wise min values:\n", np.min(arr, axis=1))
print("Column-wise max value:\n", np.max(arr, axis=0))
