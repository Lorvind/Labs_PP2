a = input()

total = 0

nums = list(map(int, input().split()))

for num in nums:
    if num > 0:
        total += 1

print(total)