class Shape:
    def what_am_i(self):
        print("I am a shape")


class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def calculate_perimeter(self):
        return self.width * 2 + self.len * 2


class Square(Shape):
    def __init(self, w):
        self.width = w

    def calculate_perimeter(self):
        return self.width * 4

    def change_size(self, num):
        self.width += num


class Horse:
    def __init__(self, owner):
        self.owner = owner


class Rider:
    def __init__(self, name):
        self.name = name


rider = Rider("wave")
horse = Horse(rider)
print(horse.owner.name)
