n = int(input())

squares = list(map(lambda x: int(x)**2, input().split()))

total = sum(squares)

print(total)