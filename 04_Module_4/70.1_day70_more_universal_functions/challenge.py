import numpy as np

mat = np.arange(1, 16).reshape(3, 5)

square_root = np.sqrt(mat)

print("Original matrix:\n", mat)
print("Square root of matrix:\n", square_root)

cum_sum = np.cumsum(square_root)
print("Cumulative sum:", cum_sum)

print("Greater than 5:", mat > 5)

frac, whole = np.modf(cum_sum)
print("Fractional parts:", frac)
print("Whole parts:", whole)
