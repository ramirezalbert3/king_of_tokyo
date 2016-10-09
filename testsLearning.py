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
        # This is a pretty bad test
        self.assertTrue(testedGame.doWeKeepDice(1, 0, 0))
        self.assertTrue(testedGame.doWeKeepDice(8, 3, 0))
        self.assertTrue(testedGame.doWeKeepDice(64, constants.STARTING_DICE_NUMBER, 0))
        self.assertFalse(testedGame.doWeKeepDice(1, constants.STARTING_DICE_NUMBER+1, 0))
        self.assertFalse(testedGame.doWeKeepDice(5, 1, 0))
