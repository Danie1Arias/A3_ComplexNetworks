import numpy as np
import random

from matplotlib import pyplot as plt


class SISModel:
    def __init__(self, graph, beta, mu, rho0=0.2):
        self.G = graph
        self.beta = beta
        self.mu = mu
        self.rho0 = rho0
        self.states = {node: "S" for node in self.G.nodes}
        self.N = len(self.G)
        self._initialize_infection()

    def _initialize_infection(self):
        infected = random.sample(list(self.G.nodes()), max(30, int(self.rho0 * self.N)))
        for node in infected:
            self.states[node] = "I"

    def step(self):
        new_states = self.states.copy()
        for node in self.G.nodes:
            if self.states[node] == "I":
                if np.random.rand() < self.mu:
                    new_states[node] = "S"
            elif self.states[node] == "S":
                for neighbor in self.G.neighbors(node):
                    if self.states[neighbor] == "I" and np.random.rand() < self.beta:
                        new_states[node] = "I"
                        break
        self.states = new_states

    def run(self, Tmax=1000, Ttrans=900):
        rho_t = []
        rho_values = []
        for t in range(Tmax):
            self.step()
            infected = sum(1 for state in self.states.values() if state == "I")
            rho = infected / self.N
            rho_values.append(rho)
            if t >= Ttrans:
                rho_t.append(rho)
        return np.mean(rho_t), rho_values
