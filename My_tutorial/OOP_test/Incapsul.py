import math


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.area = math.pi * radius ** 2


c1 = Circle(1)
print(c1.area)

c1.radius = 100
print(c1.area)

class Point:
    def __init__(self, coordinates):
        self.x = coordinates[0]
        self.y = coordinates[1]

    def move(self, delta):
        self.x = self.x + delta[0]
        self.y = self.y + delta[1]


p1 = Point([1, 3])
print(p1.x, p1.y)

p1.move([2, 3])
print(p1.x, p1.y)
