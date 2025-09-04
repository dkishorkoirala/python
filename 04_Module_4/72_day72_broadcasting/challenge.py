import numpy as np

temps_celsius = np.array(
    [
        [25, 28, 30, 32, 31, 29, 27],
        [15, 18, 20, 22, 21, 19, 17],
        [10, 12, 15, 14, 13, 11, 9],
    ]
)

fahrenheit = (temps_celsius * 9 / 5) + 32
print(fahrenheit)
