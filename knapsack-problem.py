import time
import sys

from algorithms.hillclimb import hill_climb
from supp.supp import solutionCombinations


class Backpack:
    # Definicja pojemności plecaka
    def __init__(self, capacity):
        self.capacity = capacity

    # Funkcja oceny
    def goal(self, items):
        value = 0
        weight = 0
        for item in items:
            value += item.value
            weight += item.weight
            if weight > self.capacity:
                value = -1
        return value


class Item:
    # Definicja wartości i wagi przedmiotu
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

    def __repr__(self):
        return "(" + str(self.weight) + ", " + str(self.value) + ")"


def inputData(name):
    list_of_items = []
    f = open(f"{name}.txt", mode="r")
    for line in f:
        line = line.split()
        list_of_items.append(Item(int(line[0]), int(line[1])))
    return list_of_items


def outputData(solution_items, goal, time, f_name):
    f = open(f"{f_name}.txt", "w")
    f.write(str(solution_items) + "\n" + "wartosc : " + str(goal) + "\n" + "czas : " + str(time))


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


input_file_name = sys.argv[1]
output_file_name = sys.argv[2]

# Deklaracja plecaka i jego pojemności
backpack = Backpack(15)

"""
# Przykład oceny rozwiązania
solution_items = [Item(4, 10), Item(1, 2), Item(2, 1), Item(1, 5)]
solution_value = backpack.goal(solution_items)
print("Wartość plecaka nr1 " + str(solution_value))

# Przykład gdzie waga przedmiotów przekracza pojemność plecaka
solution_items = [Item(5, 10), Item(8, 2), Item(1, 1), Item(1, 5)]
solution_value = backpack.goal(solution_items)
print("Wartość plecaka nr2 " + str(solution_value))
"""

# Załączanie przykładowych przedmiotów z pliku
items = inputData(input_file_name)
#print("Przedmioty dostarczone na wejściu :" + str(items))

# Generowanie przykładowego rozwiązania z wcześniej zaimportowanych przedmiotów
""""
solution_items = generateSolution(items, 5)
print("Wygenerowany plecak :" + str(solution_items))
solution_value = backpack.goal(solution_items)
print("Wartość plecaka nr3 " + str(solution_value))
outputData(solution_items, solution_value, "output")

# Generowanie nowego rozwiązania o takiej samej długości poprzez kombinację przedmimotów
solution_combinations = solutionCombinations(items)
next_solution = None
for combination in solution_combinations:
    if len(combination) == 5 and next_solution is None:
        next_solution = combination
print("Wygenerowane nowe rozwiązanie za pomocą kombinacji :" + str(next_solution))
solution_value = backpack.goal(next_solution)
print("Wartość plecaka nr4 " + str(solution_value))
outputData(next_solution, solution_value, "next_solution")
"""
print("Przedmioty dostarczone na wejściu :" + str(items))

start = time.time()
#solution, value = bruteForce(backpack, items)
solution, value = hill_climb(backpack, items, 10, 2)
stop = time.time()
diff = stop - start
print("rozwiązanie : " + str(solution) + " a jego wartość to " + str(value))
print("czas : " + str(diff))
outputData(solution, value, diff, output_file_name)
