import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
np.savetxt("Data.csv", arr, delimiter=",", fmt="%d")

loaded = np.loadtxt("Data.csv", delimiter=",")
print(loaded)
