from .template.markov_chain import MarkovChain
from dataclasses import dataclass
import numpy as np

class FuzzyMarkovChain(MarkovChain):
    # inherits the following from MarkovChain:
    # transition_matrix: np.array
    # state: List        

    def step(self):
        self.state = np.matmul(self.state, self.transition_matrix)
        self.state_history.append(self.state)