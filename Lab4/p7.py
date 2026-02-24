class Reverse:
    def __iter__(self):
        self.i = -1
        return self

    def __init__(self, s: str):
        self.s = s

    def __next__(self):
        if self.i < -len(self.s):
            raise StopIteration
        c = self.s[self.i]
        self.i -= 1
        return c

s = input()

reverser = Reverse(s)

for c in reverser:
    print(c, end='')