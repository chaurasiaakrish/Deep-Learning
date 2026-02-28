import numpy as np

# --- Step 1: Neuron output after activation (dummy value from previous activation example) ---
# Suppose the neuron predicted a score after applying ReLU
prediction = 72.5   # example activated output

# --- Step 2: Actual score (ground truth) ---
actual = 80         # real score received by the student

# --- Step 3: Compute Mean Squared Error (MSE) loss ---
loss = (prediction - actual) ** 2

# --- Step 4: Print the loss ---
print("Prediction:", prediction)
print("Actual:", actual)
print("Loss (MSE):", loss)