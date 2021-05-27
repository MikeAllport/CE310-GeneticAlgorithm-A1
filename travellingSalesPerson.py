from GA.geneticAlgorithm import *
from GA.bitToRealHelper import *
import sys, time

# initialises representation
placesDict = {"A" : 0, "B" : 1, "C" : 2, "D": 3, "E": 4}
destinationsA = [("B", 100), ("C", 200), ("D", 150), ("E", 175)]
destinationsB = [("A", 100), ("E", 225), ("D", 250), ("C", 125)]
destinationsC = [("B", 125), ("A", 200), ("E", 275), ("D", 300)]
destinationsD = [("C", 300), ("B", 250), ("A", 150), ("E", 75)]
destinationsE = [("A", 175), ("B", 225), ("C", 275), ("D", 75)]
frontier = [destinationsA, destinationsB, destinationsC, destinationsD, destinationsE];
startingPoint = "A"
modulo = 0
count = 0
time_start = time.time()

#defines operators
def ConvertBinaryArrToInt(bitArr):
    """Converts a bit array into its integer representation
    Scaling is achieved given a modulo operator"""
    global modulo
    dec = sum(bitArr[i] * 2**i for i in range(len(bitArr)))
    dec = dec % modulo
    return dec

def Fitness(chromosome: list):
    global count, bitToInt, ConvertBinaryArrToInt, modulo
    count += 1
    arrays = bitToInt.GetBitArrays(chromosome)
    visited = []
    totalTrip = 0;
    destinations = frontier[0] # start at A, visit A's destinations
    for i in range(len(frontier)):
        modulo = len(destinations)
        
        #selection of place from destinations
        indexTo = ConvertBinaryArrToInt(arrays[i])
        destination = destinations[indexTo]
        
        #check destination letter not been travelled to already
        if(destination[0] in visited):
            return 0
        
        #add letter of new destination to list of visited and tot cost
        visited.append(destination[0])
        totalTrip += destination[1]
        
        # sets destinations to that of places travellable from selected destination
        destinations = frontier[placesDict[destination[0]]]
    if (visited[4] != startingPoint):
        return 0
    return 1/totalTrip

if __name__ == "__main__":
    #instantiates hyper parameters and  settings
    bitToInt = BitToReal([2, 2, 2, 2, 2], 0, 4)
    numBits = 2 * 5
    settings = GASettings(numBits)
    settings._mutation_rate = 0.01
    settings._xoRate = 0.7
    settings._generations = 50

    #runs the program
    GA = GASteadyStateBinary(Fitness, settings)
    GA.Run()
    winner = GA.GetBest()

    #calculates the trip cost and the trip made
    time_end = time.time()
    duration = time_end - time_start
    arrays = bitToInt.GetBitArrays(winner[0])
    visited = []
    totalTrip = 0;
    destinations = frontier[0] # start at A, visit A's destinations
    for i in range(len(frontier)):

        #selection of place from destinations
        indexTo = ConvertBinaryArrToInt(arrays[i])
        destination = destinations[indexTo]

        #add letter of new destination to set of visited
        visited.append(destination[0])
        totalTrip += destination[1]
        # sets destinations to that of places travellable from selected destination
        destinations = frontier[placesDict[destination[0]]]

    #prints stats
    print("GA Traveling salesman solution")
    print(f'Evaluations: {count}')
    print(f'Time taken: {duration}')
    print(f'Best Route: {visited}')
    print(f'Route Cost: {totalTrip}')