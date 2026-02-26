# The ReLU activation function transforms the neuron's raw output into something more meaningful:

# If the output is positive → keep it
# If it’s negative → replace it with 0
# This helps the network learn non-linear patterns and ensures the neuron only activates for useful inputs.

# Input: Study hours
study_hours = 5

# Weight and bias
weight = 10
bias = 5

# Raw neuron output (before activation)
neuron_output = study_hours * weight + bias

# Apply ReLU activation
activated_output = max(0, neuron_output)

print("Neuron Output (before activation):", neuron_output)
print("Activated Output (ReLU):", activated_output)
