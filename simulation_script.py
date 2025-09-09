
import numpy as np
import pandas as pd

# Parameters for simulation
num_records = 1000

# Generate time steps (sequential)
time_steps = np.arange(num_records)

# Generate input values (random between -1 and 1)
inputs = np.random.uniform(-1, 1, num_records)

# Generate state values (random between -2 and 2)
states = np.random.uniform(-2, 2, num_records)

# Generate output values (random between -1 and 1)
outputs = np.random.uniform(-1, 1, num_records)

# Generate disturbance values (random between -0.5 and 0.5)
disturbances = np.random.uniform(-0.5, 0.5, num_records)

# System parameters (random values within certain ranges for A, B, C, D)
A_params = np.random.uniform(0.5, 1.5, num_records)
B_params = np.random.uniform(-0.5, 0.5, num_records)
C_params = np.random.uniform(-1, 1, num_records)
D_params = np.random.uniform(-0.5, 0.5, num_records)

# Create DataFrame to store the dataset
data = {
    "Time Step": time_steps,
    "Input (u)": inputs,
    "State (x)": states,
    "Output (y)": outputs,
    "Disturbance (ω)": disturbances,
    "System Parameter A": A_params,
    "System Parameter B": B_params,
    "System Parameter C": C_params,
    "System Parameter D": D_params
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv('simulation_data.csv', index=False)
