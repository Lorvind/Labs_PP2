def fib(n):

    i = 0
    a = 0
    b = 1
    c = 1

    while i < n:
        if i == 0: yield 0
        elif i == 1: yield 1
        else:
            c = a + b
            yield c
            a, b = b, c
        i += 1

n = int(input())
fibs = fib(n)

for i in range(n - 1):
    print(next(fibs), end=',')
if n != 0:
    print(next(fibs))