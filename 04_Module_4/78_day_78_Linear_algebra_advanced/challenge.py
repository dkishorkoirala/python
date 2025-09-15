import numpy as np

T = np.array([[2, 1], [1, 3]])
print("Transformation matrix T :\n", T)

eigenvalues, eigenvectors = np.linalg.eig(T)
print("\nEigenvalues:\n", eigenvalues)
print("\nEigenvectors (columns):\n", eigenvectors)

np.random.seed(0)
vectors = np.random.randint(-5, 6, (5, 2))
print("\nOriginal vectors:\n", vectors)

transformed = (T @ vectors.T).T
print("\nTransformed vectors:\n", transformed)

for i in range(eigenvectors.shape[1]):
    v = eigenvectors[:, i]
    lam = eigenvalues[i]
    Tv = T @ v
    print(f"\nCheck for eigenvector {i + 1}:")
    print("v:", v)
    print("T @ v:", Tv)
    print("lam * v:", lam * v)
    print("DO they match?:", np.allclose(Tv, lam * v))
