numbers = list(map(int, input().split()))

is_prime = lambda x: x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))

numbers = list(filter(is_prime, numbers))

if numbers:
    for num in numbers:
        print(num, end=' ')
else:
    print("No primes")