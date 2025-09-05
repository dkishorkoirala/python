import numpy as np

# task 1:

gen_num = np.random.randint(low=50, high=101, size=10)
print(gen_num)

# task 2:

float_random = np.random.rand(3, 3)
print(float_random)
print()

# task 3:
normal_dist_random = np.random.randn(5)
print(normal_dist_random)

# task 4:
np.random.seed(123)
print(np.random.randint(0, 5, 5))

np.random.seed(123)
print(np.random.randint(0, 5, 5))
