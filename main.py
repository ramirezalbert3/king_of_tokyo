from kingAgent import KingAgent
from utils import Stager
from utils import Monitor

limCycles = 15000
student = KingAgent()
competitor = KingAgent()
playerList = [student, competitor]
stager = Stager(limCycles)
monitor1 = Monitor(limCycles, 10, 'Output.txt', 200)
monitor2 = Monitor(limCycles, 10, 'Output2.txt', 200)

monitor1.epochHandler.stageMonitoring(0, playerList[0])
monitor2.epochHandler.stageMonitoring(0, playerList[1])
stager.turnHandler.addPlayers(playerList)
playing = True

while(stager.areWeCycling()):
    for player in playerList:
        player.resetPlayer()
    playerList[0].setPlayerTurn()
    playing = True
    while(playing):
        for player in playerList:
            player.act(playerList)
        stager.updateTurn(playerList)
        monitor1.updateTurn(playerList[0])
        monitor2.updateTurn(playerList[1])
        for player in playerList:
            playing = playing and not (player.didPlayerWin() or player.didPlayerLose())
    stager.updateCycle()
    monitor1.updateCycle(stager.cyclesPassed, playerList[0])
    monitor2.updateCycle(stager.cyclesPassed, playerList[1])
