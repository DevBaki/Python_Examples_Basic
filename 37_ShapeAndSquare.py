class Shape:
    def __init__(self):
        pass

    def area(self):
        return 2


class Square(Shape):
    def __init__(self, l):
        Shape.__init__(self)
        self.length = l

    def area(self):
        return self.length * self.length


square = Square(3)
print(square.area())

shape=Shape()
print(shape.area())
