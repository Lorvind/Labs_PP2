def degrees_of_two(n):
    i = 0
    while i <= n:
        yield 2**i
        i += 1

n = int(input())

for degree in degrees_of_two(n):
    print(degree, end=' ')