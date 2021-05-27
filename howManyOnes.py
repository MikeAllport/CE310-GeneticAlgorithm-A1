from GA.geneticAlgorithm import *
import sys, time

def Fitness(chromosome: list):
    """Fitness function that sums the total amount of 1's found in a chromosome"""
    global count
    count = count + 1
    return sum(chromosome)

def Print1s(GA, printTime = False):
    winner = GA.GetBest()
    winnerChrom = winner[0]
    '''Prints the winner and settings'''
    print("Winning BitString: " + str([winnerChrom[i] for i in range(len(winnerChrom))]))
    print(("\nSettings\n%-24s: %d\n%-24s: %d\n%-24s: %1.1f" +
           "\n%-24s: %3.2f\n%-24s: %d") % (
        "Generations", generations, 
        "Population Size", populationSize, 
        "Xo Rate", xoRate, 
        "Mutation Rate", mutationRate, 
        "Tournament Size", tournamentSize))
    print("\n%-24s: %d" % ("Total 1s", Fitness(winnerChrom)))
    if (printTime):
        time_end = time.time()
        print("%-24s: %1.2f" % ("Total time in seconds", time_end - time_start))
        print("%-24s: %d" % ("Total evalutations", count))
    
    
def Run1s(settings):
    '''quick function to initialize and run a GA for 1's problem'''
    GA = GASteadyStateBinary(Fitness, settings)
    time_start = time.time()
    GA.Run()
    return GA
    
# calculates mean over n runs
def CalcMean1s(settings, n: int):
    '''Runs n times and calculates mean fitness'''
    totalFitness = 0
    for i in range(n):
        GA = Run1s(settings)
        winner = GA.GetBest()
        winnerChrom = winner[0]
        totalFitness += Fitness(winnerChrom)
    avgFitness = totalFitness / n
    print("\nTimes tested: %d\nMean 1's: %-10.2f" % (n, avgFitness))

"""Tests"""
def TestOne():
    #runs once
    settings = GASettings(numBits, generations, populationSize, xoRate, mutationRate, tournamentSize)
    GA = Run1s(settings)

    # outputs results
    Print1s(GA, True)
    PrintCombinations(100)
    time_start = time.time()
    CalcMean1s(settings, numRuns)

def TestTwo():
    #xoRate 0.7
    xoRate: float = 0.7
    settings = GASettings(numBits, generations, populationSize, xoRate, mutationRate, tournamentSize)
    GA = Run1s(settings)
    Print1s(GA)
    CalcMean1s(settings, numRuns)

def TestThree():
    #xoRate 0.8
    xoRate: float = 0.8
    settings = GASettings(numBits, generations, populationSize, xoRate, mutationRate, tournamentSize)
    GA = Run1s(settings)
    Print1s(GA)
    CalcMean1s(settings, numRuns)

def TestFour():
    #mutation rate 0.03
    mutationRate = 0.03
    settings = GASettings(numBits, generations, populationSize, xoRate, mutationRate, tournamentSize)
    GA = Run1s(settings)
    Print1s(GA)
    CalcMean1s(settings, numRuns)

def TestFive():
    mutationRate = 0.01
    generations = 60
    settings = GASettings(numBits, generations, populationSize, xoRate, mutationRate, tournamentSize)
    GA = Run1s(settings)
    Print1s(GA)
    CalcMean1s(settings, numRuns)

"""Main"""
if __name__ == "__main__":
    # inits settings
    numBits = 100
    generations: int = 30
    populationSize: int = 100
    xoRate: float = 0.6
    mutationRate: float = 0.01 # 1 / nbits
    tournamentSize: int = 3
    numRuns = 10
    count = 0
    time_start = time.time()
    TestOne()
    TestTwo()
    TestThree()
    TestFour()
    TestFive()