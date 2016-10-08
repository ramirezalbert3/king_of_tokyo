import constants
import random


class Dice:
    # Methods
    def __init__(self):
        self.currentValue = 0
        self.nFaces = constants.N_FACES_DICE
        self.kept = False

    def roll(self):
        self.currentValue = random.randrange(0, constants.N_FACES_DICE, 1)
        return self.currentValue

    def reset(self):
        self.currentValue = 0
        self.kept = False

    def keepDice(self):
        self.kept = True

    def getValue(self):
        return self.currentValue

    def getValueAsString(self):
        for valString in constants.DiceValues:
            if (self.currentValue == valString):
                return valString.name
