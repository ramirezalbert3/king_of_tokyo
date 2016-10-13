import unittest
import constants
from game import Game
from kingAgent import KingAgent


class TestGame(unittest.TestCase):

    def testGetReward(self):
        testedGame = Game()
        # Multiple cases
        stateList = []
        rewardList = []
        # 1. No reward due to remaining rolls
        startingPoints = 3
        remainingRolls = 2
        playerDice = "a123ha"
        expectedReward = 0
        stateList.append([startingPoints, playerDice, remainingRolls])
        rewardList.append(expectedReward)
        # 2. Added reward due to dice
        startingPoints = 0
        remainingRolls = 0
        playerDice = "a12333"
        expectedReward = 3
        stateList.append([startingPoints, playerDice, remainingRolls])
        rewardList.append(expectedReward)
        # 3. Reward equal to initial points
        startingPoints = 17
        remainingRolls = 0
        playerDice = "a123h3"
        expectedReward = 17
        stateList.append([startingPoints, playerDice, remainingRolls])
        rewardList.append(expectedReward)

        # Test run
        for i in range(len(stateList)):
            reward = testedGame.getReward(stateList[i])
            self.assertEqual(reward, rewardList[i])


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
        diceToKeep = 0
        result = testedAgent.doWeKeepDice(legalAction[0], diceToKeep)
        self.assertTrue(result)
        diceToKeep = 1
        result = testedAgent.doWeKeepDice(legalAction[0], diceToKeep)
        self.assertFalse(result)

        # Legal action 1
        diceToKeep = 0
        result = testedAgent.doWeKeepDice(legalAction[1], diceToKeep)
        self.assertFalse(result)
        diceToKeep = 2
        result = testedAgent.doWeKeepDice(legalAction[1], diceToKeep)
        self.assertTrue(result)
        diceToKeep = 3
        result = testedAgent.doWeKeepDice(legalAction[1], diceToKeep)
        self.assertTrue(result)

        # Assertion when accessing more dice than we have
        try:
            fTestKeep(1, constants.STARTING_DICE_NUMBER+1)
            self.fail("Should have asserted")
        except AssertionError, e:
            self.assertEquals("Keeping more dice than we have", e.message)
