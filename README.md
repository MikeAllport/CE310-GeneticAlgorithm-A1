# Genetic Algorithm
This package contains two main modules used for this assignment "GA/geneticAlgorithm.py" and "GA/bitToRealHelper.py". Enclosed in the root directory are five tasks we have to complete and analyse - "howManyOnes.py", "knapsackProblem.py", "functionOptimisationSphere.py", "functionOptimisationMishra.py", and "travellingSalesPerson.py". The first two show how to use the binary GA, encoding the problem into a bitstring representation, and the further three show how to use the binary GA in conjunction with a bit-to-real converter.  
  
In reality, instead of using a bit-to-real conversion, it would be much simpler to create a real valued GA and change the crossover/mutation operators to use interpolation.  
  
## GASteadyStateBinary class
This is the sole class responsible for running the genetic algorithm. It takes a GASettings instance on construction, alongside a Fitness function defined to suit the problem.