import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt

from algorithms.hillclimb import neighbourhood
from supp.supp import generateSolution


def annealingGraph(temperatures, values):
    graph_folder = Path("tests")

    plt.plot(temperatures, values)
    plt.title("Wartości dla danej temperatury", fontsize=20, fontweight='bold')
    plt.xlabel("Temperatura", fontsize=18, fontweight='bold')
    plt.ylabel("Wartości", fontsize=18, fontweight='bold')

    plt.gca().invert_xaxis()

    plt.savefig(graph_folder / "annealing_graph")
    plt.clf()


def simmulatedAnnealing(backpack, items, no_iterations, temp, k, T):

    backpack = backpack
    set_items = items
    n_iterations = no_iterations
    temp_func = temp
    k = k
    T = T

    # Generowanie przykładowego rozwiązania
    solution = generateSolution(set_items)
    temperatures = []
    curr_goals = []

    for i in range(n_iterations):

        # Generowanie sąsiada
        neighbour = neighbourhood(
            set_items, solution, rand=True, no_neighbours=2)
        # Przypisaywanie wartości rozwiązań
        curr_goal = backpack.goal(solution)
        poss_goal = backpack.goal(neighbour)

        print("Iteration ", i)
        print("curr_goal: ", curr_goal)
        print("poss_goal: ", poss_goal)

        randn = np.random.rand()
        acceptance_probability = 1 / (np.exp(poss_goal - curr_goal) / T)

        if poss_goal >= curr_goal or randn >= acceptance_probability:
            solution = neighbour

        # Dane zbierane do wyświetlenia na diagramie
        temperatures.append(T)
        curr_goals.append(curr_goal)

        T = temp_func(T, k)

    annealingGraph(temperatures, curr_goals)

    return solution
