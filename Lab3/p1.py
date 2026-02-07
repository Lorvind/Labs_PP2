def is_valid(n: int):
    while n > 0:
        if n % 10 % 2 != 0:
            return False
        n //= 10
    
    return True

n = int(input())

if is_valid(n):
    print("Valid")
else:
    print("Not valid")