def is_prime(n: int):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primes(n):
    i = 2

    while i <= n:
        if is_prime(i):
            yield i
        i += 1

n = int(input())

for prime in primes(n):
    print(prime, end=' ')