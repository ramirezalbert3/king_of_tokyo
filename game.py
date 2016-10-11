
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
            self.playerList.append(Player())

    def getState(self, playerID):
        state = []
        state.append(self.playerList[playerID].points)
        state.append(self.playerList[playerID].lives)
        state.append(self.playerList[playerID].getPlayerDice())
        for iPlayer in self.playerList:
            if (iPlayer.ID != playerID):
                state.append(iPlayer.lives)
        return state

    def getLegalActions(self, playerID):
        '''
        Actions defined in a list of kept dice
        This is actually only depends on the number of dice
        Using binary representation to define legal actions
        Legal action: Do we keep or roll each dice?
        For 4 dice, 0110 (6) means we keep dice 1 & 2 and roll 0 & 3
        '''
        legalActionsList = []
        numLegalActions = 2 ** len(self.playerList[playerID].playerDice)
        for i in range(numLegalActions):
            legalActionsList.append(i)
        return legalActionsList

    def doWeKeepDice(self, legalAction, diceToKeep, playerID):
        '''
        To know if we keep a given dice we shift bites (>>) and & with True
        For previous example:
        doWeKeepDice(6, 1): (6 >> 1 & True) = True
        Where 6 is the legalAction processed and 1 is the dice we might keep
        '''
        assert (diceToKeep <= len(self.playerList[playerID].playerDice)), "Keeping more dice than we have"
        return ((legalAction >> diceToKeep) & True)

    def resetGame(self):
        self.nPlayers = 0
        self.playerList = []
        Player.nPlayers = 0
