class Backpack:
    # Definicja pojemności plecaka
    def __init__(self, capacity):
        self.capacity = capacity
        self.calls = 0

    # Funkcja oceny
    def goal(self, items):
        self.calls += 1
        value = 0
        weight = 0
        for item in items:
            value += item.value
            weight += item.weight
            if weight > self.capacity:
                value = -len(items)
        return value

class Item:
    # Definicja wartości i wagi przedmiotu
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

    def __repr__(self):
        return "(" + str(self.weight) + ", " + str(self.value) + ")"

