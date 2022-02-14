class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return "<Point (x={self.x}, y={self.y})>".format(self=self)

    

p1 = Point(1, 2)
p2 = Point(3, 2)
p3 = Point(-5, -4)