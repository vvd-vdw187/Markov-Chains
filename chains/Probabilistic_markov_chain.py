from .template.markov_chain import MarkovChain
from dataclasses import dataclass
import numpy as np

@dataclass
class ProbabilisticMarkovChain(MarkovChain):
    def step(self):
        self.state = np.random.choice(
            range(len(self.transition_matrix)),
            p=self.transition_matrix[self.state]
        )
        self.transition_history.append(self.state)