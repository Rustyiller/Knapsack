import time

from algorithms.brute import bruteForce
from algorithms.genetic import geneticAlgorythm
from algorithms.hillclimb import hillClimb
from algorithms.sa import simmulatedAnnealing
from algorithms.tabu import tabuSearch
from supp.input import inputData
from supp.output import outputData
from  supp.generate_tests import tests
from supp.temp import default_temperature


def menu(backpack):
    print("Wybierz algorytm:")
    print("1. bruteForce")
    print("2. hillClimb")
    print("3. tabuSearch")
    print("4. simmulatedAnnealing")
    print("5. Wygeneruj testy dla hillClimb i tabuSearch")
    print("6. Genetic")
    print("7. Wyjście")

    choice = int(input())

    if choice == 1:
        print("podaj źródło przedmiotów")
        items = input()
        item_list = inputData(items)
        start = time.time()
        solution, value = bruteForce(backpack, item_list)
        stop = time.time()
        diff = stop - start
        outputData(solution, value, diff, "bruteForce")
        print("wynik zapisano do pliku bruteForce.txt")

    if choice == 2:
        print("podaj źródło przedmiotów")
        items = input()
        item_list = inputData(items)
        print("podaj liczbe iteracji")
        no_iterations = int(input())
        print("podaj liczbe sąsiednich rozwiązań")
        no_neighbours = int(input())
        start = time.time()
        solution, value = hillClimb(backpack, item_list, no_iterations, no_neighbours, 0)
        stop = time.time()
        diff = stop - start
        outputData(solution, value, diff, "hillClimb")
        print("wynik zapisano do pliku hillClimb.txt")

    if choice == 3:
        print("podaj źródło przedmiotów")
        items = input()
        item_list = inputData(items)
        print("podaj liczbe iteracji")
        no_iterations = int(input())
        print("podaj liczbe sąsiednich rozwiązań")
        no_neighbours = int(input())
        print("podaj rozmiar tabu")
        tabu_size = int(input())
        start = time.time()
        solution, value = tabuSearch(backpack, item_list, no_iterations, no_neighbours, tabu_size)
        stop = time.time()
        diff = stop - start
        outputData(solution, value, diff, "tabuSearch")
        print("wynik zapisano do pliku tabuSearch.txt")

    if choice == 4:
        print("podaj źródło przedmiotów")
        items = input()
        item_list = inputData(items)
        print("podaj liczbe iteracji")
        no_iterations = int(input())
        print("wybierz typ temperatury: \n1. default_temperature")
        temp = int(input())
        if temp == 1:
            to_temp = default_temperature
        else:
            to_temp = default_temperature
            print("wybrano domyślną temperaturę default_temperature")
        print("podaj współczynnik wygaszania")
        k = float(input())
        print("podaj początkową temperaturę")
        T = int(input())
        start = time.time()
        solution = simmulatedAnnealing(backpack, item_list, no_iterations, to_temp, k, T)
        stop = time.time()
        diff = stop - start
        value = backpack.goal(solution)
        outputData(solution, value, diff, "simmulatedAnnealing")
        print("wynik zapisano do pliku annealing_graph.png")

    if choice == 5:
        tests(backpack)
        print("wyniki zapisano w folderze tests")

    if choice == 6:
        set_items = inputData("items1")
        geneticAlgorythm(backpack, set_items, 4, 1)

    if choice == 7:
        pass