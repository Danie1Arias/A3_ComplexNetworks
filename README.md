# SIS Epidemic Spreading in Complex Networks — Monte Carlo & MMCA Analysis

## Overview

This project explores epidemic spreading in complex networks through the **Susceptible-Infected-Susceptible (SIS)** model. The objective is to simulate the SIS dynamics using **Monte Carlo methods** and compare the outcomes with theoretical predictions from the **Microscopic Markov Chain Approximation (MMCA)** framework.

The study is focused on evaluating the stationary infected fraction ⟨ρ⟩ as a function of the infection probability `λ`, across different network topologies and recovery probabilities.

---

## Epidemic Model: SIS

Each node in the network represents an individual in one of two states:
- **S (Susceptible)**: Can be infected by neighbors.
- **I (Infected)**: Can transmit the infection to neighbors and recover spontaneously.

At each time step:
- Infected nodes recover with probability `μ`.
- Susceptible nodes are infected with probability `λ` per infected neighbor.

---

## Simulation Setup

**Network types (N = 1000 nodes)**:
- Erdős–Rényi (ER) with ⟨k⟩ = 4 and 6
- Barabási–Albert (BA) with ⟨k⟩ = 4 and 6

**Parameters**:
- Infection probabilities: `λ ∈ [0.00, 0.30]` with Δλ = 0.01
- Recovery probabilities: `μ = 0.2` and `μ = 0.4`
- Initial infected ratio: ρ₀ = 0.2
- Time steps: `Tmax = 1000`, with `Ttrans = 900` transient steps
- Repetitions: `Nrep = 50` (averaging over stochastic evolutions)

---

## Implementation

### Monte Carlo Simulations

Implemented in `sis_model.py`, the SIS dynamics is applied over NetworkX-generated graphs. Simulations are repeated and averaged to compute ⟨ρ⟩ after the transient regime.

### Theoretical Comparison (MMCA)

The MMCA model iteratively solves mean-field equations assuming constant degree `k`, providing an analytical estimation of the stationary infected density.

While MMCA is better suited to homogeneous networks (e.g., ER), it is also plotted for BA networks using ⟨k⟩ as an approximation.

---

## Outputs

- Epidemic diagrams: ⟨ρ⟩ vs. λ for each network and μ
- Curves include:
  - Monte Carlo simulation results
  - MMCA theoretical prediction (dashed lines)

Plots are grouped by μ values to allow visual comparison of network effects.

---

## Files

- `sis_model.py`: SIS simulation class
- `notebook.ipynb`: Main notebook for simulations, MMCA computation, and plots
- `README.md`: Project documentation

---

## Requirements

Install required libraries via pip:

```bash
pip install networkx numpy matplotlib
