import constants
import dice

class Player:
    nPlayers = 0
    def __init__(self):
        nPlayers = nPlayers + 1
        self.ID = nPlayers
        self.lives = constants.MAX_LIVES
        self.points = 0
        self.dice.Dice()
        self.remainingRolls = ROLLS_PER_TURN

    def takeDamage(self, damagePoints):
        self.lives = self.lives - damagePoints

    def heal(self, healAmmount):
        self.lives = self.lives + healAmmount

    def processDice(self):
        

    def countPoints(self):