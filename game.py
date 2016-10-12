
from kingAgent import KingAgent
from player import Player

"""
Game specific definitions
State is defined by:
Player points & lives
Player dice
Other players lives
Other players points? (more below)
? How to act on this, maybe only to aim to kill the player wih the most points

Actions:
Keep/roll dice

Rewards:
Getting closer to 20 points?
Getting closer to 10 lives?
Getting opponents closer to 0 lives?
"""


# This class should probably be game-specific (King of Tokyo in this case)
# Should return all game-specific values (states, legalActions, etc)
class Game:
    def __init__(self, nPlayers=2):
        self.nPlayers = nPlayers
        self.playerList = []
        pAdded = 0
        while (pAdded < nPlayers):
            pAdded += 1
            self.playerList.append(KingAgent())

    def getState(self, playerID):
        state = []
        state.append(self.playerList[playerID].points)
        state.append(self.playerList[playerID].lives)
        state.append(self.playerList[playerID].getPlayerDice())
        for iPlayer in self.playerList:
            if (iPlayer.ID != playerID):
                state.append(iPlayer.lives)
        return state

    def resetGame(self):
        self.nPlayers = 0
        self.playerList = []
        Player.nPlayers = 0
