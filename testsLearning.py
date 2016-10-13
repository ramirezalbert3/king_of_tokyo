import unittest
import constants
from game import Game
from kingAgent import KingAgent


class TestGame(unittest.TestCase):

    def testGetReward(self):
        testedGame = Game()
        # Multiple cases
        # 1. No reward due to remaining rolls
        startingPoints = 3
        remainingRolls = 2
        playerDice = "a123ha"
        expectedReward = 0
        # Create state and check reward
        state = [startingPoints, playerDice, remainingRolls]
        reward = testedGame.getReward(state)
        self.assertEqual(reward, expectedReward)
        # 2. Added reward due to dice
        startingPoints = 0
        remainingRolls = 0
        playerDice = "a12333"
        expectedReward = 3
        # Create state and check reward
        state = [startingPoints, playerDice, remainingRolls]
        reward = testedGame.getReward(state)
        self.assertEqual(reward, expectedReward)
        # 3. Reward equal to initial points
        startingPoints = 17
        remainingRolls = 0
        playerDice = "a123h3"
        expectedReward = 17
        # Create state and check reward
        state = [startingPoints, playerDice, remainingRolls]
        reward = testedGame.getReward(state)
        self.assertEqual(reward, expectedReward)


class TestKingAgent(unittest.TestCase):
    def testGetLegalActions(self):
        testedAgent = KingAgent()
        listedActions = []
        for i in range(2 ** constants.STARTING_DICE_NUMBER):
            listedActions.append(i)
        self.assertEqual(testedAgent.getLegalActions(), listedActions)

    def testDoWeKeepDice(self):
        testedAgent = KingAgent()
        # Case definition
        legalAction = []
        legalAction.append(1)  # Legal action 0: 0001 = 1
        legalAction.append(14)  # Legal action 1: 1110 = 14

        def fTestKeep(actionID, diceToKeep):
            return testedAgent.doWeKeepDice(legalAction[actionID], diceToKeep)

        # Legal action 0
        self.assertTrue(fTestKeep(0, 0))
        self.assertFalse(fTestKeep(0, 1))

        # Legal action 1
        self.assertFalse(fTestKeep(1, 0))
        self.assertTrue(fTestKeep(1, 2))
        self.assertTrue(fTestKeep(1, 3))

        # Assertion when accessing more dice than we have
        try:
            fTestKeep(1, constants.STARTING_DICE_NUMBER+1)
            self.fail("Should have asserted")
        except AssertionError, e:
            self.assertEquals("Keeping more dice than we have", e.message)
