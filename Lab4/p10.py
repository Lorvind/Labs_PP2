def cycle(items: list, n: int):
    for i in range(n):
        for item in items:
            yield item

items = input().split()
n = int(input())

for item in cycle(items, n):
    print(item, end=' ')