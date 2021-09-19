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


class Triangle:
    def __init__(self, length, height):
        self.length = length
        self.height = height

    def area(self):
        print((self.length * self.height) * (1 / 2))


triangle = Triangle(10, 10)
triangle.area()
