import numpy as np

string_lst = list(input("Enter the number to convert to list: "))

number_lst = [int(i) for i in string_lst]

numpy_arr = np.array(number_lst)
print(numpy_arr)

result = numpy_arr * 5

print(
    f"The original list: {number_lst}\nNumpy array: {numpy_arr}\nAfter processing: {result}"
)
