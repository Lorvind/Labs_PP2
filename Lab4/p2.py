def evens(n: int):
    i = 0

    while i < n - 1:
        
        i += 2
        yield i

n = int(input())

print(0, end='')

for even in evens(n):
    print(',', even, sep='', end='')
