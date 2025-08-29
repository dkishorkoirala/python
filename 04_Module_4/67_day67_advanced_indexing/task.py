import numpy as np

# task 1
arr = np.arange(1, 21)
print(arr[(arr % 2 == 0) & (arr > 10)])

# task 2
arr = np.array([5, 10, 15, 20, 25, 30])
print(arr[[0, 2, 4]])

# task 3
mat = np.arange(1, 10).reshape(3, 3)
print(mat[[0, 1, 2], [0, 1, 2]])
