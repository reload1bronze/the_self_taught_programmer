class Square:
    square_list = []

    def __init__(self, w):
        self.width = w
        self.square_list.append(self)

    def calculate_perimeter(self):
        return self.width * 4

    def change_size(self, num):
        self.width += num

    # 객체를 출력할 때 어떻게 표시할지 정의
    def __repr__(self):
        print("d")
        return "{} by {} by {} by {}".format(self.width, self.width, self.width, self.width)


def same_or_not(a, b):
    if a is b:
        return True
    else:
        return False


square_one = Square(3)
square_one_se = square_one
square_two = Square(5)

print(Square.square_list)
# result : [3 by 3 by 3 by 3, 5 by 5 by 5 by 5]
print(square_one)
# result : 3 by 3 by 3 by 3
print(square_two)
# result : 5 by 5 by 5 by 5

print(same_or_not(square_one, square_one_se))
print(same_or_not(square_one, square_two))
