from .template.markov_chain import MarkovChain
from dataclasses import dataclass
import numpy as np

@dataclass
class ProbabilisticMarkovChain(MarkovChain):
    # inherits the following from MarkovChain:
    # transition_matrix: np.array
    # state: int        

    def step(self):
        self.state = np.random.choice(
            range(len(self.transition_matrix)),
            p=self.transition_matrix[self.state]
        )
        self.state_history.append(self.state)