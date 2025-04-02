import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from deap import base, creator, tools, algorithms
import tsp  # власний модуль (має бути в робочій директорії)

# Налаштування параметрів
TSP_NAME = "bayg29"
POPULATION_SIZE = 300
P_CROSSOVER = 0.9
P_MUTATION = 0.1
MAX_GENERATIONS = 200
RANDOM_SEED = 42
random.seed(RANDOM_SEED)

# Отримуємо кількість міст
problem_instance = tsp.TravelingSalesmanProblem(TSP_NAME)
num_cities = len(problem_instance.locations)  # Тепер коректно отримуємо кількість міст

# Ініціалізація DEAP
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("randomOrder", random.sample, range(num_cities), num_cities)
toolbox.register("individualCreator", tools.initIterate, creator.Individual, toolbox.randomOrder)
toolbox.register("populationCreator", tools.initRepeat, list, toolbox.individualCreator)

# Функція пристосованості
def tspDistance(individual):
    return problem_instance.getTotalDistance(individual),

toolbox.register("evaluate", tspDistance)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=1.0 / num_cities)

# Генетичний алгоритм
population = toolbox.populationCreator(n=POPULATION_SIZE)
hof = tools.HallOfFame(1)
stats = tools.Statistics(lambda ind: ind.fitness.values)
stats.register("min", np.min)
stats.register("avg", np.mean)

population, logbook = algorithms.eaSimple(
    population, toolbox, cxpb=P_CROSSOVER, mutpb=P_MUTATION,
    ngen=MAX_GENERATIONS, stats=stats, halloffame=hof, verbose=True
)

# Візуалізація
plt.figure(1)
problem_instance.plotData(hof.items[0])

plt.figure(2)
minFitnessValues, meanFitnessValues = logbook.select("min", "avg")
sns.set_style("whitegrid")
plt.plot(minFitnessValues, color='red', label='Min')
plt.plot(meanFitnessValues, color='green', label='Mean')
plt.xlabel('Покоління')
plt.ylabel('Мінімальна / Середня пристосованість')
plt.title('Мінімальна та середня пристосованість у поколіннях - TSP')
plt.legend()
plt.show()