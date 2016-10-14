from player import Player
from kingAgent import KingAgent


class Game:
    def __init__(self):
        self.trainingAgent = KingAgent()
        pass

# Flow control functions
    def setInitialState(self):
        self.trainingAgent.resetPlayer()

    def getReward(self, state):
        '''
        State is defined in a list:
        Points, Lives, DiceList, RemainingRolls, OtherPlayers
        '''
        # Process current state
        playerPoints = state[0]
        playerDice = state[1]
        remainingRolls = state[2]

        reward = 0
        if(remainingRolls > 0):
            return reward

        # Using auxiliary player for Player.countPoints()
        auxPlayer = Player()
        auxPlayer.setDiceWithString(playerDice)
        auxPlayer.processDice()
        pointsGained = auxPlayer.countPoints()
        reward += playerPoints + pointsGained
        return reward
