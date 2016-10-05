import constants
from dice import Dice

class Player:
    nPlayers = 0
    def __init__(self):
        Player.nPlayers += 1
        self.ID = Player.nPlayers
        self.lives = constants.MAX_LIVES
        self.points = 0
        self.playerDice = []
        for i in range(constants.STARTING_DICE_NUMBER):
            self.playerDice.append(Dice())
        self.remainingRolls = constants.ROLLS_PER_TURN

    def takeDamage(self, damagePoints):
        self.lives = self.lives - damagePoints

    def heal(self, healAmmount):
        self.lives = self.lives + healAmmount

    def processDice(self):
        pass

    def countPoints(self):
        pass