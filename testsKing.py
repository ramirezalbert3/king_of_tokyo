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
            if (testedDice.currentValue > maxVal):
                maxVal = testedDice.currentValue
            if (testedDice.currentValue < minVal):
                minVal = testedDice.currentValue
            self.assertGreaterEqual(testedDice.currentValue, 0)
            self.assertLess(testedDice.currentValue, constants.N_FACES_DICE)
        self.assertEqual(maxVal, constants.N_FACES_DICE-1)
        self.assertEqual(minVal, 0)

    def testKeep(self):
        testedDice = Dice()
        nTests = 3
        testedDice.roll()
        diceVal = testedDice.currentValue
        testedDice.keepDice()
        for j in range(nTests):
            testedDice.roll()
            self.assertEqual(diceVal, testedDice.currentValue)


class TestPlayer(unittest.TestCase):

    def testInit(self):
        testedPlayer = Player()
        self.assertEqual(testedPlayer.ID, Player.nPlayers-1)
        testedPlayer2 = Player()
        self.assertNotEqual(testedPlayer.ID, Player.nPlayers-1)
        self.assertEqual(testedPlayer2.ID, Player.nPlayers-1)
        initialNumDice = len(testedPlayer.playerDice)
        self.assertEqual(initialNumDice, constants.STARTING_DICE_NUMBER)

    def testWin(self):
        testedPlayer = Player()
        self.assertEqual(testedPlayer.points, 0)
        self.assertFalse(testedPlayer.didPlayerWin())
        while(not testedPlayer.didPlayerWin()):
            if(not testedPlayer.isItPlayerTurn()):
                testedPlayer.setPlayerTurn()
            testedPlayer.play()
        self.assertEqual(testedPlayer.points, 20)
        self.assertTrue(testedPlayer.didPlayerWin())
        testedPlayer.play()
        self.assertEqual(testedPlayer.points, 20)

    def testLose(self):
        testedPlayer = Player()
        self.assertFalse(testedPlayer.didPlayerLose())
        testedPlayer.takeDamage(5)
        self.assertFalse(testedPlayer.didPlayerLose())
        self.assertEqual(testedPlayer.lives, constants.MAX_LIVES-5)
        testedPlayer.takeDamage(5)
        self.assertTrue(testedPlayer.didPlayerLose())
        self.assertEqual(testedPlayer.lives, 0)
        testedPlayer.takeDamage(1)
        self.assertEqual(testedPlayer.lives, 0)

    def testSetDiceWithString(self):
        testedPlayer = Player()
        # Also 'test' conversion to lower-case
        testedPlayer.setDiceWithString('a213H1')
        self.assertEqual(testedPlayer.playerDice[0], constants.DiceValues.attack)
        self.assertEqual(testedPlayer.playerDice[1], constants.DiceValues.two)
        self.assertEqual(testedPlayer.playerDice[2], constants.DiceValues.one)
        self.assertEqual(testedPlayer.playerDice[3], constants.DiceValues.three)
        self.assertEqual(testedPlayer.playerDice[4], constants.DiceValues.heal)
        self.assertEqual(testedPlayer.playerDice[5], constants.DiceValues.one)
        # Test __eq__ overdrive
        self.assertTrue(testedPlayer.playerDice[5] == constants.DiceValues.one)
        self.assertFalse(testedPlayer.playerDice[5] == constants.DiceValues.two)
        # Assertion for wrong length inputs
        try:
            testedPlayer.setDiceWithString("1")
            self.fail("Should have asserted")
        except AssertionError, e:
            self.assertEquals("Need right string length for the number of dice", e.message)

        # Assertion for wrong character input
        try:
            testedPlayer.setDiceWithString("a213G1")
            self.fail("Should have asserted")
        except AssertionError, e:
            self.assertEquals("Unknown dice value in diceString", e.message)

    def testGetDiceAsString(self):
        testedPlayer = Player()
        inputDiceList = "a3a21h"
        testedPlayer.setDiceWithString(inputDiceList)
        resultDiceList = testedPlayer.getDiceAsString()
        self.assertEqual(resultDiceList, inputDiceList)

    def testCountPoints(self):
        testedPlayer = Player()
        # Test cases
        diceCase1 = [0, 0, 3]
        diceCase2 = [0, 6, 0]
        diceCase3 = [1, 2, 2]
        inputPointDiceList = [diceCase1, diceCase2, diceCase3]
        expectedResult = [3, 5, 0]
        # Test process
        for i in range(len(expectedResult)):
            testedPlayer.pointsDice = inputPointDiceList[i]
            resultPoints = testedPlayer.countPoints()
            self.assertEqual(expectedResult[i], resultPoints)

    def testAddPoints(self):
        # Modified/extended testCountPoints (dependency)
        testedPlayer = Player()
        # Test cases
        diceCase1 = [2, 2, 1]
        diceCase2 = [5, 1, 0]
        diceCase3 = [0, 2, 4]
        inputPointDiceList = [diceCase1, diceCase2, diceCase3]
        initialPoints = 14
        testedPlayer.points = initialPoints
        expectedResult = [14, 17, 20]
        # Test return on remaining rolls
        testedPlayer.pointsDice = [0, 2, 4]  # Should add points if no return
        testedPlayer.addPoints()
        self.assertEqual(testedPlayer.points, initialPoints)
        # Rest of the test
        testedPlayer.remainingRolls = 0
        for i in range(len(expectedResult)):
            testedPlayer.pointsDice = inputPointDiceList[i]
            testedPlayer.addPoints()
            self.assertEqual(expectedResult[i], testedPlayer.points)

    def testProcessRoll(self):
        testedPlayer = Player()
        # Test cases
        diceCase1 = "a3a21h"
        diceCase2 = "232232"
        diceCase3 = "332232"
        inputPointDiceList = [diceCase1, diceCase2, diceCase3]
        diceResult1 = [1, 1, 1]
        diceResult2 = [0, 4, 2]
        diceResult3 = [0, 3, 3]
        expectedPoints = [diceResult1, diceResult2, diceResult3]
        expectedAttack = [2, 0, 0]
        expectedHeal = [1, 0, 0]
        # Test procedure
        for i in range(len(expectedPoints)):
            testedPlayer.setDiceWithString(inputPointDiceList[i])
            testedPlayer.processDice()
            self.assertEqual(expectedPoints[i], testedPlayer.pointsDice)
            self.assertEqual(expectedAttack[i], testedPlayer.attack())
            self.assertEqual(expectedHeal[i], testedPlayer.healDice)
