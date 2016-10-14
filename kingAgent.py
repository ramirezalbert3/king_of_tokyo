from agent import Agent
from player import Player
from utils import flipCoin
import random


# For now we'll define an agent that plays alone
class KingAgent(Agent, Player):
    def __init__(self, alpha=1.0, epsilon=0.05, gamma=0.8):
        Player.__init__(self)
        Agent.__init__(self, alpha, epsilon, gamma)

    # This class has to define Agent methods based on Player

    def getLegalActions(self):
        '''
        Actions defined in a list of kept dice
        In this game, state independent
        This is actually only depends on the number of dice
        Using binary representation to define legal actions
        Legal action: Do we keep or roll each dice?
        For 4 dice, 0110 (6) means we keep dice 1 & 2 and roll 0 & 3
        '''
        legalActionsList = []
        numLegalActions = 2 ** len(self.playerDice)
        for i in range(numLegalActions):
            legalActionsList.append(i)
        return legalActionsList

    def getAction(self, state):
        # Pick Action
        legalActions = self.getLegalActions(state)
        action = self.getPolicy(state)
        if (action is None or flipCoin(self.epsilon)):
            action = random.choice(legalActions)

        return action

    def doWeKeepDice(self, legalAction, diceToKeep):
        '''
        To know if we keep a given dice we shift bites (>>) and & with True
        For previous example:
        doWeKeepDice(6, 1): (6 >> 1 & True) = True
        Where 6 is the legalAction processed and 1 is the dice we might keep
        '''
        assert (diceToKeep <= len(self.playerDice)), "Keeping more dice than we have"
        return ((legalAction >> diceToKeep) & True)

    def getState(self):
        state = []
        state.append(self.points)
        state.append(self.lives)
        state.append(self.getPlayerDice())
        state.append(self.remainingRolls)
        # Append otherPlayer lives & points in lists, even if only 1
        return state
