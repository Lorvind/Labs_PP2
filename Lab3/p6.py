class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return length * width

length, width = list(map(int, input().split()))

my_shape = Rectangle(length, width)
print(my_shape.area())