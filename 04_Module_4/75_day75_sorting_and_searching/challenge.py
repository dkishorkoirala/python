import numpy as np

marks = np.array(
    [[78, 85, 92, 88], [56, 74, 80, 70], [89, 94, 90, 96], [45, 60, 55, 50]]
)

sorted_marks = np.sort(marks, axis=1)
print("Sorted student marks:\n", sorted_marks)

sorted_subjects = np.sort(marks, axis=0)
print("Sorted subject marks:\n", sorted_subjects)

find = np.where(marks > 90)
print("Students with marks greater than 90:\n", find)

pm = 60
find = np.where(marks < pm)
print("Students with failed marks less than 60:\n", find)

subject1_sorted = np.sort(marks[:, 0])
print(subject1_sorted)
print("Insert 75 at index:", np.searchsorted(subject1_sorted, 75))
