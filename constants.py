# Constants.py
from enum import IntEnum
# Constants
MAX_DICE = 8
MAX_LIVES = 10
MAX_POINTS = 20
N_FACES_DICE = 5
ROLLS_PER_TURN = 3
STARTING_DICE_NUMBER = 6
MIN_DICE_FOR_POINTS = 3


# Lists
class DiceValues(IntEnum):
    one = 0
    two = 1
    three = 2
    heal = 3
    attack = 4
