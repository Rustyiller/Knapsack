import random

import numpy as np

from supp.supp import generateSolution


def generatePopulation(set_items, population_size):
    population = []
    for i in range(population_size):
        rand_len = random.randint(1, population_size)
        population.append(generateSolution(set_items, rand_len))

    return population


def fitness(capacity, items):
    items_value = sum([x.value for x in items])
    items_weight = sum([x.weight for x in items])

    return items_value if items_weight <= capacity else 0


def selectionTournament(population, capacity):

    t_population = population
    chosen = []
    for i in range(2):
        ran_i = np.random.randint(0, len(population))
        chosen.append(population[ran_i])
        t_population.pop(t_population.index(t_population[ran_i]))
    fitnesses = [fitness(capacity, x) for x in chosen]
    return chosen[fitnesses.index(max(fitnesses))]


def crossover(parent_a, parent_b):
    shorter = min(len(parent_a), len(parent_b))

    slice_1 = np.random.randint(low=0, high=shorter)
    print(slice_1)

    slice_2 = np.random.randint(low=(0), high=shorter)
    print(slice_2)


    #return child_a, child_b


def geneticAlgorythm(backpack, set_items, population_size, cross_prob):
    population = generatePopulation(set_items, population_size)
    for i in range()
    fitnesses = []
    for bag in population:
        fitnesses.append(fitness(backpack.capacity, bag))
    first_child = selectionTournament(population, backpack.capacity)
    second_child = selectionTournament(population, backpack.capacity)
    print("first before", first_child)
    print("second berofe", second_child)
    cross = np.random.random_sample() <= cross_prob
    print(cross)
    if cross:
        first_child, second_child = crossover(first_child, second_child)
    print("first", first_child)
    print("second", second_child)