from kingAgent import KingAgent
from stager import Stager


student = KingAgent(0.7, 0.1, 0.8)
stager = Stager(2500, 10, 'Output.txt', 250)


# Training vars
playing = True

while(stager.areWeCycling()):
    student.resetPlayer()
    student.setPlayerTurn()
    playing = True
    while(playing):
            nextState = student.act()
            stager.updateCount()
            if(student.remainingRolls == 0):
                student.setPlayerTurn()
            playing = not (student.didPlayerWin() or student.didPlayerLose())
    stager.updateCycle()
