import numpy as np

C = np.array([[3, -2], [1, 0]])

print("Original Matrix:\n", C)
det = np.linalg.det(C)
print("Determinant of matrix C:\n", det)

# eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(C)
print("\nEigenvalues:\n", eigenvalues)
print("\nEigenvectors (columns):\n", eigenvectors)
