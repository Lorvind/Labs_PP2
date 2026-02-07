class Shape:
    def area(self):
        return 0

class Square(Shape):
    length: int

    def area(self):
        return self.length ** 2

my_shape = Square()
my_shape.length = int(input())
print(my_shape.area())