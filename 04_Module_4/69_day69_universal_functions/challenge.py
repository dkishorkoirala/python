import numpy as np

arr = np.arange(1, 21)

print("Original array:", arr)
out_used = np.empty_like(arr)
np.multiply(arr, 2, out=out_used)
print("Multiplication by 2 using out:", out_used)

log_base_10 = np.log10(out_used)
print("Logarithm base 10:", log_base_10)


result = np.where(log_base_10 < 1, 0, log_base_10)

print("Final after replacement (less than 1 with 0) array:", result)
