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
            self.assertLess(testedDice.getValue(), constants.N_FACES_DICE)
        self.assertEqual(maxVal, constants.N_FACES_DICE-1)
        self.assertEqual(minVal, 0)
        # print '[DICE] PASS: roll() always generates numbers between', minVal, 'and', maxVal, 'for', constants.N_FACES_DICE, '-sided dice for', nTests, 'tests.'


class TestPlayer(unittest.TestCase):

    def testInit(self):
        testedPlayer = Player()
        self.assertEqual(testedPlayer.ID, Player.nPlayers)
        testedPlayer2 = Player()
        self.assertNotEqual(testedPlayer.ID, Player.nPlayers)
        self.assertEqual(testedPlayer2.ID, Player.nPlayers)
        self.assertEqual(len(testedPlayer.playerDice), constants.STARTING_DICE_NUMBER)

    def testProcessPlay(self):
        testedPlayer = Player()

        # Assign dice values
        # One dice for each value, two for attack
        for i, currentDice in enumerate(testedPlayer.playerDice):
            currentDice.currentValue = i
        testedPlayer.playerDice[5].currentValue = constants.DiceValues.attack
        # Process play
        testedPlayer.processPlay()
        # Assert
        self.assertEqual(testedPlayer.attackDice, 2)
        self.assertEqual(testedPlayer.healDice, 1)
        testedPlayer.addPoints()
        self.assertEqual(testedPlayer.points, 0)

        testedPlayer.resetPlayer()
        # Assign dice values
        testedPlayer.playerDice[0].currentValue = constants.DiceValues.two
        testedPlayer.playerDice[1].currentValue = constants.DiceValues.three
        testedPlayer.playerDice[2].currentValue = constants.DiceValues.two
        testedPlayer.playerDice[3].currentValue = constants.DiceValues.two
        testedPlayer.playerDice[4].currentValue = constants.DiceValues.three
        testedPlayer.playerDice[5].currentValue = constants.DiceValues.two
        # Process play
        testedPlayer.processPlay()
        # Assert
        self.assertEqual(testedPlayer.attackDice, 0)
        self.assertEqual(testedPlayer.healDice, 0)
        testedPlayer.addPoints()
        self.assertEqual(testedPlayer.points, 3)

        testedPlayer.resetPlayer()
        # Assign dice values
        testedPlayer.playerDice[0].currentValue = constants.DiceValues.three
        testedPlayer.playerDice[1].currentValue = constants.DiceValues.three
        testedPlayer.playerDice[2].currentValue = constants.DiceValues.two
        testedPlayer.playerDice[3].currentValue = constants.DiceValues.two
        testedPlayer.playerDice[4].currentValue = constants.DiceValues.three
        testedPlayer.playerDice[5].currentValue = constants.DiceValues.two
        # Process play
        testedPlayer.processPlay()
        # Assert
        self.assertEqual(testedPlayer.attackDice, 0)
        self.assertEqual(testedPlayer.healDice, 0)
        testedPlayer.addPoints()
        self.assertEqual(testedPlayer.points, 5)
