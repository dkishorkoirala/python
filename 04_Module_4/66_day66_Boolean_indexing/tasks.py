import numpy as np

# task1
arr = np.arange(1, 21)
print(arr[(arr % 3 == 0)])

# task 2
new_arr = np.array([15, 22, 8, 19, 31, 42, 7])

print(new_arr[(new_arr % 2 == 0) & (new_arr > 10)])

# task 3
generated_array = np.arange(1, 17).reshape(4, 4)
print(generated_array)
print(generated_array[(generated_array > 5) & (generated_array < 12)])
