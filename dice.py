import constants
import random


class Dice:
    def __init__(self):
        self.currentValue = 0
        self.nFaces = constants.N_FACES_DICE
        self.kept = False

    def roll(self):
        if(self.kept):
            return self.currentValue
        else:
            self.currentValue = random.randrange(0, constants.N_FACES_DICE, 1)
            return self.currentValue

    def reset(self):
        self.currentValue = 0
        self.kept = False

    def keepDice(self):
        self.kept = True

    def __eq__(self, other):
        if(self.currentValue == other):
            return True
        else:
            return False
