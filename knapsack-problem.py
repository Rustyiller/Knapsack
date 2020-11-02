from random import randint
import itertools as it


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


def inputData():
    list_of_items = []
    f = open("items.txt", mode="r")
    for line in f:
        line = line.split()
        list_of_items.append(Item(int(line[0]), int(line[1])))
    return list_of_items


def outputData(solution_items, goal, f_name):
    f = open(f"{f_name}.txt", "w")
    f.write(str(solution_items) + "\n" + str(goal))


def generateSolution(set_items, length):
    set_items = list(set_items).copy()
    some_solution = []
    for i in range(length):
        if len(set_items) < 1:
            break
        rand_i = randint(0, len(set_items) - 1)
        some_solution.append(set_items.pop(rand_i))
    return some_solution


def solutionCombinations(options, start=1, stop=-1):
    if stop == -1:
        stop = len(options) + 1

    all_combinations = []
    for i in range(start, stop + 1):
        all_combinations.extend(list(it.combinations(options, i)))
    return all_combinations


# Deklaracja plecaka i jego pojemności
backpack = Backpack(10)

# Przykład oceny rozwiązania
solution_items = [Item(4, 10), Item(1, 2), Item(2, 1), Item(1, 5)]
solution_value = backpack.goal(solution_items)
print("Wartość plecaka nr1 " + str(solution_value))

# Przykład gdzie waga przedmiotów przekracza pojemność plecaka
solution_items = [Item(5, 10), Item(8, 2), Item(1, 1), Item(1, 5)]
solution_value = backpack.goal(solution_items)
print("Wartość plecaka nr2 " + str(solution_value))

# Załączanie przykładowych przedmiotów z pliku
items = inputData()
print("Przedmioty dostarczone na wejściu :" + str(items))

# Generowanie przykładowego rozwiązania z wcześniej zaimportowanych przedmiotów
solution_items = generateSolution(items, 4)
print("Wygenerowany plecak :" + str(solution_items))
solution_value = backpack.goal(solution_items)
print("Wartość plecaka nr3 " + str(solution_value))
outputData(solution_items, solution_value, "output")

# Generowanie nowego rozwiązania o takiej samej długości poprzez kombinację przedmimotów
solution_combinations = solutionCombinations(items)
next_solution = None
for combination in solution_combinations:
    if len(combination) == 4 and next_solution is None:
        next_solution = combination
print("Wygenerowane nowe rozwiązanie za pomocą kombinacji :" + str(next_solution))
solution_value = backpack.goal(next_solution)
print("Wartość plecaka nr4 " + str(solution_value))
outputData(next_solution, solution_value, "next_solution")
