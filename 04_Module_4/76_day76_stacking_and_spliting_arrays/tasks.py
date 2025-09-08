import numpy as np

# task 1

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Horizontal stack:", np.hstack((a, b)))
print("Vertical stack:\n", np.vstack((a, b)))

# task 2
x = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print("horizontal split:\n", np.hsplit(x, 2))
print("Vertical split:\n", np.vsplit(x, 2))

# task 3
arr = np.arange(16)
print("Splitted by 4:\n", np.split(arr, 4))
