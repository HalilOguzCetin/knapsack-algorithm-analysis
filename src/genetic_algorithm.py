import random
import csv
import time

def read_data(filename):
    weights = []
    values = []

    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            weights.append(int(row['weight']))
            values.append(int(row['value']))

    return weights, values


def fitness(solution, weights, values, capacity):
    total_weight = 0
    total_value = 0

    for i in range(len(solution)):
        if solution[i] == 1:
            total_weight += weights[i]
            total_value += values[i]

    if total_weight > capacity:
        return total_value * 0.1
    return total_value


def create_population(size, n):
    return [[random.randint(0, 1) for _ in range(n)] for _ in range(size)]


def selection(population, weights, values, capacity):
    population.sort(key=lambda x: fitness(x, weights, values, capacity), reverse=True)
    return population[:len(population)//2]


def crossover(parent1, parent2):
    point = random.randint(0, len(parent1) - 1)
    child = parent1[:point] + parent2[point:]
    return child


def mutate(solution, rate=0.01):
    for i in range(len(solution)):
        if random.random() < rate:
            solution[i] = 1 - solution[i]
    return solution


def genetic_algorithm(weights, values, capacity, generations=50, pop_size=50):
    n = len(weights)
    population = create_population(pop_size, n)

    for _ in range(generations):
        selected = selection(population, weights, values, capacity)
        new_population = selected.copy()

        while len(new_population) < pop_size:
            p1, p2 = random.sample(selected, 2)
            child = crossover(p1, p2)
            child = mutate(child)
            new_population.append(child)

        population = new_population

    best = max(population, key=lambda x: fitness(x, weights, values, capacity))
    return fitness(best, weights, values, capacity)


if __name__ == "__main__":
    files = [
        "../data/data_50.csv",
        "../data/data_200.csv",
        "../data/data_1000.csv"
    ]

    capacity = 200

    for file in files:
        weights, values = read_data(file)

        start = time.time()
        result = genetic_algorithm(weights, values, capacity)
        end = time.time()

        print(f"{file} → GA değer: {result}, süre: {end - start:.5f} saniye")