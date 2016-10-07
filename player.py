import constants
from dice import Dice

class Player:
    nPlayers = 0
    def __init__(self):
        Player.nPlayers += 1
        self.ID = Player.nPlayers
        self.inPlay = True
        self.lives = constants.MAX_LIVES
        self.points = 0
        self.playerDice = []
        for i in range(constants.STARTING_DICE_NUMBER):
            self.playerDice.append(Dice())
        self.remainingRolls = constants.ROLLS_PER_TURN
        self.attackDice = 0
        self.healDice = 0
        self.pointDice = [0, 0, 0]

    def takeDamage(self, damagePoints):
        self.lives = self.lives - damagePoints
        if (self.lives < 0):
            self.lives = 0
            self.inPlay = False

    def heal(self, healAmmount):
        self.lives = self.lives + healAmmount
        if (self.lives > constants.MAX_LIVES):
            self.lives = constants.MAX_LIVES

    def attack(self):
        return self.attackDice

    def resetDice(self):
        for i in len(self.playerDice):
            self.playerDice[i].reset()

    def resetPlayer(self):
        self.resetDice()
        self.lives = constants.MAX_LIVES
        self.points = 0

    def processPlay(self):
        for i in len(self.playerDice):
            if(self.playerDice[i].getValue == constants.DiceValues.attack):
                self.attackDice += 1
            elif(self.playerDice[i].getValue == constants.DiceValues.heal):
                self.healDice += 1
            else:
                self.pointDice[self.playerDice[i].getValue-1] += 1

    def addPoints(self):
        for i in len(self.pointDice):
            if(self.pointDice[i] // MIN_DICE_FOR_POINTS):
                self.points = i + self.pointDice[i] % MIN_DICE_FOR_POINTS