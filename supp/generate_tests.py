from pathlib import Path
from matplotlib import pyplot as plt


from algorithms.hillclimb import hillClimb
from algorithms.tabu import tabuSearch
from supp.input import inputData


def measureTime(algorithm, backpack, items, no_iterations, no_neighbours, tabu_size):
    import time
    start = time.time()
    result, _ = algorithm(backpack, items, no_iterations, no_neighbours, tabu_size)
    stop = time.time()
    diff = stop - start
    return result, diff


def testData(method, set_length, time, value):

    # Wpisywanie wyników testów do plików
    out_folder = Path("tests")
    raw_data = ""
    f = open(out_folder / f'test_{method}.txt', mode="a")
    raw_data += f"{method} "
    raw_data += f"{set_length} "
    raw_data += f"{time} "
    raw_data += f"{value} \n"
    f.write(raw_data)
    f.close()



def dataForGraph(filename):
    data_folder = Path("tests")
    graph_folder = Path("tests")
    f = open(data_folder / f"{filename}.txt", mode="r")
    next(f)

    sizes = []
    times = []
    values = []

    #Zebranie danych z pliku
    for line in f:
        line = line.split()
        name = line[0]
        sizes.append(int(line[1]))
        times.append(float(line[2]))
        values.append(float(line[3]))

    plt.plot(sizes, times, 'ro')
    plt.title(f"{name} Porównanie czasu obliczeń do rozmiaru zadania")
    plt.xlabel("Rozmiar")
    plt.ylabel("Czas ")
    plt.savefig(graph_folder / f"{name}_time_size_plot.png")

    plt.clf()

    plt.plot(sizes, values, 'ro')
    plt.title(f"{name} Porównanie jakości wykonanego zadania do rozmiaru zadania")
    plt.xlabel("Rozmiar")
    plt.ylabel("Jakość")
    plt.savefig(graph_folder / f"{name}_value_size_plot.png")

    plt.clf()


def tests(backpack):
    out_folder = Path("tests")

    f = open(out_folder / "test_hillClimb.txt", mode="w+")
    f.write("metoda rozmiar czas_sredni wynik_sredni \n")
    f.close()

    f = open(out_folder / "test_tabuSearch.txt", mode="w+")
    f.write("metoda rozmiar czas_sredni wynik_sredni \n")
    f.close()

    items_sets = [inputData("items"), inputData("items1"), inputData("items2"),
                  inputData("items3"), inputData("items4"), inputData("items5")]
    algorithms = [hillClimb, tabuSearch]
    algorithms_names = {hillClimb: "hillClimb", tabuSearch: "tabuSearch"}
    for item_set in items_sets:
        for algorithm in algorithms:
            times = []
            goals = []
            i = 25
            while i > 0:
                i -= 1
                solution, diff = measureTime(algorithm, backpack, item_set, 100, 2, 10)
                times.append(diff)
                goals.append(backpack.goal(solution))

            testData(method=algorithms_names[algorithm], set_length=len(
                    item_set), time=sum(times) / len(times), value=sum(goals) / len(goals))

    dataForGraph("test_tabuSearch")
    dataForGraph("test_hillClimb")

