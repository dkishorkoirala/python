import numpy as np

mat = np.arange(1, 13).reshape(3, 4)

print("Original matrix:\n", mat)
print("Row-wise sum:\n", np.sum(mat, axis=1))
print("Column-wise mean:\n", np.mean(mat, axis=0))
