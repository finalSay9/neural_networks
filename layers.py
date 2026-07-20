import random

inputs = [1, 2, 3, 1.1, 2.3]

times = int(input("How many neurons? "))

for i in range(times):

    weights = [random.uniform(-1, 1) for _ in range(len(inputs))]
    bias = random.uniform(-1, 1)

    output = 0

    for x, w in zip(inputs, weights):
        output += x * w

    output += bias

    print(f"Neuron {i+1}")
    print("Weights:", weights)
    print("Bias:", bias)
    print("Output:", output)
    print()