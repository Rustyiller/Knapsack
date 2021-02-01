import itertools as it
import random

from supp.supp import generateSolution, solutionCombinations


def neighbourhood(set_items, current_solution, n_neighbours=2):
    '''
    Generates neighbouring Item for every item in the solution

    Args:
        set_items: list of Item objects
        current_solution: list of Item objects
        rand: bool indicates whether we want to turn neighbours
        into all possible combinations of them

    Returns:
        list of Items' lists
    '''
    neighbours = []
    for i in range(n_neighbours):
        item = set_items[random.randint(0, len(set_items) - 1)]
        if item not in neighbours and item not in current_solution:
            neighbours.append(item)

    neighbours.extend(current_solution)
    return solutionCombinations(neighbours, start=len(current_solution) - 1, stop=len(current_solution) + 1)


def hill_climb(backpack, items, n, ne):
    '''
    Finds the optimal solution in set_items using full hill climb algorithm

    Args:
        set_items: list of Item objects
        n_iterations: int, number of times to search the neighbourhood

    Returns:
        list of Item objects
    '''
    backpack = backpack
    set_items = items
    n_iterations = n
    n_neighbours = ne

    current_solution = list(generateSolution(set_items))

    for i in range(n_iterations):

        neighbours = neighbourhood(
            set_items, current_solution, n_neighbours=n_neighbours)
        for neighbour in neighbours:
            if backpack.goal(neighbour) > backpack.goal(current_solution):
                current_solution = list(neighbour).copy()

    return current_solution, backpack.goal(current_solution)



