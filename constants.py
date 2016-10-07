# Constants.py
from enum import Enum
# Constants
MAX_DICE = 8
MAX_LIVES = 10
MAX_POINTS = 20
N_FACES_DICE = 5
ROLLS_PER_TURN = 3
STARTING_DICE_NUMBER = 6
MIN_DICE_FOR_POINTS = 3

# Lists
class DiceValues(Enum):
    one = 1
    two = 2
    three = 3
    heal = 4
    attack = 5