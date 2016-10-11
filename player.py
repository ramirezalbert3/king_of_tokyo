import constants
from dice import Dice


class Player:
    nPlayers = 0

    def __init__(self):
        self.ID = Player.nPlayers
        Player.nPlayers += 1
        self.lives = constants.MAX_LIVES
        self.points = 0
        self.myTurn = False
        self.playerWon = False
        self.playerLost = False
        self.playerDice = []
        for i in range(constants.STARTING_DICE_NUMBER):
            self.playerDice.append(Dice())
        self.remainingRolls = constants.ROLLS_PER_TURN
        self.attackDice = 0
        self.healDice = 0
        self.pointsDice = [0, 0, 0]

# Play methods
    def processRoll(self):
        for currentDice in self.playerDice:
            if(currentDice.currentValue == constants.DiceValues.attack):
                self.attackDice += 1
            elif(currentDice.currentValue == constants.DiceValues.heal):
                self.healDice += 1
            else:
                self.pointsDice[currentDice.currentValue] += 1

    def addPoints(self):
        if (self.remainingRolls != 0):
            return
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

# Setters
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

    def setPlayerTurn(self):
        self.resetAllDice()
        self.myTurn = True

    def setDiceWithString(self, diceString):
        assert (len(diceString) == len(self.playerDice)), "setDiceWithString: provide a right string for the number of dice"
        diceString = diceString.lower()
        for i, currentDice in enumerate(self.playerDice):
            if(diceString[i] == 'h'):
                currentDice.currentValue = constants.DiceValues.heal
            elif(diceString[i] == 'a'):
                currentDice.currentValue = constants.DiceValues.attack
            elif(diceString[i] == '1'):
                currentDice.currentValue = constants.DiceValues.one
            elif(diceString[i] == '2'):
                currentDice.currentValue = constants.DiceValues.two
            elif(diceString[i] == '3'):
                currentDice.currentValue = constants.DiceValues.three
            else:
                assert (False), "setDiceWithString: Unknown dice value in diceString"

# Getters & Printers
    def attack(self):
        return self.attackDice

    def isItPlayerTurn(self):
        return (self.myTurn)

    def didPlayerWin(self):
        return self.playerWon

    def didPlayerLose(self):
        return self.playerLost

    def getPlayerDice(self):
        diceList = []
        for currentDice in self.playerDice:
            diceList.append(currentDice.getValueAsString())
        return diceList

    def printPlayerStatus(self):  # pragma: no cover
        # print 'Player', self.ID
        print 'Points:', self.points
        print 'Lives:', self.lives

    def printPlayerDice(self):  # pragma: no cover
        print 'Attack dice:', self.attackDice
        print 'Heal dice:', self.healDice
        print 'Point [1,2,3] dice:', self.pointsDice

# Resetters
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
