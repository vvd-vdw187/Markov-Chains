import numpy as np
from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class MarkovChain:
    transition_matrix: np.array
    state: int
    reference_states: list 
    
    def __post_init__(self):
        self.transition_history: list = [self.transition_matrix]
        self.state_history: list = [self.state]

        #Generate a dictionary that counts the transitions between states per state
        unique_states = np.unique(self.reference_states)
        print(unique_states)
        self.transition_counts = {i: {j: 0 for j in unique_states} for i in unique_states}
        # self.transition_counts = {i: {j: 0 for j in range(len(unique_states[i]))} for i in range(len(unique_states))}
        print(self.transition_counts)
        for i in range(len(self.reference_states)-1):
            self.transition_counts[self.reference_states[i]][self.reference_states[i+1]] += 1

        print(self.transition_counts)
    
    @abstractmethod
    def step(self):
        pass

    @abstractmethod
    def generate_transition_matrix(self):
        pass

    def run(self, n_steps: int):
        print(f"Running Markov Chain for {n_steps} steps")
        for _ in range(n_steps):
            self.step()
