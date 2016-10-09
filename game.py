
from player import Player

"""
Game specific definitions
State is defined by:
Player points & lives
Player dice
Other players lives
Other players points??? (no way to act on this, so maybe not part of state)

Actions:
Keep/roll dice

Rewards:
Getting closer to 20 points?
Getting closer to 10 lives?
Getting opponents closer to 0 lives?
"""


class Game:
    def __init__(self, nPlayers):
        self.nPlayers = nPlayers
        for i in nPlayers:
            self.playerList.append(Player())
        self.epsilon  # (exploration prob)
        self.alpha  # (learning rate)
        self.gamma  # (discount rate)

    def getState(self):
        pass

    def getLegalActions(self):
        pass
