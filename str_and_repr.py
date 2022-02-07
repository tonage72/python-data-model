class Taco:
    def __init__(self, shell, protein, toppings=[]):
        self.shell = shell
        self.protein = protein
        self.toppings = toppings

    def __repr__(self):
        first = f'<Taco toppings={self.toppings} protein={self.protein} shell={self.shell}'
        return first + '@ ' + str(id(self)) + '>'

    def __str__(self):
        toppings = (f' with {",".join(self.toppings)}' if self.toppings else '')
        return (f'{self.shell}shell {self.protein} taco {toppings}')

    def __format__(self, fmt_spec):
        if fmt_spec.endswith('d'):
            return str(sum(ord(char) for char in self.__str__()))
        return self.__str__()

t1 = Taco('hard', 'chicken')
t2 = Taco('soft', 'tofu', toppings=['cheese', 'lettuce', 'sour cream'])