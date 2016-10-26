from kingAgent import KingAgent
from utils import Stager


student = KingAgent()
competitor = KingAgent()
playerList = [student, competitor]
stager = Stager(15000, 10, 'Output.txt', 200)

stager.epochHandler.stageMonitoring(0, playerList)
stager.turnHandler.addPlayers(playerList)
playing = True
playerList[0].setPlayerTurn()
while(stager.areWeCycling()):
    for player in playerList:
        player.resetPlayer()
    playerList[0].setPlayerTurn()
    playing = True
    while(playing):
            nextState = student.act()
            stager.updateTurn(playerList)
            for player in playerList:
                playing = playing and not (player.didPlayerWin() or player.didPlayerLose())
    stager.updateCycle(playerList)
