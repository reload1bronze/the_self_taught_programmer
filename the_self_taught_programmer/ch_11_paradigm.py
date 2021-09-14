import math


class Apple:
    def __init__(self, color, hardness, size, weight):
        self.color = color
        self.hardness = hardness
        self.size = size
        self.weight = weight


class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        print(self.radius ** 2 * math.pi)


circle = Circle(10)
circle.area()
