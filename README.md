# Physics-Informed Double Deep Q-Network (PI-DDQN) for Autonomous EV Routing

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

This repository contains the source code, data, and academic documentation for the research on **Physics-Informed Double Deep Q-Networks (PI-DDQN)** integrated with **SG-GAN**. This project establishes a new, mathematically rigorous state-of-the-art methodology for safe, autonomous Electric Vehicle (EV) routing in dynamic, gridlocked smart cities.

---

## 📌 Detailed Research Overview

A fundamental vulnerability of traditional data-driven EV routing models—such as Tabular Q-Learning and standard Deep Reinforcement Learning (DRL) algorithms—is that they are fundamentally "physics-blind." They evaluate spatial graphs purely based on historical or heuristic data, inherently relying on post-failure penalization. In dynamic urban environments, this causes conventional A.I. agents to blindly route EVs into highly congested, high-incline arteries, draining the battery faster than the heuristic expects and leading to catastrophic stranding events.

This research successfully bridges the gap between theoretical algorithmic pathfinding and practical mechanical constraints. We introduce the **Physics Action Mask**, a mathematical filter integrated directly into the neural network's decision pipeline. By calculating the required thermodynamic energy ($E_{req}$) for every adjacent edge—factoring in vehicle mass, aerodynamic drag ($C_d = 0.28$), drivetrain efficiency (0.85), road incline, and real-time congestion ($I'$)—the architecture preemptively masks out impossible actions *before* the neural network evaluates them. 

---

## 🚀 Core Architectural Innovations

### 1. Formal Physical Guarantees (100% Safe Routing)
By embedding real-world physical constraints into the architecture, the PI-DDQN evaluates $E_{req} > SOC$ to mathematically block lethal state transitions. This entirely eliminates the 1,845 physical stranding violations observed in the baseline tabular architecture, guaranteeing a **perfect 100% routing success rate**.

### 2. Edge Deployability (Solving the Curse of Dimensionality)
Standard Tabular Q-Learning suffers an $\mathcal{O}(|S| \times |A|)$ memory explosion, requiring a massive $\sim$78.0 MB Q-table at 100 nodes, rendering it completely incompatible with legacy vehicular microcontrollers. Our proposed neural architecture maps state spaces via continuous forward-pass tensor operations. The deployable inference model requires only **$\sim$281 KB at 50 nodes** and processes routing decisions in **$<0.200$ ms**, definitively proving its feasibility for edge computing.

### 3. Energy Optimization Under Severe Congestion
We implemented a dynamic congestion model that computes a local stop-and-go factor ($I'_{ij}$), directly inflating energy consumption by up to +20\% in gridlock to simulate realistic thermodynamic waste. The PI-DDQN proactively forces strategic detours along secondary flat roads, achieving a non-monotonic energy drop at 100\% gridlock (18.52 kWh/100km). This comes within 2.3\% of the theoretical MILP global optimum and saves **+7.96\%** more energy than the baseline model.

### 4. Highly Realistic Topology Generation (SG-GAN)
To bypass the severe mode collapse common in synthetic graph generation, we heavily modified the SG-GAN framework. By explicitly extracting authentic geographic speed-to-distance ratios from real **Dwarka Mod OpenStreetMap (OSM)** data and applying a 20-iteration post-hoc heuristic search, the generator enforces strict spatial logic. It achieved a near-perfect 96\% connectivity rate and an optimal Kullback-Leibler Divergence (KLD) of **0.18**.

---

## 📂 Detailed Folder Significance & Repository Structure

To assist external reviewers and collaborators, the codebase has been strictly organized into logical modules:

### 🧠 Core Algorithm Modules
* **`pi_ddqn/` (Proposed Architecture)**: This folder contains the novel contribution of this research. It houses `pi_ddqn_routing.py`, which defines the neural network architecture, the Physics Action Mask logic, the experience replay buffer, and the reward penalty regularizer ($\lambda=0.25$).
* **`base_paper/` (Baseline Architecture)**: This folder isolates the legacy models we compare against. It contains the Tabular Q-Learning implementations and the baseline SG-GAN architecture from previous literature, ensuring a strict, fair, and untainted environment for benchmark testing.

### 📄 Documentation & Academia
* **`Latex Code/`**: Contains the complete, final LaTeX source code for the research manuscript, fully formatted for IEEE submission. This includes all rigorous mathematical proofs and generated tables (`result new .tex`).
* **`Markdown Docs/`**: Contains raw analytical notes, manual hand-calculation proofs for the physics engine, and granular variable introductions.
* **`Research Papers/`**: Contains the PDF literature and reference material cited within the study.

### 📊 Support & Logs
* **`Logs/`**: A repository for terminal output dumps, profiling overhead logs, and debug traces. (Kept out of the root directory to maintain a clean workspace).
* **`Utils/`**: Contains independent scratchpad files, PDF extraction tools, and graph node testing scripts used during development but not required for executing the main experiments.
* **`Data/` or `Maps/`**: Stores serialized graph artifacts (like `shared_map.pkl` and `real_gan_data.json`) to guarantee that all algorithms are evaluated on the exact same synthetic urban topologies.

### ⚙️ Root Execution Scripts
* **`config.py`**: The central brain for hyperparameter tuning. Adjusting variables here (like learning rate, EV mass, or maximum episodes) applies universally across both `base_paper` and `pi_ddqn` for perfectly fair testing.
* **`generate_map.py`**: The execution script for the SG-GAN. Run this to synthesize a new urban mesh topology.
* **`comparison_table.py`**: The primary experiment runner. It loads identical EV parameters and forces both the baseline and PI-DDQN algorithms to route them through identical traffic congestion profiles (25%, 50%, 100%), generating side-by-side performance metrics.
* **`generate_fig6.py` & `generate_physics_metrics.py`**: Automated scripts that calculate polynomial time scaling, generate 3D surface visualizations of the memory footprint, and plot convergence dynamics.

---

## 🛠️ Installation & Execution Guide

**1. Clone the repository:**
```bash
git clone https://github.com/yourusername/PI-DDQN-EV-Routing.git
cd PI-DDQN-EV-Routing
```

**2. Install dependencies:**
The environment relies on scientific and deep learning libraries.
```bash
pip install numpy torch networkx osmnx matplotlib scipy pandas
```

**3. Run the complete experiment pipeline:**

*Step A: Generate the Synthetic Topology*
```bash
python generate_map.py
```

*Step B: Execute the Routing Comparison (Q-Learning vs. PI-DDQN)*
```bash
python comparison_table.py
```

*Step C: Generate Academic Visualizations*
```bash
python generate_fig6_fast.py
python generate_physics_metrics.py
```

---
*This research was developed as a Bachelor of Technology (BTP) Project.*
