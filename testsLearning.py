import unittest
import constants
from agent import Agent
from kingAgent import KingAgent
from collections import Counter


class testAgent(unittest.TestCase):
    def testAgent(self):
        alpha = 0.7
        epsilon = 0.05
        gamma = 0.8
        testedAgent = Agent(alpha, epsilon, gamma)
        # First state
        firstPoints = 0
        firstLives = 8
        firstDice = '1222ah'
        firstRemainingRolls = 3
        firstState = (firstPoints, firstLives, firstDice, firstRemainingRolls)
        # Second state
        secondPoints = 0
        secondLives = 10
        secondDice = '123aah'
        secondRemainingRolls = 3
        secondState = (secondPoints, secondLives, secondDice, secondRemainingRolls)
        # Test unvisited state
        self.assertIsNone(testedAgent.getPolicy(firstState))
        # Parameters needed for update()
        reward = 3
        firstAction = 8
        # Test update: first pass
        resQ = 2.1
        resV = resQ
        testedAgent.update(firstState, firstAction, reward, secondState)
        roundQ = round(testedAgent.getQValue(firstState, firstAction), 2)
        roundV = round(testedAgent.getValue(firstState), 2)
        self.assertEqual(roundQ, resQ)
        self.assertEqual(roundV, resV)
        self.assertEqual(testedAgent.getPolicy(firstState), firstAction)
        self.assertIsNone(testedAgent.getPolicy(secondState))
        # Test update: same state different action
        reward = 2
        secondAction = 2
        resQ = 1.4
        testedAgent.update(firstState, secondAction, reward, secondState)
        roundQ = round(testedAgent.getQValue(firstState, secondAction), 2)
        roundV = round(testedAgent.getValue(firstState), 2)
        self.assertEqual(roundQ, resQ)
        self.assertEqual(roundV, resV)
        self.assertEqual(testedAgent.getPolicy(firstState), firstAction)
        # Test update: same state, same action, more reward
        reward = 8
        secondAction = 2
        resQ = 6.02
        resV = resQ
        testedAgent.update(firstState, secondAction, reward, secondState)
        roundQ = round(testedAgent.getQValue(firstState, secondAction), 2)
        roundV = round(testedAgent.getValue(firstState), 2)
        self.assertEqual(roundQ, resQ)
        self.assertEqual(roundV, resV)
        self.assertEqual(testedAgent.getPolicy(firstState), secondAction)
        # Test update: from second to first state
        reward = 1
        thirdAction = 3
        resQ = 4.07
        resV = resQ
        testedAgent.update(secondState, thirdAction, reward, firstState)
        roundQ = round(testedAgent.getQValue(secondState, thirdAction), 2)
        roundV = round(testedAgent.getValue(secondState), 2)
        self.assertEqual(roundQ, resQ)
        self.assertEqual(roundV, resV)
        self.assertEqual(testedAgent.getPolicy(secondState), thirdAction)


class TestKingAgent(unittest.TestCase):

    def testAct(self):
        testedAgent = KingAgent(1, 0, 1)  # Full learning, no exploration
        expectedReward = 6
        testedAgent.setPlayerTurn()
        testedAgent.setDiceWithString('333333')
        testedAgent.remainingRolls = 1
        initState = testedAgent.getState([testedAgent])
        policy = 63  # Keep all dice
        testedAgent.states[initState] = 1
        testedAgent.Policy[initState] = policy
        testedAgent.act([testedAgent])
        self.assertEqual(testedAgent.states[initState], 2)
        self.assertEqual(testedAgent.Q[initState, policy], expectedReward)
        self.assertEqual(testedAgent.V[initState], expectedReward)
        self.assertEqual(testedAgent.Policy[initState], policy)

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

    def testGetState(self):
        # It's important we can use the state to index a Counter
        auxCounter = Counter()
        testedAgent = KingAgent()
        state = testedAgent.getState([testedAgent])
        self.assertEqual(auxCounter[state], 0)
        auxCounter[state] = 1
        self.assertEqual(auxCounter[state], 1)
        # Check the state format
        startingPoints = 0
        remainingRolls = constants.ROLLS_PER_TURN
        playerDice = "111111"
        lives = 10
        oppLives = 10
        inputState = (startingPoints, lives, playerDice, remainingRolls, oppLives)
        self.assertEqual(inputState, testedAgent.getState([testedAgent]))

    def testGetAction(self):
        alpha = 0.7
        epsilon = 0.2
        gamma = 0.8
        testedAgent = KingAgent(alpha, epsilon, gamma)
        nTests = 100
        count = Counter()
        state = testedAgent.getState([testedAgent])
        expectedPolicy = 1
        testedAgent.Policy[state] = expectedPolicy
        testedAgent.states[state] = 2
        for i in range(nTests):
            resAction = testedAgent.getAction(state)
            count[resAction] += 1
        resPolicy = count[expectedPolicy]
        base = (1-epsilon) * nTests
        greaterThan = base - nTests / 10
        LessThan = base + nTests / 10
        self.assertGreaterEqual(resPolicy, greaterThan)
        self.assertLessEqual(resPolicy, LessThan)

    def testGetReward(self):
        testedAgent = KingAgent()
        lives = 10
        minOppLives = 10
        # Multiple cases
        stateList = []
        rewardList = []
        # 1. No reward due to remaining rolls
        startingPoints = 3
        remainingRolls = 2
        playerDice = "test"
        expectedReward = 0
        stateList.append([startingPoints, lives, playerDice, remainingRolls, minOppLives])
        rewardList.append(expectedReward)
        # 2. Reward expected
        startingPoints = 3
        remainingRolls = 0
        playerDice = "test"
        expectedReward = 3
        stateList.append([startingPoints, lives, playerDice, remainingRolls, minOppLives])
        rewardList.append(expectedReward)

        # Test run
        for i in range(len(stateList)):
            reward = testedAgent.getReward(stateList[i])
            self.assertEqual(reward, rewardList[i])

    def testKeepDice(self):
        testedAgent = KingAgent()
        testedAgent.roll()
        state = testedAgent.getState([testedAgent])
        action = 20  # Dice kept as follows 010 100
        keptDice1 = testedAgent.playerDice[2].currentValue
        keptDice2 = testedAgent.playerDice[4].currentValue
        testedAgent.keepDice(state, action)
        testedAgent.roll()
        resDice1 = testedAgent.playerDice[2].currentValue
        resDice2 = testedAgent.playerDice[4].currentValue
        self.assertEqual(keptDice1, resDice1)
        self.assertEqual(keptDice2, resDice2)
