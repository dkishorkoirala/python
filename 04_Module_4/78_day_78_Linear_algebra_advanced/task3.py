import numpy as np

D = np.array([[4, 2, 1], [0, 3, -1], [2, 0, 1]])

det = np.linalg.det(D)

print("Original Matrix:\n", D)
print("Determinant of matrix D:\n", det)

if det != 0:
    D_inv = np.linalg.inv(D)
    print("Inverse of D:\n", D_inv)
else:
    print("Matrix D is not invertible.")
