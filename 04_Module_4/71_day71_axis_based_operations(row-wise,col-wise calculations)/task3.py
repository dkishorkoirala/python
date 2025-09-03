import numpy as np

matrix = np.random.randint(1, 51, (4, 5))

print("Original matrix:\n", matrix)
print("Row-wise standard deviation:\n", np.std(matrix, axis=1))

print("Column-wise variance:\n", np.var(matrix, axis=0))
