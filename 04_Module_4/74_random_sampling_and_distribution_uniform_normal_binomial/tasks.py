import numpy as np

# task 1
float_5_gen = np.random.uniform(5, 15, 5)
print(float_5_gen)
print()

# task2
normal_Dist = np.random.normal(100, 20, 10)
print(normal_Dist)
print()

# task 3
binomaial_dist = np.random.binomial(8, 0.5, 10)
print(binomaial_dist)
print()

# task 4
np.random.seed(42)
print(np.random.normal(0, 1, 5))

np.random.seed(42)
print(np.random.normal(0, 1, 5))
