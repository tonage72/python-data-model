from concurrent.futures import ProcessPoolExecutor

class Adder:
    def __init__(self, add_number):
        self.number = add_number
    def __call__(self, value):
        return self.number + value

add_one = Adder(1)
add_three = Adder(3)

numbers = [1, 2, 3, 4, 5]
with ProcessPoolExecutor() as e:
    results = e.map(add_three, numbers)
    print(list(results))