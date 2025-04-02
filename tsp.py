# tsp.py
import numpy as np

class TravelingSalesmanProblem:
    def __init__(self, name):
        self.name = name
        self.locations = self.load_data(name)  # Загрузка координат городов

    def load_data(self, name):
        # Пример данных для bayg29 (можно заменить на реальные)
        return np.random.rand(29, 2) * 100  # Случайные координаты

    def getTotalDistance(self, individual):
        distance = 0
        for i in range(len(individual)):
            start = self.locations[individual[i]]
            end = self.locations[individual[(i + 1) % len(individual)]]
            distance += np.linalg.norm(start - end)
        return distance

    def plotData(self, individual):
        import matplotlib.pyplot as plt
        path = [self.locations[i] for i in individual]
        path.append(path[0])  # Замыкаем маршрут
        plt.plot(*zip(*path), marker='o')
        plt.title(f"TSP Route: {self.name}")
        plt.show()