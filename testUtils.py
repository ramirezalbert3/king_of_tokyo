from utils import Stager
from utils import Monitor
from utils import EpochHandler
from utils import TurnHandler
from constants import ROLLS_PER_TURN
from kingAgent import KingAgent
import unittest


class TestTurnHandler(unittest.TestCase):
    def testTurnHandler(self):
        expectedPlayers = 3
        auxPlayer1 = KingAgent()
        auxPlayer2 = KingAgent()
        auxPlayer3 = KingAgent()
        playerList = [auxPlayer1, auxPlayer2, auxPlayer3]
        playerList[0].setPlayerTurn()
        testedHandler = TurnHandler()
        testedHandler.addPlayers(playerList)
        self.assertEqual(testedHandler.numberOfPlayers, expectedPlayers)
        for loops in range(50):
            for player in playerList:
                    player.resetPlayer()
            playerList[0].setPlayerTurn()
            testedHandler.playingID = 0
            for i in range(loops):
                for player in playerList:
                    player.act()
                testedHandler.setTurn(playerList)
            playerPlaying = (loops / ROLLS_PER_TURN) % expectedPlayers
            self.assertEqual(testedHandler.playingID, playerPlaying)


class TestStager(unittest.TestCase):
    def testStager(self):
        testedStager = Stager()
        pass
