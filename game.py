from player import Player


class Game:
    def __init__(self):
        pass

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

        # Using auxiliary player for Player.CountPoints()
        auxPlayer = Player()
        auxPlayer.setDiceWithString(playerDice)
        auxPlayer.processRoll()
        pointsGained = auxPlayer.CountPoints()
        reward += playerPoints + pointsGained
        return reward
