from GA.geneticAlgorithm import *
from GA.bitToRealHelper import *

"""
functionOptimisationSphere's purpose is to use a Binary GA to perform a constrained function optimisation to find the global minima of the Mishra's Bird equation - https://en.wikipedia.org/wiki/Test_functions_for_optimization

@author Michael Allport 2021
"""

def U(x, y):
    """Mishra's function to be optimised"""
    return math.sin(y) * math.e ** ((1 - math.cos(x))**2) + math.cos(x) * math.e **((1 - math.sin(y))**2) + (x - y) ** 2


def g(x, y):
    """Constraint penalty"""
    return (x + 5) ** 2 + (y + 5) ** 2 - 25


def Fitness(chromosome: list):
    """Fitness problem, minimization"""
    global count, bitConverter
    count+=1
    x = bitConverter.GetRealValue(chromosome, 1)
    y = bitConverter.GetRealValue(chromosome, 2)
    constraint = g(x, y)
    if (constraint > 0):
        penalty = constraint ** 3
    else:
        penalty = 0
    return -(U(x, y) + 10 * penalty)

if __name__ == "__main__":
    time_start = time.time()

    #instantiates real representation
    numBits = 90
    minimum = -10
    maximum = 0
    bitConverter = BitToReal([int(numBits/2), int(numBits/2)], minimum, maximum)
    count = 0

    #instantiates hyper parameter settings
    settings = GASettings(numBits)
    settings._mutation_rate = 1/(numBits/2)
    settings._xoRate = 0.7
    settings._generations = numBits

    #runs the program & prints
    GA = GASteadyStateBinary(Fitness, settings)
    GA.Run()
    winner = GA.GetBest()
    winnerChrom = winner[0]
    time_end = time.time()
    bitStrings = bitConverter.GetBitArrays(winnerChrom)
    x = bitConverter.GetRealValue(winnerChrom, 1)
    y = bitConverter.GetRealValue(winnerChrom, 2)
    print("Binary to real")
    print("Bit N: " + str(numBits))
    print("Range: '" + str(minimum) + "' to '" + str(maximum) + "'")
    bitConverter.PrintResolutions()
    print("----------------------------------")
    print("Results of Mishra's Bird optimisation")
    print("x bits: " + str(bitStrings[0]))
    print("x value: " + str(x))
    print("y bits: " + str(bitStrings[1]))
    print("y value: " + str(y))
    print("Total time in seconds: " + str(time_end - time_start))
    print("Total evaluations: " + str(count))