import numpy as np

arr = np.arange(1, 37).reshape(6, 6)
print(arr)

reshaped = arr.reshape(3, -1)
print(reshaped)

flat1 = arr.flatten()
print(flat1)
print()

print(flat1.flags["OWNDATA"])
flat1[0] = 100
print(flat1[0])
print(arr[0, 0])

print()
flat2 = arr.ravel()
print(flat2)
print(flat2.flags["OWNDATA"])
flat2[0] = 100
print(flat2)
print(arr)
