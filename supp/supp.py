import itertools as it
from random import randint


def generateSolution(set_items, length):
    set_items = list(set_items).copy()
    some_solution = []
    for i in range(length):
        if len(set_items) < 1:
            break
        rand_i = randint(0, len(set_items) - 1)
        some_solution.append(set_items.pop(rand_i))
    return some_solution


def solutionCombinations(options, start=1):
    stop = len(options) + 1
    all_combinations = []
    for i in range(start, stop + 1):
        all_combinations.extend(list(it.combinations(options, i)))
    return all_combinations
