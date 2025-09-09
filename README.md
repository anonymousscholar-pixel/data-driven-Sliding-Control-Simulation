
# Data-Driven Control Simulation Dataset

## Overview
This repository contains simulation data and scripts for testing data-driven control methods. The dataset is aligned with the research on iterative methods in robust control, particularly focusing on system identification under disturbances.

## Directory Structure
- `/scripts`: Contains the simulation and data generation scripts.
- `/dataset`: The CSV file containing the input-state-output data for control systems.
- `/configs`: Configuration files detailing parameters used for simulation.
- `/docs`: Documentation and instructions for replicating the experiments.

## How to Run
1. Clone the repository.
2. Install the required dependencies (see requirements.txt).
3. Run the simulation script: `python scripts/simulation_script.py`.
4. The generated data will be saved as `simulation_data.csv` in the `/dataset` directory.

## Dependencies
- Python 3.8+
- numpy
- pandas

## Dataset Details
The dataset includes:
- Time steps
- Input, state, and output trajectories
- Disturbances and system parameters (A, B, C, D)

For further details, refer to the accompanying research paper and configuration files.
