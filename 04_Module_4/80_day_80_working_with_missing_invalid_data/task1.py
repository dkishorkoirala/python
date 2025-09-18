import numpy as np

arr = np.array([1, 2, np.nan, 4, np.nan])
print(np.isnan(arr))

count = np.isnan(arr).sum()
print(count)
