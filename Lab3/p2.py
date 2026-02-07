def is_usual(n: int):
    while n % 2 == 0:
        n //= 2
    while n % 3 == 0:
        n //= 3
    while n % 5 == 0:
        n //= 5

    if n == 1:
        return True
    else:
        return False

n = int(input())

if is_usual(n):
    print("Yes")
else:
    print("No")