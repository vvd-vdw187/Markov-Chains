from .template.markov_chain import MarkovChain
from dataclasses import dataclass
import numpy as np
from pprint import pprint

@dataclass
class ProbabilisticMarkovChain(MarkovChain):
    def generate_transition_matrix(self, s: int):
        # self.transition_matrix = np.random.dirichlet(np.ones(len(self.transition_matrix)), size=1)[0]
        # lower P = n_S / s + n
        # upper P = s + n_S / s + n
        # n = transitions per key
        # n_S = item
        self.transition_matrix = [[[item / (s + sum(self.transition_counts[key].values())), # lower P
                                    (s + item) / (s + sum(self.transition_counts[key].values()))] # upper P
                                   for item in self.transition_counts[key].values()] 
                                   for key in self.transition_counts.keys()]
        pprint(self.transition_matrix)

    def step(self):
        self.state = np.random.choice(
            range(len(self.transition_matrix)),
            p=self.transition_matrix[self.state]
        )
        self.transition_history.append(self.state)