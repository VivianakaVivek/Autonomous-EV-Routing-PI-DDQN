# Physics-Informed Double Deep Q-Network (PI-DDQN) for Autonomous EV Routing

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

This repository contains the source code, data, and academic documentation for the research on **Physics-Informed Double Deep Q-Networks (PI-DDQN)** integrated with **SG-GAN**. This project establishes a new, mathematically rigorous state-of-the-art methodology for safe, autonomous Electric Vehicle (EV) routing in dynamic, gridlocked smart cities.

---

## 🛑 NEWCOMERS: START HERE

If you are new to this repository, please read the methodology documentation located in `Documentation/Methodology/` sequentially. They perfectly sum up the entirety of the research, the mathematics, and the problem solved.

1. **[01_Research_Overview.md](Documentation/Methodology/01_Research_Overview.md)**: The complete, consolidated summary of our Research Aim, the Core Problem (Tabular Q-Learning failing at physics), How we solve it with PI-DDQN, and the extensive empirical simulation results (Energy, Scalability, and Overhead).
2. **[02_Mathematical_Formulas_and_Variables.md](Documentation/Methodology/02_Mathematical_Formulas_and_Variables.md)**: A complete breakdown of all mathematical formulas used for traffic congestion, travel time, physics constraints, and the novel deep learning variables introduced.
3. **[03_Hand_Calculation_Proof_of_Physics.md](Documentation/Methodology/03_Hand_Calculation_Proof_of_Physics.md)**: A transparent, step-by-step manual calculation proving that the underlying physics engine perfectly matches empirical reality.

---

## 📌 High-Level Research Overview

A fundamental vulnerability of traditional data-driven EV routing models—such as Tabular Q-Learning and standard Deep Reinforcement Learning (DRL) algorithms—is that they are fundamentally "physics-blind." They evaluate spatial graphs purely based on historical or heuristic data, inherently relying on post-failure penalization. In dynamic urban environments, this causes conventional A.I. agents to blindly route EVs into highly congested, high-incline arteries, draining the battery faster than the heuristic expects and leading to catastrophic stranding events.

This research successfully bridges the gap between theoretical algorithmic pathfinding and practical mechanical constraints. We introduce the **Physics Action Mask**, a mathematical filter integrated directly into the neural network's decision pipeline. By calculating the required thermodynamic energy ($E_{req}$) for every adjacent edge—factoring in vehicle mass, aerodynamic drag ($C_d = 0.28$), drivetrain efficiency (0.85), road incline, and real-time congestion ($I'$)—the architecture preemptively masks out impossible actions *before* the neural network evaluates them. 

---

## 📂 Repository Structure

To assist external reviewers and collaborators, the codebase has been perfectly restructured into logical modules representing the separation of concerns:

### 🧠 Core Implementation Modules
* **`PI_DDQN/`**: Contains the novel routing intelligence (`pi_ddqn_routing.py`, `run.py`).
* **`SG_GAN/`**: Completely decoupled map generation and adversarial environment logic (`network_env.py`).
* **`Baselines/`**: Contains all legacy algorithms used for comparison (Q-Learning, Clustering, Dijkstra, GNN_RL, MILP, Metaheuristic).
* **`Scripts/`**: Evaluation scripts to run large-scale simulations and generate comparative graphics.
* **`config.py`**: The central brain for hyperparameter tuning. Shared across all algorithms to guarantee fair testing.

### 📄 Documentation & References (`Documentation/`)
* **`Methodology/`**: The core research explanations and markdown proofs (Start here!).
* **`Literature_Review/`**: Perfectly numbered and professionally titled PDF reference materials cited within the study.
* **`PI_DDQN_Research Paper.pdf`**: The finalized manuscript detailing our findings.

### 📊 Data & Results
* **`Data/`**: Serialized graphs and GAN metrics ensuring deterministic environments for testing.
* **`Results/`**: Simulation logs, metrics, and visualization HTML files.
* **`Utils/`**: Independent helper tools and scratchpad scripts.

---

## 🛠️ Installation & Execution Guide

**1. Clone the repository:**
```bash
git clone https://github.com/yourusername/PI-DDQN-EV-Routing.git
cd PI-DDQN-EV-Routing
```

**2. Install dependencies:**
The environment relies on standard scientific and deep learning libraries.
```bash
pip install numpy torch networkx osmnx matplotlib scipy pandas
```

**3. Run the complete experiment pipeline:**

Execute the main simulations from the `Scripts/Evaluation_Scripts/` directory (or use your IDE to run the specific Python files) to generate topologies, run comparisons, and plot the efficiency graphs.

---
*This research was developed as a Bachelor of Technology (BTP) Project.*
