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


class TestEpochHandler(unittest.TestCase):
    def testStager(self):
        explFraction = 0.4
        trainFracion = 0.3
        cycles = 10
        testedHandler = EpochHandler(cycles, explFraction, trainFracion)
        auxPlayer = KingAgent()
        # First stage boundary
        inCycles = 0
        self.assertEqual(testedHandler.stage, 0)
        testedHandler.stageMonitoring(inCycles, auxPlayer)
        self.assertEqual(testedHandler.stage, 1)
        # Skipping forward prevention
        testedHandler.stageMonitoring(cycles, auxPlayer)
        self.assertEqual(testedHandler.stage, 1)
        # Second stage boundary
        inCycles = cycles * (explFraction)
        testedHandler.stageMonitoring(inCycles, auxPlayer)
        self.assertEqual(testedHandler.stage, 2)
        # Skipping back prevention
        testedHandler.stageMonitoring(0, auxPlayer)
        self.assertEqual(testedHandler.stage, 2)
        # Third stage boundary
        inCycles = cycles * (explFraction + trainFracion)
        testedHandler.stageMonitoring(inCycles, auxPlayer)
        self.assertEqual(testedHandler.stage, 3)


class TestMonitor(unittest.TestCase):
    def testUpdateTurn(self):
        auxPlayer = KingAgent()
        testedMonitor = Monitor()
        testedMonitor.updateTurn(auxPlayer)
        self.assertEqual(0, testedMonitor.movementCount)
        auxPlayer.setPlayerTurn()
        testedMonitor.updateTurn(auxPlayer)
        self.assertEqual(1, testedMonitor.movementCount)

    def testCycleStats(self):
        cycles1 = 3
        cycles2 = 6
        outputFreq = 3
        averages = [1, 4]
        testedMonitor = Monitor(cycles2, outputFreq)
        for c in range(cycles1):
            testedMonitor.movementCount = c
            testedMonitor.cycleStats(c)
        self.assertEqual(testedMonitor.averageMoves, averages[0])
        for c in range(cycles1, cycles2):
            testedMonitor.movementCount = c
            testedMonitor.cycleStats(c)
        self.assertEqual(testedMonitor.averageMoves, averages[1])

