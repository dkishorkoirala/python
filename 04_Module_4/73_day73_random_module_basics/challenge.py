import numpy as np

gen = np.random.randint(low=1, high=7, size=1000)

dict_ = {i: 0 for i in range(1, 7)}  # dict with count = 0 for 1-6

for g in gen:
    dict_[g] += 1  # increment of dict_count(i)

print(dict_)
