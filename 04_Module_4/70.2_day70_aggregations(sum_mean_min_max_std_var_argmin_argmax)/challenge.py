import numpy as np

marks = np.array(
    [
        [78, 85, 92, 88],
        [60, 72, 80, 75],
        [90, 95, 85, 100],
        [50, 65, 70, 60],
        [88, 78, 84, 92],
    ]
)

avg = np.mean(marks, axis=0)


print("The average marks of each student:", np.mean(marks, axis=1))
print("The average marks of each subject:", avg)
print("The highest marks scored in entire class:", np.max(marks))
print("The subject with the lowest average score:", np.min(avg))
