class Pair:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def pair_sum(self, another_pair):
        self.a += another_pair.a
        self.b += another_pair.b
        

    def display(self):
        print(f"Result: {self.a} {self.b}")

a, b, c, d = list(map(int, input().split()))

pair1 = Pair(a, b)
pair2 = Pair(c, d)

pair1.pair_sum(pair2)
pair1.display()
