import numpy as np

mat = np.arange(1, 26).reshape(5, 5)
print("First column:", mat[:, 0])

print("Last row:", mat[-1, :])

print("Middle 3x3 sub-matrix:")
print(mat[1:4, 1:4])
