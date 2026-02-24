def gen_multiples(n):
    i = 0

    while i <= n:
        if i % 12 == 0:
            yield i
        
        i += 1

n = int(input())

for multiple in gen_multiples(n):
    print(multiple, end=' ')
