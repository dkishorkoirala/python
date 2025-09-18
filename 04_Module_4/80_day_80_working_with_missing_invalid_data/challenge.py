import numpy as np

data = np.array([[1, 2, np.nan], [4, np.nan, 6], [7, 8, np.inf]])

print("Original data:\n", data)

for col in range(data.shape[1]):
    column = data[:, col]

    mean_val = np.nanmean(column)
    column[np.isnan(column)] = mean_val

    finite_val = column[np.isfinite(column)]
    max_val = finite_val.max() if finite_val.size > 0 else 0
    column[np.isinf(column)] = max_val

    data[:, col] = column

print("Cleaned data:\n", data)
