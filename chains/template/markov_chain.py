import numpy as np
from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class MarkovChain:
    transition_matrix: np.array
    state: list
    
    def __post_init__(self):
        self.state_history: list = [self.transition_matrix]

    # @property
    # def get_state(self):
    #     return self.state
    
    # @get_state.setter
    # def set_state(self, value):
    #     self.state = value
    
    # @property
    # def get_state_history(self):
    #     return self.state_history
    
    # @get_state_history.setter
    # def set_state_history(self, value):
    #     self.state_history = value
    
    @abstractmethod
    def step(self):
        pass

    def run(self, n_steps: int):
        print("Running Markov Chain for {} steps".format(n_steps))
        for _ in range(n_steps):
            self.step()

    

