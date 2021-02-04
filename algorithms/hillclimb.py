import random

from supp.supp import generateSolution, solutionCombinations


def neighbourhood(set_items, current_solution, rand=False, no_neighbours=2):

    # tworzenie sąsiednich przedmiotów do obecnego rozwiązania
    neighbours = []
    for i in range(no_neighbours):
        item = set_items[random.randint(0, len(set_items) - 1)]
        if item not in neighbours and item not in current_solution:
            neighbours.append(item)

    neighbours.extend(current_solution)
    if rand:
        ran_len = random.randint(
            len(current_solution) - 1, len(current_solution) + 1)
        if ran_len == 0:
            ran_len = len(neighbours) // 2
        return list(generateSolution(neighbours, ran_len))
    else:
        return solutionCombinations(neighbours, start=len(current_solution) - 1, stop=len(current_solution) + 1)


def hillClimb(backpack, items, no_iterations, no_neighbours, tabu_size):

    backpack = backpack
    set_items = items
    n_iterations = no_iterations
    n_neighbours = no_neighbours

    current_solution = list(generateSolution(set_items))

    for i in range(n_iterations):

        neighbours = neighbourhood(
            set_items, current_solution, rand=False, no_neighbours=n_neighbours)
        for neighbour in neighbours:
            if backpack.goal(neighbour) > backpack.goal(current_solution):
                current_solution = list(neighbour).copy()

    return current_solution, backpack.goal(current_solution)



