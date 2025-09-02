import numpy as np

# task 1
arr = np.arange(1, 11)
sum_ = np.sum(arr)
mean_ = np.mean(arr)
sd_ = np.std(arr)

print("Original array:", arr)
print("Sum:", sum_)
print("Mean:", mean_)
print("Standard Deviation:", sd_)

print()
# task 2
arr = np.array([12, 7, 19, 3, 25, 8])
min_value = np.min(arr)
max_value = np.max(arr)
min_index = np.argmin(arr)
max_index = np.argmax(arr)

print("Original array:", arr)
print("Minimum value:", min_value)
print("Index of minimum value:", min_index)
print("Maximum value:", max_value)
print("Index of maximum value:", max_index)
print()

# task 3
matrix_ = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])

column_wise_mean = np.mean(matrix_, axis=0)
row_wise_sum = np.sum(matrix_, axis=1)

print("Column-wise mean:", column_wise_mean)
print("Row-wise sum:", row_wise_sum)
