from kingAgent import KingAgent
from utils import Stager
from utils import Monitor

limCycles = 15000
student = KingAgent()
competitor = KingAgent()
playerList = [student, competitor]
stager = Stager(limCycles)
monitor = Monitor(limCycles, 10, 'Output.txt', 200)

monitor.epochHandler.stageMonitoring(0, [student])
stager.turnHandler.addPlayers(playerList)
playing = True
playerList[0].setPlayerTurn()
while(stager.areWeCycling()):
    for player in playerList:
        player.resetPlayer()
    playerList[0].setPlayerTurn()
    playing = True
    while(playing):
        for player in playerList:
            player.act()
        stager.updateTurn(playerList)
        monitor.updateTurn(playerList[0])
        for player in playerList:
            playing = playing and not (player.didPlayerWin() or player.didPlayerLose())
    stager.updateCycle()
    monitor.updateCycle(stager.cyclesPassed, playerList[0])
