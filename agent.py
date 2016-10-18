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

    def update(self, state, action, reward, nextState):
        '''
        state = action => nextState and reward transition
        Q-Value, visits counter, Value and Policy update here
        '''
        self.states[state] += 1  # Increase visits counter
        prevQ = self.Q[state, action]
        # Reward for ending in next state + expected reward from then on
        increaseQ = reward + self.gamma*self.V[nextState]
        # For alpha=0 no learning, for =1 no remembering
        self.Q[state, action] += self.alpha * (increaseQ - prevQ)
        if (self.Q[state, action] > self.V[state]):
            self.V[state] = self.Q[state, action]
            self.Policy[state] = action

    def act(self, state):  # pragma: no cover
        '''
        Perform an action and call update
        '''
        pass

    def getReward(self, state):  # pragma: no cover
        '''
        State is defined in a list:
        Points, Lives, DiceList, RemainingRolls, OtherPlayers
        '''
        pass

    def getAction(self, state):  # pragma: no cover
        '''
        Compute the action to take in the current state
        With probability self.epsilon we should take a random action
        and take the best policy action otherwise
        '''
        pass

    def getLegalActions(self):  # pragma: no cover
        '''
        Compute the action to take in the current state
        With probability self.epsilon we should take a random action
        and take the best policy action otherwise
        '''
        pass

    def getQValue(self, state, action):
        '''
        Return Q-value for a given pair "state & action"
        '''
        return self.Q[state, action]

    def getValue(self, state):
        '''
        Returns max_action Q(state,action) over legal actions
        '''
        return self.V[state]

    def getPolicy(self, state):
        '''
        Return the best action to take in a state or None
        '''
        if (self.states[state] > 0):
            return self.Policy[state]
        else:
            return None
