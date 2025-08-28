import numpy as np

generated_array = np.random.randint(1, 100, 50)
print(generated_array[(generated_array % 2 == 0) & (generated_array % 15 == 0)])
# or
# generated_array [ generated_array % 30 == 0]

print(generated_array[(generated_array < 20) | (generated_array < 70)])
