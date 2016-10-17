from kingAgent import KingAgent
from game import Game

student = KingAgent(0.9, 0.1, 0.8)

#Training vars
playing = True
cycles = 0
cycleLim = 1000
count = 0

while(cycles < cycleLim):
    cycles += 1
    while(playing):
            nextState = student.act()
            count += 1
            if(student.remainingRolls == 0):
                student.setPlayerTurn()
            playing = not (student.didPlayerWin() or student.didPlayerLose())
            if(count % 1000 == 0):
                print 'Cycle:', cycles, 'is taking more than', count, 'movements'
                print 'Currently got:', student.points, 'points'
    if(cycles % 100 == 0):
        print 'Cycle:', cycles, 'took', count, 'movements'
    student.resetPlayer()
    count = 0
