from math import ceil, floor

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return "<Point (x={self.x}, y={self.y})>".format(self=self)

    def __float__(self):
        return float(self.x)

    #def __floor__(self):
    #    return float(floor(self.x))

p = Point(3.6, 2.7)