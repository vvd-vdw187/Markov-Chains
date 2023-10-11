import numpy as np
from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class MarkovChain:
    transition_matrix: np.array
    state: list
    
    def __post_init__(self):
        self.state_history: list = [self.transition_matrix]
    
    @abstractmethod
    def step(self):
        pass

    def run(self, n_steps: int):
        print("Running Markov Chain for {} steps".format(n_steps))
        for _ in range(n_steps):
            self.step()

    

