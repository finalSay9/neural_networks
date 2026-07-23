import numpy as np

inputs = [1.2, 2, 1.0, 3]
weights = [0.1, 1.1, 0.2, 0.3]
bias = 2

output = np.dot(inputs, weights) + bias

print(output)