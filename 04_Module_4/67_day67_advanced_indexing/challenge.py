import numpy as np

arr = np.random.randint(1, 101, 50)

mask = arr[(arr % 2 == 0) & (arr % 5 == 0)]
final = mask[(mask < 20) | (mask > 80)]
print("original array:", arr)
print("number divisible by 10:", mask)
print("Final result:", final)
