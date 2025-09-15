import numpy as np

B = np.array([[1, 2], [7, 4]])
det = np.linalg.det(B)

print("Original matrix:\n", B)
print("Determinant:\n", det)

B_inv = np.linalg.inv(B)
print("Inverse of B:\n", B_inv)

# check /confirmation
print("B x B_inverse:\n", np.dot(B, B_inv))
