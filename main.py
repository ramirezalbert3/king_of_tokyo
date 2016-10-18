from kingAgent import KingAgent


student = KingAgent(0.7, 0.1, 0.8)


# Training vars
playing = True
cycles = 0
cycleLim = 2500
count = 0

# Output to file
text_file = open("Output.txt", "w")
outputString ="%s %s %s\n" % ("Cycles", "Movements_cycle", "Visited_states")
text_file.write(outputString)

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

    if(cycles % (cycleLim / 10) == 0):
        print 'Cycle:', cycles, 'took', count, 'movements'
        print 'States visited', len(student.states)
    if(cycles % (cycleLim / 250) == 0):
        outputString ="%d %d %d\n" % (cycles, count, len(student.states))
        text_file.write(outputString)
    count = 0
text_file.close()
