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

    def testGetValue(self):
        testedDice = Dice()
        testedDice.currentValue = constants.DiceValues.heal
        self.assertEqual(testedDice.getValueAsString(), 'heal')


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
        testedPlayer.setDiceWithString('a213H1')  # Also 'test' conversion to lower-case
        self.assertEqual(testedPlayer.playerDice[0], constants.DiceValues.attack)
        self.assertEqual(testedPlayer.playerDice[1], constants.DiceValues.two)
        self.assertEqual(testedPlayer.playerDice[2], constants.DiceValues.one)
        self.assertEqual(testedPlayer.playerDice[3], constants.DiceValues.three)
        self.assertEqual(testedPlayer.playerDice[4], constants.DiceValues.heal)
        self.assertEqual(testedPlayer.playerDice[5], constants.DiceValues.one)
        self.assertFalse(testedPlayer.playerDice[5] == constants.DiceValues.two)
        # Assertion when accessing more dice than we have
        try:
            b = testedPlayer.setDiceWithString("1")
            self.fail("Should have asserted")
        except AssertionError, e:
            self.assertEquals( "Need right string length for the number of dice", e.message )

        # Assertion when accessing more dice than we have
        try:
            b = testedPlayer.setDiceWithString("a213G1")
            self.fail("Should have asserted")
        except AssertionError, e:
            self.assertEquals( "Unknown dice value in diceString", e.message )

    def testProcessRoll(self):
        testedPlayer = Player()
        # Assign dice values
        testedPlayer.setDiceWithString("a3a21h")
        testedPlayer.remainingRolls = 0
        # Process play
        testedPlayer.processRoll()
        testedPlayer.addPoints()
        # Assert
        self.assertEqual(testedPlayer.attack(), 2)
        self.assertEqual(testedPlayer.healDice, 1)
        self.assertEqual(testedPlayer.points, 0)
        testedPlayer.resetPlayer()
        # Assign dice values
        testedPlayer.setDiceWithString("232232")
        testedPlayer.remainingRolls = 0
        # Process roll
        testedPlayer.processRoll()
        testedPlayer.addPoints()
        # Assert
        self.assertEqual(testedPlayer.attack(), 0)
        self.assertEqual(testedPlayer.healDice, 0)
        self.assertEqual(testedPlayer.points, 3)
        testedPlayer.resetPlayer()
        # Assign dice values
        testedPlayer.setDiceWithString("332232")
        # Process play
        testedPlayer.processRoll()
        testedPlayer.addPoints()
        # Assert
        self.assertEqual(testedPlayer.attack(), 0)
        self.assertEqual(testedPlayer.healDice, 0)
        self.assertEqual(testedPlayer.points, 0)
        testedPlayer.remainingRolls = 0
        testedPlayer.addPoints()
        self.assertEqual(testedPlayer.points, 5)

        
    def testGetPlayerDice(self):
        testedPlayer = Player()
        testedPlayer.setDiceWithString("a3a21h")
        testedPlayer.remainingRolls = 0
        resultDiceList = testedPlayer.getPlayerDice()
        inputDiceList = []
        inputDiceList.append(constants.DiceValues.attack.name)
        inputDiceList.append(constants.DiceValues.three.name)
        inputDiceList.append(constants.DiceValues.attack.name)
        inputDiceList.append(constants.DiceValues.two.name)
        inputDiceList.append(constants.DiceValues.one.name)
        inputDiceList.append(constants.DiceValues.heal.name)
        self.assertEqual(resultDiceList, inputDiceList)