from player import Player

"""
Useful definitions:
V(s) = max_{a in actions} Q(s,a)
policy(s) = arg_max_{a in actions} Q(s,a)
"""


class Agent(Player):
    def __init__(self):
        pass

    # Return Q-value for a given pair "state & action"
    def getQValue(self, state, action):
        pass

    # Returns max_action Q(state,action) over legal actions
    def getValue(self, state):
        pass

    # Compute the action to take in the current state
    # With probability self.epsilon we should take a random action
    # and take the best policy action otherwise
    def getAction(self, state):
        pass

    # Return the best action to take in a state or None
    def getPolicy(self, state):
        pass

    # state = action => nextState and reward transition
    # Q-Value update here
    def update(self):
        pass
