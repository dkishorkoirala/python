import numpy as np

arr = np.array([5, 10, 15, 20, 25])

print(arr)
print(type(arr))
print()

lst = [1, 2, 3, 4, 5]
new_list = [i * 3 for i in lst]

print(new_list)
print(type(new_list))

print()
my_arr = np.array(lst)
print(my_arr * 3)
print(type(my_arr))
