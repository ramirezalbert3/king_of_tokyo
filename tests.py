import unittest
import constants
from dice import Dice
from player import Player 

class TestDice(unittest.TestCase):

    def testInit(self):
        testedDice = Dice()
        self.assertEqual(testedDice.currentValue, 0)
        self.assertEqual(testedDice.nFaces, constants.N_FACES_DICE)
        # print '[DICE] PASS: init() to', testedDice.currentValue, 'with', testedDice.nFaces, 'faces' 

    def testRoll(self):
        testedDice = Dice()
        maxVal = 0
        minVal = constants.N_FACES_DICE
        nTests = 50
        for i in range(nTests):
            testedDice.roll()
            if (testedDice.getValue() > maxVal):
                maxVal = testedDice.getValue()
            if (testedDice.getValue() < minVal):
                minVal = testedDice.getValue()
            self.assertGreaterEqual(testedDice.getValue, 0)
            self.assertLess(testedDice.getValue(),constants.N_FACES_DICE)
        self.assertEqual(maxVal, constants.N_FACES_DICE-1)
        self.assertEqual(minVal, 0)
        # print '[DICE] PASS: roll() always generates numbers between', minVal, 'and', maxVal, 'for', constants.N_FACES_DICE, '-sided dice for', nTests, 'tests.'

class TestPlayer(unittest.TestCase):

    def testInit(self):
        testedPlayer = Player()
        self.assertEqual(testedPlayer.ID,Player.nPlayers)
        testedPlayer2 = Player()
        self.assertNotEqual(testedPlayer.ID,Player.nPlayers)
        self.assertEqual(testedPlayer2.ID,Player.nPlayers)
        self.assertEqual(len(testedPlayer.playerDice),constants.STARTING_DICE_NUMBER)