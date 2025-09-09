
# Data-Driven Control Simulation Dataset

## Overview
This repository contains simulation scripts, configuration files, and datasets used for testing the **Compliant Super Spiral Sliding Control (CS3C)** method. The CS3C method is designed to dynamically adjust computation frequencies and switch between linear and nonlinear problem-solving according to system needs. This dataset is derived from a batch reactor case study, used to evaluate the control system's performance under disturbances and uncertainties.

The control method aims to optimize high-precision control while suppressing high-frequency oscillations, enhancing system stability in both linear and nonlinear environments. The dataset used is referenced from [37], where a batch reactor with 10 controllers and a 0.1s sampling interval is modeled.

## Directory Structure
- **`/scripts`**: Contains simulation and data generation scripts for evaluating the CS3C method.
- **`/dataset`**: Contains the CSV file with input-state-output data for control systems, used for simulations.
- **`/configs`**: Configuration files detailing the parameters used for simulations, including adjustable and default parameters.
- **`/docs`**: Documentation and instructions for replicating the experiments.

## How to Run
1. **Clone the repository**:
   ```bash
   git clone https://github.com/anonymousscholar-pixel/data-driven-Sliding-Control-Simulation
   ```
2. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the simulation script**:
   ```bash
   python scripts/simulation_script.py
   ```
4. The generated data will be saved as `simulation_data.csv` in the `/dataset` directory.

## Dependencies
- **Python 3.8+**
- **numpy**
- **pandas**
- **matplotlib** (for data visualization)

## Dataset Details
The dataset is based on a batch reactor case study used for simulating the CS3C method. The data is structured to represent both **linear** and **nonlinear** system operations under various control inputs.

### Variables in the Dataset:
- **Time steps**: The sequence of time steps for system evolution.
- **Input**: Control input applied to the system.
- **State**: The state of the system at each time step.
- **Output**: The system's output at each time step.
- **Disturbances**: Disturbance inputs affecting the system.
- **System Parameters**: Includes system matrices \( A \), \( B \), \( C \), and \( D \), which are used to build the model for simulation. The system's disturbance is bounded by \( \omega(k)\omega(k)^T \leq 0.0014I_6 \).

For simulation, the dataset consists of 100 input-state-output trajectories, where each trajectory has a length \( T = 8 \). The data is randomly generated for the inputs within the range of \([-0.1, 0.1]\). The initial system state is set as \( x_0 = [0.51, 0.39, -0.30, -0.28]^T \).

### Reactor Case Study:
- **Sampling Time**: 0.1s
- **Job Length**: 100
- **Number of Controllers**: 10
- **Parameters**: The key parameters include time, sampling rate, allocation count, job count, and completion time.

For more detailed information about the parameters used for the CS3C method, refer to the configuration files in the `/configs` folder.

## Research Paper
The dataset and simulation scripts are based on the **Compliant Super Spiral Sliding Control (CS3C)** method outlined in the following research paper. For further details about the method and the experimental setup, refer to the associated publication:

- **Title**: [Insert Paper Title Here]
- **Link**: [Insert Link Here]

### Key Features of the CS3C Method:
- **Dynamic Frequency Adjustment**: CS3C adjusts computational frequencies based on linear and nonlinear problem-solving requirements.
- **Federated Learning**: The system uses federated learning for real-time optimization of system parameters, enabling efficient problem-solving across different computational challenges.
- **Stability in Uncertain Environments**: The method mitigates high-frequency oscillations and enhances system stability.

### Figures:
- **Figure 1**: System Design Representation – Describes how linear and nonlinear system parameters are handled within the CS3C framework.
- **Figure 2**: Simulation Results – Comparison of DDC with \( q = 1 \) and \( q = 100 \), Offline DDC, Online DDC, and Model-based H∞ control performance.

## License
The contents of this repository are made available for academic research and educational purposes. Please reference the corresponding research paper when using this dataset or simulation scripts.
