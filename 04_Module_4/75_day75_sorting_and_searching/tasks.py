import numpy as np

# task 1

arr = np.array([12, 5, 8, 15, 3])
print("Original array:\n", arr)
print("\nSorted array:\n", np.sort(arr))
print("\nOriginal indices:\n", np.argsort(arr))

# task 2
mat = np.array([[5, 2, 8], [1, 7, 3]])
print("\nOriginal matrix:\n", mat)
print("Row-wise sort:\n", np.sort(mat, axis=1))
print("Column-wise sort:\n", np.sort(mat, axis=0))

# task 3

arr = np.array([11, 22, 33, 44, 55])

print("Original array:\n", arr)
print("Indices of number greater than 30:\n", np.where(arr > 30))
print("Value greater than 30:\n", arr[np.where(arr > 30)])

# task 4
arr = np.array([10, 20, 30, 40])
print("Original array:\n", arr)
print("Insert 25 at index:", np.searchsorted(arr, 25))
print("Insert 35 at index:", np.searchsorted(arr, 35))
