from supp.supp import solutionCombinations


def bruteForce(backpack, items):
    solution_combinations = solutionCombinations(items)
    highest_value = 0
    best_combination = []

    for combination in solution_combinations:
        combination_value = backpack.goal(combination)
        if combination_value > highest_value:
            highest_value = combination_value
            best_combination = combination
    return best_combination, highest_value

