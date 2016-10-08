import unittest
import constants
from dice import Dice
from player import Player


class TestDice(unittest.TestCase):

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

    def testKeep(self):
        testedDice = Dice()
        nTests = 3
        testedDice.roll()
        diceVal = testedDice.getValue()
        testedDice.keepDice()
        for j in range(nTests):
            testedDice.roll()
            self.assertEqual(diceVal, testedDice.getValue())


class TestPlayer(unittest.TestCase):

    def testInit(self):
        testedPlayer = Player()
        self.assertEqual(testedPlayer.ID, Player.nPlayers)
        testedPlayer2 = Player()
        self.assertNotEqual(testedPlayer.ID, Player.nPlayers)
        self.assertEqual(testedPlayer2.ID, Player.nPlayers)
        self.assertEqual(len(testedPlayer.playerDice), constants.STARTING_DICE_NUMBER)

    def testProcessRoll(self):
        testedPlayer = Player()
        # Assign dice values
        # One dice for each value, two for attack
        testedPlayer.playerDice[0].currentValue = constants.DiceValues.attack
        testedPlayer.playerDice[1].currentValue = constants.DiceValues.three
        testedPlayer.playerDice[2].currentValue = constants.DiceValues.attack
        testedPlayer.playerDice[3].currentValue = constants.DiceValues.two
        testedPlayer.playerDice[4].currentValue = constants.DiceValues.one
        testedPlayer.playerDice[5].currentValue = constants.DiceValues.heal
        # Process play
        testedPlayer.processRoll()
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
        # Process roll
        testedPlayer.processRoll()
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
        testedPlayer.processRoll()
        # Assert
        self.assertEqual(testedPlayer.attackDice, 0)
        self.assertEqual(testedPlayer.healDice, 0)
        testedPlayer.addPoints()
        self.assertEqual(testedPlayer.points, 5)
