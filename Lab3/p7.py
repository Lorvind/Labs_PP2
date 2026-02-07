class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self, x, y):
        self.x = x
        self.y = y

    def dist(self, point):
        dist_x = self.x - point.x
        dist_y = self.y - point.y
        dist = (dist_x * dist_x+ dist_y * dist_y) ** 0.5
        return f"{dist:.2f}"

x, y = list(map(int, input().split()))

point1 = Point(x, y)
point1.show()

x, y = list(map(int, input().split()))
point1.move(x, y)
point1.show()

x, y = list(map(int, input().split()))
point2 = Point(x, y)
print(point1.dist(point2))