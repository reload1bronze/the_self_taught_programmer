# Encapsulation 캡슐화
class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def area(self):
        return self.width * self.len


class Data:
    def __init__(self):
        self.nums = [1, 2, 3, 4, 5]

    def change_data(self, index, n):
        self.nums[index] = n


# 은닉
# 파이썬에는 private 없음
class PublicPrivateExample:
    def __init__(self):
        self.public = "safe"
        self._private = "unsafe"

    def public_method(self):
        pass

    def _unsafe_method(self):
        pass


# Abstraction 추상화

# Polymorphism 다형성
print("Hello, world")
print(200)
print(200.9)

# shape = ["tr1", "sq1", "cr1"]
# for a_shape in shape:
#     a_shape.draw()


# Inheritance 상속
class Shape:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("""{} by {}
              """.format(self.width, self.len))


class Square(Shape):
    def area(self):
        return self.width * self.len

    def print_size(self):
        print("""I am {} by {}
              """.format(self.width, self.len))


a_square = Square(20, 20)
a_square.print_size()


# Composition 합성
class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner


class Person:
    def __init__(self, name):
        self.name = name


shock = Person("Shock Wave")
stan = Dog("Stanley",
           "Bulldog",
           shock)
print(stan.owner.name)

