import numpy as np

arr = np.array([1, np.inf, 2, -np.inf, np.nan, 5])

print(np.isfinite(arr))

extracted_finite = arr[np.isfinite(arr)]
print(extracted_finite)
