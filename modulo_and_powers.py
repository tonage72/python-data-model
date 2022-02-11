class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return "<Point (x={self.x}, y={self.y})>".format(self=self)

    def __mod__(self, other):
        return Point(self.x % other.x, self.y % other.y)

    def __rmod__(self, other):
        print('rmod')

    def __imod__(self, other):
        self.x %= other.x
        self.y %= other.y
        return self

p1 = Point(0, 0)
p2 = Point(1, 3)
p3 = Point(-2, -4)