import numpy as np

inputs = [1.2, 2, 1.0, 3]
weights = [
    [0.1, 1.1, 0.2, 0.3],
    [1.1, 0.4, 0.11, 0.2],
    [0.1, 0.3, 0.2, 0.7]
    ]
bias = [0.2, 2.1, 3]

output = np.dot(inputs, weights) + bias

print(output)