import numpy as np

mat = np.arange(1, 25).reshape(6, 4)

print("original matrix:\n", mat)

vertical_split = np.vsplit(mat, 3)
print("Row-wize split:\n", vertical_split)

horizontal_split = np.hsplit(mat, 2)
print("Column-wise split:\n", horizontal_split)

stacked_rows = np.vstack((vertical_split[0], vertical_split[1]))
print("Stacked rows:\n", stacked_rows)

horizontal_stack = np.hstack((horizontal_split[0], horizontal_split[1]))
print("Horizontal stack:\n", horizontal_stack)
