from .template.markov_chain import MarkovChain
from dataclasses import dataclass
import numpy as np

class PossibilisticMarkovChain(MarkovChain):
    def __init__(self, transition_matrix: np.array, state: list):
        super().__init__(transition_matrix, state)

        self.transitions = {i: {j: transition_matrix[i][j] for j in range(len(transition_matrix[i]))} for i in range(len(transition_matrix))}
        
    def step(self):
        current_state = self.state[-1]
        next_state = max(self.transitions[current_state], key=self.transitions[current_state].get)
        self.state_history.append(next_state)
        self.transition_history.append(self.transition_matrix)
