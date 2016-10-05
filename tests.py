import unittest
import constants
import dice

class TestDice(unittest.TestCase):
    testedDice = dice.Dice()

    def testRoll(self):
        maxVal = 0
        minVal = constants.N_FACES_DICE
        nTests = 50
        for i in range(0,nTests):
            self.testedDice.roll()
            if (self.testedDice.getValue() > maxVal):
                maxVal = self.testedDice.getValue()
                pass
            if (self.testedDice.getValue() < minVal):
                minVal = self.testedDice.getValue()
                pass
            self.assertGreaterEqual(self.testedDice.getValue, 0)
            self.assertLess(self.testedDice.getValue(),constants.N_FACES_DICE)
            pass
        self.assertEqual(maxVal, constants.N_FACES_DICE-1)
        self.assertEqual(minVal, 0)
        print 'PASS: dice.roll() always generates numbers between', minVal, 'and', maxVal, 'for', constants.N_FACES_DICE, '-sided dice for', nTests, 'tests.'