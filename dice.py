import constants
import random

class Dice:
    # Methods
    def __init__(self):
        self.currentValue = 0
        self.nFaces = constants.N_FACES_DICE

    def roll(self):
        self.currentValue = random.randrange(0,constants.N_FACES_DICE,1)
        return self.currentValue

    def getValue(self):
        return self.currentValue 
