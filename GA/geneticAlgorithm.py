import random, math
import numpy as np
import time
from itertools import combinations
from typing import Callable
from operator import itemgetter
import pdb

class GASettings():
    def __init__(self, 
                 N: int,
                 generations: int = 60,
                 populationSize: int = 100,
                 xoRate: float = 0.8,
                 mutationRate: float = 0.01,
                 tournamentSize: int = 3,
                 single_point_xo = True):
        """GASettings purpose is to store the hyperparameters available for the GA, 
        and instantiate default parameters if the user does not specify"""
        self.N = N
        self.generations = generations
        self.populationSize = populationSize
        self.xoRate = xoRate
        self.mutation_rate = mutationRate
        self.tournamentSize = tournamentSize
        self.single_point_xo = single_point_xo

class GASteadyStateBinary:
    
    """Main Genetic Algorithm class

    This uses a one point crossover operator with Tournament selection and maintains
    the fittest individual over all generations.
    
    Algorithm takes GASettings as input to initialize hyper parameters, and a Fitness
    function for an instance of the GA, alongside a boolean indicating whether to
    print the population at each generation (defaults to false, mainly for debugging)
    
    the data structure for an individual in population is (chromosome, fitness) where
    chromosome is the bitstring representation of the genotype

    The class has been designed such that one may override the MainLoop if required"""
    def __init__(self,
                 Fitness: Callable, 
                 settings: GASettings,
                 printGenerations: bool = False):
        self.Fitness = Fitness
        self.N = settings.N
        self.generations = settings.generations
        self.populationSize = settings.populationSize
        self.xoRate = settings.xoRate
        self.mutation_rate = settings.mutation_rate
        self.tournamentSize = settings.tournamentSize
        self.population = []
        self.InitPopulation()
        self.printGenerations = printGenerations
        self.single_point_xo = settings.single_point_xo
    
    def InitPopulation(self):
        """InitPopulation populates the instances '_population' list with 
        '_populationSize' individuals containing randomized chromosomes, initializes
        the population"""
        for i in range(self.populationSize):
            chromosome = [np.random.randint(0, 2) for i in range(self.N)]
            chromoFit = (chromosome, self.Fitness(chromosome))
            if (i == 0):
                self.fittest = chromoFit
            else:
                if (chromoFit[1] > self.fittest[1]):
                    self.fittest = chromoFit
            self.population.append(chromoFit)

    def CrossOver(self):
        """CrossOver creates offspring with a mixture of the parents chromosomes
        with the option to use single point or uniform (default settings is 1point)"""
        firstParent = self.population[self.Tournament()][0]
        secondParent = self.population[self.Tournament()][0]
        
        if self.single_point_xo:
            ##one point xo
            crossOverPoint = np.random.randint(1, self.N-1)
            childChromo = firstParent[0:crossOverPoint] + secondParent[crossOverPoint:]

        else:
            ## Uniform crossover
            uniformCrossover = (np.random.randint(0,2,self.N))
            childChromo = [firstParent[i] if uniformCrossover[i] == 0 else secondParent[i] for i in range(self.N)]
        
        child = (childChromo, self.Fitness(childChromo))
        index = self.Tournament(False)
        self.population[index] = child
        return index
        

    def Tournament(self, highest: bool = True):
        """Tournament function selects 'tournamentSize' number of individuals from
        the population at random and returns the index of either the fittest rated
        individual or the least fittest individual from the selection dependance on
        'highest' argument"""
        index = np.random.randint(0, self.populationSize-1, self.tournamentSize)
        individuals = [(i, self.population[i][1]) for i in index]
        if highest:
            individual = max(individuals, key = itemgetter(1))
        else:
            individual = min(individuals, key = itemgetter(1))
        return individual[0]

    def Mutate(self, index: int):
        """Mutate flips bits in an individuals chromosome randomly by generating an
        array of values between 0-1 and converting them to a boolean based on the
        mutation rate. If the random bool is true at position x then it flips the
        individuals chromosome at position x"""
        chromosome = self.population[index][0]
        for i in range(len(chromosome)):
            if np.random.rand() <= self.mutation_rate:
                if chromosome[i] == 0:
                    chromosome[i] = 1 
                else:
                    chromosome[i] = 0
        chromoFit = (chromosome, self.Fitness(chromosome))
        if (chromoFit[1] > self.fittest[1]):
            self.fittest = chromoFit
        # I have no idea how this following situation occurs, but it does
        if (self.fittest[1] != self.Fitness(self.fittest[0])):
            self.fittest = (self.fittest[0], self.Fitness(self.fittest[0]))
        self.population[index] = chromoFit
        

    def GetBest(self):
        return self.fittest

    
    def MainLoop(self):
        """The main loop for generating new generations, this has been made a seperate
        function such that an outside party may override this function and it still be 
        runnable via self.Run"""
        for gen in range(self.generations):
            for individual in range(len(self.population)):
                if np.random.random() <= self.xoRate:
                    # XO, return index of individual
                    index = self.CrossOver()
                else:
                    # cloning
                    index = self.Tournament()
                self.Mutate(index)
            if (self.printGenerations):
                print(f'Generation: {gen}')
                self.PrintGeneration(self)
    
    def PrintGeneration(self, GA):
        for i in range(len(self.population)):
            print(self.population[i])
        
    def Run(self):
        self.MainLoop()

def SetRandom(value = time.time()):
    """Simple function to reset the seed of numpy's random either using given argument
    or now time which would be sufficiently random"""
    np.random.seed(value)
    
def PrintCombinations(value):
    """prints total number of combinations"""
    input = list(range(value))
    sum = 0
    for i in range(len(input)):
        sum += math.factorial(value) / (math.factorial(i) * math.factorial((len(input) - i)))
    print(f'Number of combinations: {str(sum)}')