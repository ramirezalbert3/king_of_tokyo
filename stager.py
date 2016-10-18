class Stager:
    def __init__(self, limCycles=2500, outputFrequency=25, outputFileName='Output.txt', printFrequency=250):
        self.limCycles = limCycles
        self.outputFrequency = outputFrequency
        self.printFrequency = printFrequency
        self.outputFile = open(outputFileName, 'w')
        outputString = 'Cycles Movements_cycle Visited_states\n'
        self.outputFile.write(outputString)
        self.cyclesPassed = 0
        self.movementCount = 0
        self.averageMoves = 0

    def outputToFile(self):
        outputString = '{} {}\n'.format(self.cyclesPassed, self.averageMoves)
        self.outputFile.write(outputString)

    def printStatus(self):
        print 'Cycle:', self.cyclesPassed, '\tAverage Moves:', self.averageMoves

    def cycleStats(self):
        outputCycles = self.cyclesPassed % self.outputFrequency
        if(outputCycles == 0):
            outputCycles = self.outputFrequency
        totalMoves = self.averageMoves * (outputCycles - 1)
        self.averageMoves = (totalMoves + self.movementCount) / outputCycles

    def updateCount(self):
        self.movementCount += 1

    def updateCycle(self):
        self.cyclesPassed += 1
        self.cycleStats()
        if((self.cyclesPassed % self.printFrequency) == 0):
            self.outputToFile()
            if((self.cyclesPassed % self.outputFrequency) == 0):
                self.printStatus()
            self.averageMoves = 0
        self.movementCount = 0

    def areWeCycling(self):
        return (self.cyclesPassed < self.limCycles)

    def __del__(self):
        self.outputFile.close()
