from random import randint

class Car:

    __slots__ = ('color', 'year')

    def __init__(self, color, year):
        self.color = color
        self.year = year

first = Car('red', 1997)
second = Car('blue', 2001)
third = Car('red', 1997)

reviews = {}
reviews[first] = 'awesome'
reviews[second] = 'meh'
reviews[third] = 'it is okay'