# TSP_GeneticAlgorithm

In this homework you have to apply genetic algorithm on TSP problem. This homework is an open
homework, which means you must go through different experiments and make your code better,
but you have to meet the minimum requirements (At least do a complete test with 100 cities and
report). These are the parameters of your program.

1. Number of cities:
Try to increase number of cities as much as you can till it takes more than minute to give
you the answer (or 2-3 minutes)

2. Instances in population:
This is an important parameter, choosing small size may not give you the best answer,
choosing a large population makes it slow. Run your code with different population size to
get the best answer.

3. Crossover, Mutation, Elitism:
Do not forget to give higher chance for crossover to better instances.
Mutation should be small 1-2% but it will be good to check a bit higher percentage.
Elitism can be useful. Some of the best instances go directly to next generation, test to find
the best proportion. Maybe 5-10% be a good estimate. Also give the chance to these
instances to go through crossover based on their fitness.

4. Fitness function:
You have to choose a fitness function, as it can be important. A function based on the
distance. You can define a function that give better fitness value to better instances.


You can choose any programming language that you like. Python and Matlab seems to be better
choices. Your code should have a plotting part and as the program runs shows the best result after
certain number of generations. It will be a good idea to give options to user to choose the
parameters like number of cities, number of instances in population, mutation percentage, ….
Write a report and discuss your experience based on parameters and show several results of
different runs of your code.