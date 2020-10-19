class Backpack:
    #Definicja pojemności plecaka
    def __init__(self, capacity):
        self.capacity = capacity

    #Funkcja oceny
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
    #Definicja wartości i wagi przedmiotu
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

#Deklaracja plecaka i jego pojemności
backpack = Backpack(10)

#Przykład oceny rozwiązania
solution_items = [Item(4, 10), Item(1, 2), Item(2, 1), Item(1, 5)]
solution_value = backpack.goal(solution_items)
print("value of backpack nr1 " + str(solution_value))

#Przykład gdzie waga przedmiotów przekracza pojemność plecaka
solution_items = [Item(5, 10), Item(8, 2), Item(1, 1), Item(1, 5)]
solution_value = backpack.goal(solution_items)
print("value of backpack nr2 " + str(solution_value))
