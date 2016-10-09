from player import Player


def GameOver(pList):
    gameOver = False
    for p in pList:
        if(p.didPlayerWin()):
            print 'Player', p.ID, 'won :)'
            break
        elif(p.didPlayerLose()):
            print 'Player', p.ID, 'lost :('
            break
    gameOver = p.didPlayerWin() or p.didPlayerLose()
    return gameOver

pList = []
for i in range(2):
    pList.append(Player())

playing = True

while(playing):
    for i, p in enumerate(pList):
        p.setPlayerTurn()
        print 'Player', i+1, 'turn'
        # print '-----Before rolling dice-----'
        p.printPlayerStatus()
        while(p.isItPlayerTurn()):
            p.play()
        # print '-----After rolling dice------'
        # p.printPlayerStatus()
        # p.printPlayerDice()
        for j, otherPlayer in enumerate(pList):
            if (i != j):
                otherPlayer.takeDamage(p.attack())
        print '-----------------------------'
        playing = not GameOver(pList)
        if(not playing):
            break
