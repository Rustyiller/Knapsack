from item import Item


def inputData(name):
    list_of_items = []
    f = open(f"{name}.txt", mode="r")
    for line in f:
        line = line.split()
        list_of_items.append(Item(int(line[0]), int(line[1])))
    return list_of_items