# Імпорт бібліотек
import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from deap import base, creator, tools, algorithms
import knapsack  # власний модуль (має бути в робочій директорії)

# Налаштування параметрів
POPULATION_SIZE = 50
P_CROSSOVER = 0.9
P_MUTATION = 0.1
MAX_GENERATIONS = 50
RANDOM_SEED = 42
random.seed(RANDOM_SEED)

# Ініціалізація DEAP
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
toolbox.register("zeroOrOne", random.randint, 0, 1)
toolbox.register("individualCreator", tools.initRepeat, creator.Individual, toolbox.zeroOrOne, len(knapsack.Knapsack01Problem()))
toolbox.register("populationCreator", tools.initRepeat, list, toolbox.individualCreator)

# Функція придатності
def knapsackValue(individual):
    return knapsack.Knapsack01Problem().getValue(individual),

toolbox.register("evaluate", knapsackValue)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("mate", tools.cxOnePoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=1.0/len(knapsack.Knapsack01Problem()))

# Генетичний алгоритм
population = toolbox.populationCreator(n=POPULATION_SIZE)
hof = tools.HallOfFame(1)
stats = tools.Statistics(lambda ind: ind.fitness.values)
stats.register("max", np.max)
stats.register("avg", np.mean)

population, logbook = algorithms.eaSimple(
    population, toolbox, cxpb=P_CROSSOVER, mutpb=P_MUTATION,
    ngen=MAX_GENERATIONS, stats=stats, halloffame=hof, verbose=True
)

# Візуалізація
maxFitnessValues, meanFitnessValues = logbook.select("max", "avg")
sns.set_style("whitegrid")
plt.plot(maxFitnessValues, color='red', label='Max')
plt.plot(meanFitnessValues, color='green', label='Mean')
plt.xlabel('Generation')
plt.ylabel('Max / Average Fitness')
plt.title('Max and Average Fitness over Generations - Knapsack')
plt.legend()
plt.show()