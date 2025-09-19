import numpy as np

arr = np.array([[1, 2, np.nan], [np.nan, 5, np.nan]])

np.savetxt("messy.csv", arr, delimiter=",", fmt="%.2f")

with open("messy.csv") as f:
    text = f.read().replace("nan", "")

with open("messy_clean.csv", "w") as f:
    f.write(text)

loaded = np.genfromtxt(
    "messy_clean.csv", delimiter=",", missing_values="nan", filling_values=-1
)
print(loaded)
