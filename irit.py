class Taco:
    def __init__(self, shell, toppings=[]):
        self.shell = shell
        self.toppings = toppings
        self.index = -1

    def __iter__(self):
        return (t for t in self.toppings)

    def __len__(self):
        return len(self.toppings)

    def __reversed__(self):
        for i in range(len(self) -1, -1, -1):
            yield self.toppings[i]

taco = Taco('soft', ['sour cream', 'tomatoes'])