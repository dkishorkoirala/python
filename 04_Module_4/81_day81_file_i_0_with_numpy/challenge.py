import numpy as np

rows, cols = 10, 5
readings = np.random.rand(rows, cols)

np.savetxt("sensor_readings.csv", readings, delimiter=",", fmt="%.9f")
np.save("sensor_readings.npy", readings)

csv_loaded = np.loadtxt("sensor_readings.csv", delimiter=",")
npy_loaded = np.load("sensor_readings.npy")

print("Original:\n", readings)
print("\nCSV Loaded:\n", csv_loaded)
print("\nNPY Loaded:\n", npy_loaded)

print("\nCSV and NPY match?", np.allclose(csv_loaded, npy_loaded))
