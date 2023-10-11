from chains.Probabilistic_markov_chain import ProbabilisticMarkovChain
from chains.Possibilistic_markov_chain import PossibilisticMarkovChain
from chains.Fuzzy_markov_chain import FuzzyMarkovChain

TRANSITION_MATRIX = [[0.0, 0.2, 0.8, 0.0],
                     [0.3, 0.0, 0.0, 0.7],
                     [0.1, 0.1, 0.1, 0.7],
                     [0.1, 0.6, 0.1, 0.2]]



def main(transition_matrix):
    # Pr_chain = ProbabilisticMarkovChain(transition_matrix=transition_matrix, state=[0])
    # Pr_chain.run(10000)
    # print(Pr_chain.state_history)
    # print(Pr_chain.state)

    Ps_chain = PossibilisticMarkovChain(transition_matrix=transition_matrix, state=[0.2,0.3,0.4,0.1])
    Ps_chain.run(10)
    print(Ps_chain.state_history)
    print(Ps_chain.state)

if __name__ == "__main__":
    main(transition_matrix=TRANSITION_MATRIX)