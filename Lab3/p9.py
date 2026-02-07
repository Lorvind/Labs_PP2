class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        pi = 3.14159
        area = pi * self.radius * self.radius
        return f"{area:.2f}"

my_circle = Circle(int(input()))
print(my_circle.area())
