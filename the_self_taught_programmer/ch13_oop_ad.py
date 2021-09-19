# 클래스 변수와 인스턴스 변수
class Rectangle:
    # 클래스 변수
    recs = []

    def __init__(self, w, l):
        # 인스턴스 변수
        self.width = w
        # 인스턴스 변수
        self.len = l
        self.recs.append((self.width, self.len))

    def print_size(self):
        print("""{} by {}
              """.format(self.width, self.len))


r1 = Rectangle(23, 42)
r2 = Rectangle(29, 48)
r3 = Rectangle(15, 82)

print(Rectangle.recs)


# 매직 메서드
class Lion:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


shock_lion = Lion("shock")
print(shock_lion)


# 표현식의 피연산자는 연산자가 사용할 매직메서드를 포함하고 있어야함 (더하기를 하려면 피연산자가 더하기 기능을 가지고 있어야 한다는 말)
class AlwaysPositive:
    def __init__(self, number):
        self.n = number

    def __add__(self, other):
        return abs(self.n + other.n)


x = AlwaysPositive(-34)
y = AlwaysPositive(12)

print(x + y)
# result : 22

# is 키워드 : 같은 객체인지 확인
x = 10
if x is None:
    print("x is None :(")
else:
    print("x is not None")

x = None
if x is None:
    print("x is None :(")
else:
    print("x is not None")
