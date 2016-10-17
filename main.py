from kingAgent import KingAgent
from game import Game

student = KingAgent(0.9, 0.1, 0.8)

#Training vars
playing = True
cycles = 0
cycleLim = 10000
count = 0
text_file = open("Output.txt", "w")
while(cycles < cycleLim):
    cycles += 1
    student.resetPlayer()
    student.setPlayerTurn()
    playing = True
    while(playing):
            nextState = student.act()
            count += 1
            if(student.remainingRolls == 0):
                student.setPlayerTurn()
            playing = not (student.didPlayerWin() or student.didPlayerLose())
            '''
            if(count % 100 == 0):
                print 'Cycle:', cycles, 'is taking more than', count, 'movements'
                print 'Currently got:', student.points, 'points'
            '''

    if(cycles % 200 == 0):
        print 'Cycle:', cycles, 'took', count, 'movements'
        print 'States visited', len(student.states)
    if(cycles % 100 == 0):  
        outputString ="%d %d\n" % (cycles, count)
        text_file.write(outputString)
    count = 0
text_file.close()
