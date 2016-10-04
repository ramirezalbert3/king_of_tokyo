import unittest
import constants
import dice

class TestDice(unittest.TestCase):
    testedDice = dice.Dice()

    def testRoll(self):
        for i in range(0,50):
            self.testedDice.roll()
            # print("Rolled a: ",self.testedDice.getValue())
            self.assertGreaterEqual(self.testedDice.getValue, 0)
            self.assertLess(self.testedDice.getValue(),constants.N_FACES_DICE)
            pass