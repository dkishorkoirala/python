import numpy as np

arr = np.array([10, 20, np.nan, 40, 50, np.nan])

mean_val = np.nanmean(arr)
arr[np.isnan(arr)] = mean_val
print(arr)
