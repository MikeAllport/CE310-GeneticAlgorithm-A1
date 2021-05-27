from GA.geneticAlgorithm import *
from GA.bitToRealHelper import *

"""
functionOptimisationSphere's purpose is to use a Binary GA to perform a single objective function optimisation to find the global minima of the sphere equation 

@author Michael Allport 2021
"""

if __name__ == "__main__":
    time_start = time.time()
    # instantiates real representation
    numBits = 90
    minimum = -1
    maximum = 1
    # 3 parameters of bit length 30 each for the bit to real
    bitConverter = BitToReal([30, 30, 30], minimum, maximum)
    count = 0
    #instantiates hyper parameter settings
    settings = GASettings(numBits)
    settings._mutation_rate = 0.01
    settings._xoRate = 0.8
    settings._generations = 100

    #defines fitness function
    def Fitness(chromosome: list):
        """Fitness function attains the real value of each bit array, and returns the negative squared value
        of each variable"""
        global count, bitConverter
        count += 1
        bit1val = bitConverter.GetRealValue(chromosome, 1)
        bit2val = bitConverter.GetRealValue(chromosome, 2)
        bit3val = bitConverter.GetRealValue(chromosome, 3)
        return -(bit1val**2 + bit2val**2 + bit3val**2) #minimisation

    #runs the program
    GA = GASteadyStateBinary(Fitness, settings)
    GA.Run()
    winner = GA.GetBest()
    winnerChrom = winner[0]
    time_end = time.time()
    bitStrings = bitConverter.GetBitArrays(winnerChrom)
    print("Binary to real")
    print("Bit N: " + str(numBits))
    print("Range: '" + str(minimum) + "' to '" + str(maximum) + "'")
    bitConverter.PrintResolutions()
    print("----------------------------------")
    print("Results of Sphere algorithm optimisation")
    print("x1 bits: " + str(bitStrings[0]))
    print("x1 value: " + str(bitConverter.GetRealValue(winnerChrom, 1)))
    print("x2 bits: " + str(bitStrings[1]))
    print("x2 value: " + str(bitConverter.GetRealValue(winnerChrom, 2)))
    print("x3 bits: " + str(bitStrings[2]))
    print("x4 value: " + str(bitConverter.GetRealValue(winnerChrom, 3)))
    print("Total time in seconds: %2.2f" % (time_end - time_start))
    print("Total evaluations: " + str(count))