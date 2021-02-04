class Item:
    # Definicja wartości i wagi przedmiotu
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

    def __repr__(self):
        return "(" + str(self.weight) + ", " + str(self.value) + ")"
