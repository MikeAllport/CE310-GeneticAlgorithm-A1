from GA.geneticAlgorithm import *
import sys, time

"""
The purpose of knapsackProblem.py is to use a Binary Steady State Genetic Algorithm to solve the
knapsack combinatorial problem

@author Michael Allport 2021
"""

"""Representation of knapsack"""
numBoxes = 30
w_i = [ 5,  5, 10, 3,  9, 14,  2, 2, 6,  6, 19, 10, 3,  1, 18, 11, 7,  6, 6, 6, 6, 2, 10]
v_i = [15, 20,  2, 5, 10, 15, 15, 2, 1, 10, 20,  3, 8, 10,  5,  9, 5, 17, 3, 3, 3, 15, 1]
w_max = 50

"""Fitness function"""
def Fitness(chromosome: list):
    global count, w_i, v_i, w_max
    count = count + 1
    weights = [w_i[i] for i in range(len(chromosome)) if chromosome[i] > 0]
    total = sum(weights)
    if total > w_max or total == 0:
        return 0
    values = [v_i[i] for i in range(len(chromosome)) if chromosome[i] > 0]
    return sum(values)

"""main program"""
if __name__ == "__main__":
    count = 0
    time_start = time.time()

    def Fitness(chromosome: list):
        global count, w_i, v_i, w_max
        count = count + 1
        weights = [w_i[i] for i in range(len(chromosome)) if chromosome[i] > 0]
        total = sum(weights)
        if total > w_max or total == 0:
            return 0
        values = [v_i[i] for i in range(len(chromosome)) if chromosome[i] > 0]
        return sum(values)

    generations: int = 60
    populationSize: int = 100
    xoRate: float = 0.8
    mutationRate: float = 1 / len(w_i)
    tournamentSize: int = 3
    settings = GASettings(len(w_i), generations, populationSize, xoRate, mutationRate, tournamentSize)
    GA = GASteadyStateBinary(Fitness, settings)
    GA.Run()
    winner = GA.GetBest()
    winnerChrom = winner[0]
    time_end = time.time()
    print("Boxes: " + str([i for i in range(len(winnerChrom)) if winnerChrom[i] > 0]))
    print("Total value: " + str(sum([v_i[i] for i in range(len(winnerChrom)) if winnerChrom[i] > 0])))
    print("Total weight: " + str(sum([w_i[i] for i in range(len(winnerChrom)) if winnerChrom[i] > 0])))
    print("Total time in seconds: " + str(time_end - time_start))
    print("Total evaluations: " + str(count))
    PrintCombinations(len(v_i))