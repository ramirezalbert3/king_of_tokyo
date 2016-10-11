import unittest
import constants
from game import Game


class TestGame(unittest.TestCase):

    def testGetState(self):
        testedGame = Game()
        for i in range(1, 5):
            nPlayers = i
            testedGame.resetGame()
            testedGame = Game(nPlayers)
            # State listed: player points, lives, dice, other players lives
            initialState = []
            initialState.append(0)
            initialState.append(constants.MAX_LIVES)
            # getPlayerDice() should already be tested somewhere else
            initialState.append(testedGame.playerList[0].getPlayerDice())
            pProcessed = 1
            while(pProcessed < nPlayers):
                initialState.append(constants.MAX_LIVES)
                pProcessed += 1
            self.assertEqual(testedGame.getState(0), initialState)

    def testGetLegalActions(self):
        testedGame = Game()
        listedActions = []
        for i in range(2 ** constants.STARTING_DICE_NUMBER):
            listedActions.append(i)
        self.assertEqual(testedGame.getLegalActions(0), listedActions)

    def testDoWeKeepDice(self):
        testedGame = Game()
        # Case definition
        legalAction = []
        legalAction.append(1)  # Legal action 0: 0001 = 1
        legalAction.append(14)  # Legal action 1: 1110 = 14

        def fTestKeep(actionID, diceToKeep):
            # Checking only for player one
            return testedGame.doWeKeepDice(legalAction[actionID], diceToKeep, 0)

        # Legal action 0
        self.assertTrue(fTestKeep(0 ,0))
        self.assertFalse(fTestKeep(0, 1))

        # Legal action 1
        self.assertFalse(fTestKeep(1, 0))
        self.assertTrue(fTestKeep(1, 2))
        self.assertTrue(fTestKeep(1, 3))

        # Assertion when accessing more dice than we have
        try:
            b = fTestKeep(1, constants.STARTING_DICE_NUMBER+1)
            self.fail("Should have asserted")
        except AssertionError, e:
            self.assertEquals( "Keeping more dice than we have", e.message )
