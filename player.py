import constants
from dice import Dice


class Player:
    nPlayers = 0

    def __init__(self):
        Player.nPlayers += 1
        self.ID = Player.nPlayers
        self.lives = constants.MAX_LIVES
        self.points = 0
        self.playerDice = []
        for i in range(constants.STARTING_DICE_NUMBER):
            self.playerDice.append(Dice())
        self.remainingRolls = constants.ROLLS_PER_TURN
        self.attackDice = 0
        self.healDice = 0
        self.pointsDice = [0, 0, 0]
        self.myTurn = False
        self.playerWon = False
        self.playerLost = False

    def takeDamage(self, damagePoints):
        self.lives -= damagePoints
        if (self.lives <= 0):
            self.lives = 0
            self.myTurn = False
            self.playerLost = True

    def healDamage(self, healAmmount):
        self.lives += healAmmount
        if (self.lives > constants.MAX_LIVES):
            self.lives = constants.MAX_LIVES

    def attack(self):
        return self.attackDice

    def resetAllDice(self):
        for currentDice in self.playerDice:
            currentDice.reset()
        self.attackDice = 0
        self.healDice = 0
        self.pointsDice = [0, 0, 0]
        self.remainingRolls = constants.ROLLS_PER_TURN

    def resetPlayer(self):
        self.resetAllDice()
        self.lives = constants.MAX_LIVES
        self.points = 0
        self.myTurn = False
        self.playerWon = False
        self.playerLost = False

    def processRoll(self):
        for currentDice in self.playerDice:
            if(currentDice.getValue() == constants.DiceValues.attack):
                self.attackDice += 1
            elif(currentDice.getValue() == constants.DiceValues.heal):
                self.healDice += 1
            else:
                self.pointsDice[currentDice.getValue()] += 1

    def addPoints(self):
        for i, roundPoints in enumerate(self.pointsDice):
            # Points if 3 equal dice
            if(roundPoints // constants.MIN_DICE_FOR_POINTS):
                # Points per 3 equal dice
                self.points += (i + 1)
                # Points per extra equal dice after that
                self.points += roundPoints % constants.MIN_DICE_FOR_POINTS
        if(self.points >= constants.MAX_POINTS):
            self.points = constants.MAX_POINTS
            self.playerWon = True
            self.myTurn = False

    def roll(self):
        self.attackDice = 0
        self.healDice = 0
        self.pointsDice = [0, 0, 0]
        for currentDice in self.playerDice:
            if(not currentDice.kept):
                currentDice.roll()

    def getPlayerDice(self):
        diceList = []
        for currentDice in self.playerDice:
            diceList.append(currentDice.getValueAsString())
        return diceList

    def isItPlayerTurn(self):
        return (self.myTurn)

    def setPlayerTurn(self):
        self.resetAllDice()
        self.myTurn = True

    def getPlayerID(self):
        return self.ID

    def printPlayerStatus(self):
        # print 'Player', self.ID
        print 'Points:', self.points
        print 'Lives:', self.lives

    def printPlayerDice(self):
        print 'Attack dice:', self.attackDice
        print 'Heal dice:', self.healDice
        print 'Point [1,2,3] dice:', self.pointsDice

    def play(self):
        if (not self.myTurn or self.playerWon or self.playerLost):
            return
        if (self.remainingRolls != 0):
            self.roll()
            self.remainingRolls -= 1
            self.processRoll()
        else:
            # Add points, heal and ?attack?
            self.healDamage(self.healDice)
            self.addPoints()
            self.remainingRolls = constants.ROLLS_PER_TURN
            self.myTurn = False

    def didPlayerWin(self):
        return self.playerWon

    def didPlayerLose(self):
        return self.playerLost
