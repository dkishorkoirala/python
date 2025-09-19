import numpy as np

arr = np.arange(1000)

np.save("big_array.npy", arr)

loaded = np.load("big_array.npy")
print(loaded)

print("Array matches?", np.array_equal(arr, loaded))
