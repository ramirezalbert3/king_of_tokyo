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
        for currentDice in self.playerDice:
            currentDice.reset()

    def resetPlayer(self):
        self.resetDice()
        self.lives = constants.MAX_LIVES
        self.points = 0
        self.attackDice = 0
        self.healDice = 0
        self.pointDice = [0, 0, 0]

    def processPlay(self):
        for currentDice in self.playerDice:
            if(currentDice.getValue() == constants.DiceValues.attack):
                self.attackDice += 1
            elif(currentDice.getValue() == constants.DiceValues.heal):
                self.healDice += 1
            else:
                self.pointDice[currentDice.getValue()] += 1

    def addPoints(self):
        # print 'Point dice list:', self.pointDice
        for i, roundPoints in enumerate(self.pointDice):
            if(roundPoints // constants.MIN_DICE_FOR_POINTS):
                self.points += (i + 1) + roundPoints % constants.MIN_DICE_FOR_POINTS
                # print 'Points after adding', i+1, ':', self.points
