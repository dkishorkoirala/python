import numpy as np

M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("Original Matrix:\n", M)

trace_ = np.trace(M)
print("\nThe Trace of M:\n", trace_)

rank_ = np.linalg.matrix_rank(M)
print("\nThe Rank of M:\n", rank_)

diagnol_matrix = np.diag(np.diag(M))
print("\nDiagonal Matrix:\n", diagnol_matrix)

print("\nMultiplication Mxdiagonal_matrix:\n", np.dot(M, diagnol_matrix))
