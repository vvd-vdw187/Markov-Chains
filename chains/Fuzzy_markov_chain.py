from .template.markov_chain import MarkovChain
from dataclasses import dataclass
import numpy as np

class FuzzyMarkovChain(MarkovChain):
    def step(self):
        self.state = np.matmul(self.state, self.transition_matrix)
        self.transition_history.append(self.state)