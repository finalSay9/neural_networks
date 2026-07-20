#lets create a single neuron

inputs = [1,2,3]
weights = [0.2, 0.3, -0.4]
bias = 2

outputs = (
    inputs[0] * weights[0] +
    inputs[1] * weights[1] +
    inputs[1] * weights[1] + bias
)

print(outputs)
