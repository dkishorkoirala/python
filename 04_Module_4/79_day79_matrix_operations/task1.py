import numpy as np

Identity_matrix = np.identity(4)

print("The identity matrix of 4x4:\n", Identity_matrix)

A = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])

print("\nOriginal Matrix A:\n", A)
result = np.dot(A, Identity_matrix)
print("\nResult of A x Identity_matrix:\n", result)
