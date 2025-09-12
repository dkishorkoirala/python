import numpy as np

# task 1

a = np.array([2, 3, 4])
b = np.array([1, 0, -1])

print("Dot product:\n", np.dot(a, b))

# task 2
X = np.array([[1, 2], [3, 4]])
Y = np.array([[2, 0], [1, 2]])

print("Matrix multiplication:\n", np.matmul(X, Y))
print("Element wise multiplication:\n", X * Y)

# task 3
mat = np.array([[1, 2], [3, 4], [5, 6]])

t_mat = mat.T

print("Original matrix:\n", mat)
print("Transpose:\n", t_mat)
print("Multiplication with transpose:\n", np.matmul(mat, t_mat))
