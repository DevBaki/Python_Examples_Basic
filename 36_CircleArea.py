import math


class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        print(math.pi * self.radius ** 2)


cir = Circle(2)
cir.area()
