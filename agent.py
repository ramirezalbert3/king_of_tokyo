"""
Useful definitions:
V(s) = max_{a in actions} Q(s,a)
policy(s) = arg_max_{a in actions} Q(s,a)

Also from: http://artint.info/html/ArtInt_227.html
Qk+1(s,a) 	= ∑s' P(s'|s,a) (R(s,a,s')+ γVk(s'))  for k ≥ 0
Vk(s) 	= maxa Qk(s,a)  for k>0
"""


# Maybe this class should NOT be game specific
# Does it need to inherit? Maybe only Class Game needs to know about Player
class Agent():
    def __init__(self, alpha=1.0, epsilon=0.05, gamma=0.8):
        self.epsilon = epsilon  # (exploration prob)
        self.alpha = alpha  # (learning rate)
        self.gamma = gamma  # (discount rate)
        self.states = []
        self.V = []
        self.Q = []
        self.Policy = []

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
