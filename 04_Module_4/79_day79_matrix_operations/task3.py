import numpy as np

C = np.array([[2, 3], [4, 6]])

rank_ = np.linalg.matrix_rank(C)
print("Original Matrix:\n", C)
print("\nRank of C:\n", rank_)
