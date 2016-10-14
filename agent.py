from collections import Counter
"""
Useful definitions:
V(s) = max_{a in actions} Q(s,a)
policy(s) = arg_max_{a in actions} Q(s,a)

Also check: http://artint.info/html/ArtInt_227.html
"""


class Agent():
    def __init__(self, alpha, epsilon, gamma):
        self.epsilon = epsilon  # (exploration prob)
        self.alpha = alpha  # (learning rate)
        self.gamma = gamma  # (discount rate)
        # Counters are like dictionaries that default to zero
        # Counter[KeyNotIndexedYet] = 0 instead of error
        self.V = Counter()
        self.Q = Counter()
        self.Policy = Counter()
        # Used to keep track of visited states because:
        # Policy[state] = 0 might be a valid action
        self.states = Counter()

    # Compute the action to take in the current state
    # With probability self.epsilon we should take a random action
    # and take the best policy action otherwise
    def getAction(self, state):  # pragma: no cover
        pass

    def getLegalActions(self):  # pragma: no cover
        pass

    # Return Q-value for a given pair "state & action"
    def getQValue(self, state, action):
        return self.Q[state, action]

    # Returns max_action Q(state,action) over legal actions
    def getValue(self, state):
        return self.V[state]

    # Return the best action to take in a state or None
    def getPolicy(self, state):
        if (self.states[state] > 0):
            return self.Policy[state]
        else:
            return None

    # state = action => nextState and reward transition
    # Q-Value, visits counter, Value and Policy update here
    def update(self, state, action, reward, nextState):
        self.states[state] += 1  # Increase visits counter
        prevQ = self.Q[state, action]
        # Reward for ending in next state + expected reward from then on
        increaseQ = reward + self.gamma*self.V[nextState]
        # For alpha=0 no learning, for =1 no remembering
        self.Q[state, action] += self.alpha * (increaseQ - prevQ)
        if (self.Q[state, action] > self.V[state]):
            self.V[state] = self.Q[state, action]
            self.Policy[state] = action
