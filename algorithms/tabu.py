from algorithms.hillclimb import neighbourhood
from supp.supp import generateSolution


def tabuSearch(backpack, items, no_iterations, no_neighbours, tabu_size):

    backpack = backpack
    set_items = items
    n_iterations = no_iterations
    n_neighbours = no_neighbours
    tabu_size = tabu_size

    best_solution = list(generateSolution(set_items))
    best_candidate = best_solution.copy()
    tabu = []
    tabu.append(best_solution)

    for i in range(n_iterations):
        # tworzenie sąsiednich rozwiązań
        neighbouring_solutions = neighbourhood(
            set_items, best_candidate, no_neighbours=n_neighbours)

        # sprawdzamy dla każdego sąsiedniego rozwiązania czy jest już na liście tabu i czy jest lepsze od best_candidate
        for candidate in neighbouring_solutions:
            if tabu.count(candidate) == 0:
                if backpack.goal(candidate) > backpack.goal(best_candidate):
                    best_candidate = list(candidate).copy()

        # porównujemy czy best_candidate jest lepszy od best_solution
        if backpack.goal(best_candidate) > backpack.goal(best_solution):
            best_solution = best_candidate.copy()

        tabu.append(best_candidate)
        if len(tabu) > tabu_size:
            tabu.pop(0)

    return best_solution, backpack.goal(best_solution)
