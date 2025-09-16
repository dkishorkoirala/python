import numpy as np

B = np.array([[4, 1, 0], [0, 5, 2], [7, 0, 6]])

Diagonal_elements = np.diag(B)
print("Diagonal elements:\n", Diagonal_elements)

trace_ = np.trace(B)
print("\nTrace of B:\n", trace_)
