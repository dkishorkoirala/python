import numpy as np

mat = np.arange(1, 10).reshape(3, 3)

print("Original matrix:\n", mat)

added_10 = mat + 10
print("Adding 10 to each element:\n", added_10)

vec = np.array([1, 2, 3])
multiplied = added_10 * vec
print("Multiplying with vector:\n", multiplied)

scal = 15

multiplied[multiplied > scal] = 0
print("Checking greater than 15 replaced by zero:\n", multiplied)
