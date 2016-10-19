import random


class epochHandler:
    def __init__(self, totalCycles=3000, explorationFraction=0.4, trainingFraction=0.5):
        assert (explorationFraction + trainingFraction) <= 1
        self.explorationCycles = totalCycles * explorationFraction
        self.trainingCycles = totalCycles * (explorationFraction + trainingFraction)
        self.stage = 0

    def setExploration(self, agent):
        print 'Starting exploration!'
        self.stage = 1
        agent.epsilon = 0.5
        agent.alpha = 1
        agent.gamma = 0.8

    def setTraining(self, agent):
        print 'Starting training!'
        self.stage = 2
        agent.epsilon = 0.1
        agent.alpha = 0.7
        agent.gamma = 0.8

    def setPlay(self, agent):
        print 'Starting play phase!'
        self.stage = 3
        agent.epsilon = 0
        agent.alpha = 0.1
        agent.gamma = 0.8

    def stageMonitoring(self, cyclesPassed, agent):
        if(cyclesPassed < self.explorationCycles):
            if(self.stage == 0):
                self.setExploration(agent)
        elif(cyclesPassed < self.trainingCycles):
            if(self.stage == 1):
                self.setTraining(agent)
        elif(self.stage == 2):
            self.setPlay(agent)


class Stager:
    def __init__(self, limCycles=3000, outputFrequency=10, outputFileName='Output.txt', printFrequency=200):
        self.limCycles = limCycles
        self.outputFrequency = outputFrequency
        self.printFrequency = printFrequency
        self.cyclesPassed = 0
        self.movementCount = 0
        self.averageMoves = 0
        self.outputFile = open(outputFileName, 'w')
        outputString = 'Cycles Movements_cycle '
        self.outputFile.write(outputString)
        self.epochHandler = epochHandler(limCycles, 0.4, 0.5)
        explCycles = int(self.epochHandler.explorationCycles)
        trainCycles = int(self.epochHandler.trainingCycles)
        outputString = '{} {}\n'.format(explCycles, trainCycles)
        self.outputFile.write(outputString)

    def outputToFile(self):
        if((self.cyclesPassed % self.outputFrequency) != 0):
            return
        outputString = '{} {}\n'.format(self.cyclesPassed, self.averageMoves)
        self.outputFile.write(outputString)
        self.averageMoves = 0

    def printStatus(self):
        if((self.cyclesPassed % self.printFrequency) != 0):
            return
        print 'Cycle:', self.cyclesPassed, '\tCycle Moves:', self.movementCount

    def cycleStats(self):
        outputCycles = self.cyclesPassed % self.outputFrequency
        if(outputCycles == 0):
            outputCycles = self.outputFrequency
        totalMoves = self.averageMoves * (outputCycles - 1)
        self.averageMoves = (totalMoves + self.movementCount) / outputCycles

    def updateCount(self):
        self.movementCount += 1

    def updateCycle(self, agent):
        self.cyclesPassed += 1
        self.cycleStats()
        self.outputToFile()
        self.printStatus()
        self.epochHandler.stageMonitoring(self.cyclesPassed, agent)
        self.movementCount = 0

    def areWeCycling(self):
        return (self.cyclesPassed < self.limCycles)

    def __del__(self):
        self.outputFile.close()


def flipCoin(probability):
    n = random.random()
    if (n < probability):
        return True
    else:
        return False
